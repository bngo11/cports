pkgname = "python-passlib"
pkgver = "1.7.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = ["python"]
checkdepends = ["python-bcrypt", "python-pytest-xdist"]
pkgdesc = "Password hashing library for Python"
license = "BSD-3-Clause"
url = "https://passlib.readthedocs.io"
source = f"https://foss.heptapod.net/python-libs/passlib/-/archive/{pkgver}/passlib-{pkgver}.tar.gz"
sha256 = "ea541419716d6011a3ca6f6804d6a0d3f7fecdce0aad2aa655d4ee0d5448edff"
# meh, seems to check libcrypt? also 70% of the tests skip
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
