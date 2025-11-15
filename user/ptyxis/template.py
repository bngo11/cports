pkgname = "ptyxis"
pkgver = "49.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "doxygen",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgtop-devel",
    "libportal-devel",
    "pcre2-devel",
    "vte-gtk4-devel",
]
pkgdesc = "Ptyxis"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/chergert/ptyxis"
source = (
    f"$(GNOME_SITE)/ptyxis/{pkgver[:-2]}/ptyxis-{pkgver}.tar.xz"
)
sha256 = "549b4bfb7e4cbce70a9969949cc6a7b843369e266cf02739666114dc540afcca"
