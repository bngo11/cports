pkgname = "xmlcatmgr"
pkgver = "2.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
# trigger on /etc so the hook fires on updates to self
triggers = [
    "/etc/xml",
    "/etc/sgml",
    "/usr/share/xml/catalogs",
    "/usr/share/sgml/catalogs",
]
pkgdesc = "XML and SGML catalog manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://xmlcatmgr.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/xmlcatmgr/{pkgname}-{pkgver}.tar.gz"
sha256 = "ea1142b6aef40fbd624fc3e2130cf10cf081b5fa88e5229c92b8f515779d6fdc"
# ld: error: undefined symbol: setprogname
options = ["!lto"]

if self.profile().cross:
    hostmakedepends = ["xmlcatmgr"]


def post_build(self):
    if self.profile().cross:
        xcmgr = "/usr/bin/xmlcatmgr"
    else:
        xcmgr = self.chroot_cwd / self.make_dir / "xmlcatmgr"

    self.do(xcmgr, "-sc", "catalog.sgml", "create")
    self.do(xcmgr, "-c", "catalog.xml", "create")


def post_install(self):
    self.install_file("catalog.sgml", "etc/sgml", name="catalog")
    self.install_file("catalog.xml", "etc/xml", name="catalog")

    self.install_license("COPYING")
