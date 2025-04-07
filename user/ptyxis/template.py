pkgname = "ptyxis"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
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
sha256 = "e71bd6b6a5baedf83cef06e733265498b3f9f516e7efd056585379841652d94f"
