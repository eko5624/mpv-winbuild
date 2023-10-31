#!/bin/bash
set -ex  
CURL_RETRIES="--connect-timeout 60 --retry 5 --retry-delay 5"

#Get mpv latest commit sha
short_sha=$(cat /github/home/opt/mpv/SHORT_SHA)
body=$(cat <<END
Bump to mpv-player/mpv@${short_sha}
**Compiler**: clang
END
)

id=$(curl -u $GITHUB_ACTOR:$GH_TOKEN $CURL_RETRIES \
  -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/${GITHUB_REPOSITORY}/releases \
  -d @- <<END | jq -r '.id' 
{
  "tag_name": "'"$date"'",
  "name":"'"$date"'",
  "body": "$(echo ${body//$'\n'/'\n'})"
}
END
)
  
for f in *.7z; do
  curl -u $GITHUB_ACTOR:$GH_TOKEN $CURL_RETRIES \
    -X POST -H "Accept: application/vnd.github.v3+json" \
    -H "Content-Type: $(file -b --mime-type $f)" \
    https://uploads.github.com/repos/${GITHUB_REPOSITORY}/releases/$id/assets?name=$(basename $f) --data-binary @$f; 
done
