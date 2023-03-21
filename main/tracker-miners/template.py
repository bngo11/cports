pkgname = "tracker-miners"
pkgver = "3.5.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: user services with dinit?
    "-Ddefault_library=shared",
    "-Dtracker_core=system", "-Dextract=true", "-Dfunctional_tests=false",
    "-Dman=true", "-Dsystemd_user_services=false",
    # features
    "-Dminer_rss=false", # libgrss hasn't been touched in a while
    "-Dplaylist=enabled",
    "-Dexif=enabled",
    "-Djpeg=enabled",
    "-Dtiff=enabled",
    "-Diptc=enabled",
    "-Draw=enabled",
    "-Dxps=enabled",
    "-Dpng=enabled",
    "-Dgif=enabled",
    "-Dpdf=enabled",
    "-Dxml=enabled",
    "-Dcue=enabled",
    "-Dgsf=enabled",
    "-Diso=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "asciidoc", "xsltproc",
]
makedepends = [
    "tracker-devel", "glib-devel", "dbus-devel", "gstreamer-devel",
    "gst-plugins-base-devel", "icu-devel", "libexif-devel", "libseccomp-devel",
    "libjpeg-turbo-devel", "libpng-devel", "libtiff-devel", "giflib-devel",
    "libxml2-devel", "libpoppler-glib-devel", "upower-devel", "exempi-devel",
    "networkmanager-devel", "gexiv2-devel", "totem-pl-parser-devel",
    "libgxps-devel", "libcue-devel", "libgsf-devel", "libiptcdata-devel",
    "libosinfo-devel",
]
pkgdesc = "Data miners for tracker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gnome.pages.gitlab.gnome.org/tracker"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "17966603dc432a98526b490586a48acd7f9f59935f7895dfc51729a46a6901a3"
# check relies on stuff unsupported in chroot
options = ["!check", "!cross"]
