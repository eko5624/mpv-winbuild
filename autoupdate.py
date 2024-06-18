import json
from urllib import request
import in_place

resp = request.urlopen('https://github.com/eko5624/nginx-nosni/raw/master/old.json')
x = json.loads(resp.read().decode('utf-8'))
x = dict(map(lambda p: (p, x['data'][p]['version']), x['data'].keys()))

pkgs = {}
for p in ['mpv', 'ffmpeg', 'luajit2']:
  pkgs['%s' % p] = x[p]
for p in [
  'aom',
  'avisynth',
  'brotli',
  'bzip2',
  'dav1d',
  'davs2',
  'expat',
  'ffnvcodec',
  'freetype2',
  'fribidi',
  'harfbuzz',
  'highway',
  'lame',
  'lcms2',
  'libarchive',
  'libaribcaption',
  'libass',
  'libbluray',
  'libbs2b',
  'libcaca',
  'libdovi', 
  'libdvdcss',
  'libdvdnav',
  'libdvdread',
  'libiconv',
  'libjxl',
  'libudfread',
  'libunibreak',
  'libjpeg',
  'libmodplug',
  'libmysofa',
  'libogg',
  'libopenmpt',
  'libplacebo',
  'libpng',
  'libsamplerate',
  'libsdl2',
  'libsixel',
  'libspeex',
  'libssh',
  'libsrt',
  'libva',
  'libvpl',
  'libwebp',
  'libxml2',
  'libxvid',
  'libzimg',
  'libzvbi',
  'lzo',
  'mbedtls',
  'mujs',
  'openal-soft',
  'openssl',
  'opus',
  'rav1e',
  'rubberband',
  'shaderc',
  'spirv-cross',
  'svtav1',
  'uavs3d',
  'vulkan',
  'xxhash',
  'xz',
  'zlib',
  'zstd',
  ]:
  pkgs['%s-dev' % p] = x[p]

for p in ['libplacebo-dev', 'mpv', 'ffmpeg', 'vulkan-dev', 'luajit2']:
  with in_place.InPlace('%s/PKGBUILD' % p, newline='') as f:
    for l in f:
      if l.startswith('pkgver'):
        l = 'pkgver=%s\n' % pkgs[p]
      f.write(l)
pkgs['amf-headers-dev'] = x['amf']
pkgs['angle-headers'] =x['angle']
pkgs['ffmpeg-shared'] = x['ffmpeg']
pkgs['ffmpeg-shared-dev'] = x['ffmpeg']
pkgs['libplacebo-shared-dev'] = x['libplacebo']
pkgs['libvorbis_aotuv-dev'] = x['libvorbis']
pkgs['luajit2-shared-dev'] = x['luajit2']
pkgs['luajit2-shared'] = x['luajit2']
pkgs['mpv-shared'] = x['mpv']
pkgs['vapoursynth-dev'] = x['VapourSynth'][1:]
pkgs['vulkan-shared-dev'] = x['vulkan']

for t in ['ffmpeg.yml', 'libplacebo.yml', 'vulkan.yml', 'mpv.yml', 'build-mpv.yml']:
  with in_place.InPlace('.github/workflows/%s' % t, newline='') as f:
    for l in f:
      if (i:=l.find('/dev-$COMPILER-$BIT/')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+20:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+20], p, pkgs[p], l[r:])
      elif (i:=l.find('/latest-$COMPILER-$BIT/')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+23:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+23], p, pkgs[p], l[r:])
      elif (i:=l.find('/yt-dlp/releases/download/')) > -1:
        l = '%s%s/yt-dlp.exe\n' % (l[:i+26], x['yt-dlp'])                 
      f.write(l)