pkgname = "ptyxis"
pkgver = "48.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "doxygen",
    "pkgconf",
]
makedepends = [
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgtop-devel",
    "pcre2-devel",
    "vte-gtk4-devel",
    "json-glib-devel",
    "libportal-devel",
]
pkgdesc = "Ptyxis"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/chergert/ptyxis"
source = (
    f"$(GNOME_SITE)/ptyxis/{pkgver[:-2]}/ptyxis-{pkgver}.tar.xz"
)
sha256 = "f91f8ebe1bb1aef6bf772a994d6b4f4d0832c28baf6384c27461bbc6af2aad8e"
