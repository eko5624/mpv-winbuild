pkgname=config
pkgver=1.0
pkgrel=1
pkgdesc='MPV config files'
arch=('x86_64')
url="https://github.com/eko5624/mpv-config/"
license=('custom')
source=(git+"https://github.com/eko5624/mpv-config")
options=(!strip)
md5sums=('SKIP')

package() {
  export PATH="${TOP_DIR}/cross/bin:$PATH"
  export PKG_CONFIG_LIBDIR="${MINGW_PREFIX}/lib/pkgconfig"
  export PKG_CONFIG="pkgconf --static"
  export PKGEXT='.pkg.tar.xz'
  mkdir -p $pkgdir${MINGW_PREFIX}/mpv
  cd $srcdir/mpv-config
  mv portable_config $pkgdir${MINGW_PREFIX}/mpv
  mv installer $pkgdir${MINGW_PREFIX}/mpv
  mv d3dcompiler_43.dll $pkgdir${MINGW_PREFIX}/mpv
}
