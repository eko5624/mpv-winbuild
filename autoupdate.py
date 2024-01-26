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
