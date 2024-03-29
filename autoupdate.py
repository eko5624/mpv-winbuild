import json
from urllib import request
import in_place

resp = request.urlopen('https://github.com/eko5624/nginx-nosni/raw/master/old.json')
x = json.loads(resp.read().decode('utf-8'))
    
pkgs = {} 
curl = x['curl']
pkgs['libsixel'] = x['libsixel']     
pkgs['vapoursynth'] = x['VapourSynth'][1:]
for p in ['curl', 'mpv', 'ffmpeg', 'luajit2', 'mujs', 'rubberband']:
  pkgs['%s' % p] = x[p]
pkgs['libvorbis_aotuv-dev'] = x['libvorbis']
for p in [
  'amf',
  'aom',
  'angle',
  'avisynth',
  'brotli',
  'dav1d',
  'davs2',
  'ffnvcodec',
  'freetype2',
  'fribidi',
  'harfbuzz',
  'highway',
  'lame',
  'lcms2',
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
  'mbedtls',
  'openal-soft',
  'openssl',
  'opus',
  'rav1e',
  'shaderc',
  'spirv-cross',
  'uavs3d',
  'vulkan',
  'xxhash',
  'zlib',
  ]:
  pkgs['%s-dev' % p] = x[p]
for p in pkgs:
  with in_place.InPlace('%s/PKGBUILD' % p, newline='') as f:
    for l in f:
      if l.startswith('pkgver'):
        l = 'pkgver=%s\n' % pkgs[p]
      f.write(l)
pkgs['amf-headers-dev'] = x['amf']
pkgs['angle-headers-dev'] = x['angle']
pkgs['libsixel-dev'] = x['libsixel']     
pkgs['luajit2-dev'] = x['luajit2']
pkgs['mujs-dev'] = x['mujs']
pkgs['rubberband-dev'] = x['rubberband']
pkgs['vapoursynth-dev'] = x['VapourSynth'][1:]
pkgs['ffmpeg-dev'] = x['ffmpeg']
pkgs['ffmpeg-git'] = x['ffmpeg']
pkgs['ffmpeg-thinlto'] = x['ffmpeg']
pkgs['libmpv-git'] = x['mpv']
pkgs['mpv-git'] = x['mpv']
pkgs['mpv-thinlto'] = x['mpv']
pkgs['shaderc-thinlto'] = x['shaderc']

for t in ['build-mpv-clang.yml', 'build-mpv-gcc-mcf.yml', 'ffmpeg.yml', 'mpv.yml', 'libplacebo.yml', 'shaderc.yml', 'vulkan.yml']:
  with in_place.InPlace('.github/workflows/%s' % t, newline='') as f:
    for l in f:
      if (i:=l.find('/dev-llvm-clang-$BIT/')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+21:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+21], p, pkgs[p], l[r:])
      elif (i:=l.find('/latest-llvm-clang-$BIT/')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+24:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+24], p, pkgs[p], l[r:])
      elif (i:=l.find('/dev-gcc-mcf-$BIT/')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+18:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+18], p, pkgs[p], l[r:])
      elif (i:=l.find('/latest-gcc-mcf-$BIT/')) > -1:
        r = l.find('-1-x86_64')
        rr = l.rfind('-', i, r)
        p = l[i+21:rr]
        if p in pkgs:
          l = '%s%s-%s%s' % (l[:i+21], p, pkgs[p], l[r:])
      elif (i:=l.find('/yt-dlp/releases/download/')) > -1:
        l = '%s%s/yt-dlp.exe\n' % (l[:i+26], x['yt-dlp'])                 
      f.write(l)