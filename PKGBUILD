
# Maintainer: Evert Vorster <evorster@gmail.com>

pkgname=domovoy_automata
pkgver=1.0.0
pkgrel=1
pkgdesc="KDE System Monitor and helper"
arch=('any')
url="https://github.com/yourusername/domovoy_automata"
license=('GPL-3.0-or-later')
depends=('python' 'python-pyside6' 'python-psutil' 'python-pyqtgraph' 'python-notify2')
source=("$pkgname-$pkgver.tar.gz::https://github.com/evertvorster/domovoy_automata/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1
}
