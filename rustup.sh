#!/bin/bash
set -e

TOP_DIR=$(pwd)

# Speed up the process
# Env Var NUMJOBS overrides automatic detection
MJOBS=$(grep -c processor /proc/cpuinfo)

export M_ROOT=$(pwd)
export M_CROSS=$M_ROOT/cross
export RUSTUP_LOCATION=$M_ROOT/rust

export PATH="$M_CROSS/bin:$RUSTUP_LOCATION/.cargo/bin:$PATH"
export PKG_CONFIG="pkgconf --static"
export PKG_CONFIG_LIBDIR="$M_CROSS/lib/pkgconfig"
export RUSTUP_HOME="$RUSTUP_LOCATION/.rustup"
export CARGO_HOME="$RUSTUP_LOCATION/.cargo"

echo "building rustup"
echo "======================="
curl -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable --target x86_64-pc-windows-gnu --no-modify-path --profile minimal
rustup update
cargo install cargo-c --profile=release-strip --features=vendored-openssl
cat <<EOF >$CARGO_HOME/config
[net]
git-fetch-with-cli = true

[target.x86_64-pc-windows-gnu]
linker = "$M_CROSS/bin/x86_64-w64-mingw32-gcc"
ar = "$M_CROSS/bin/x86_64-w64-mingw32-ar"

[profile.release]
panic = "abort"
strip = true
EOF
