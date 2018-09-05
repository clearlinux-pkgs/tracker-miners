#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tracker-miners
Version  : 2.1.4
Release  : 15
URL      : https://download.gnome.org/sources/tracker-miners/2.1/tracker-miners-2.1.4.tar.xz
Source0  : https://download.gnome.org/sources/tracker-miners/2.1/tracker-miners-2.1.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: tracker-miners-config
Requires: tracker-miners-lib
Requires: tracker-miners-bin
Requires: tracker-miners-data
Requires: tracker-miners-license
Requires: tracker-miners-locales
Requires: tracker-miners-man
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(exempi-2.0)
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gstreamer-tag-1.0)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libosinfo-1.0)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(taglib_c)
BuildRequires : pkgconfig(totem-plparser)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(vorbisfile)
BuildRequires : tracker-dev

%description
1 Introduction
Tracker is a search engine and that allows the user to find their
data as fast as possible. Users can search for their files and
search for content in their files too.

%package bin
Summary: bin components for the tracker-miners package.
Group: Binaries
Requires: tracker-miners-data
Requires: tracker-miners-config
Requires: tracker-miners-license
Requires: tracker-miners-man

%description bin
bin components for the tracker-miners package.


%package config
Summary: config components for the tracker-miners package.
Group: Default

%description config
config components for the tracker-miners package.


%package data
Summary: data components for the tracker-miners package.
Group: Data

%description data
data components for the tracker-miners package.


%package lib
Summary: lib components for the tracker-miners package.
Group: Libraries
Requires: tracker-miners-data
Requires: tracker-miners-license

%description lib
lib components for the tracker-miners package.


%package license
Summary: license components for the tracker-miners package.
Group: Default

%description license
license components for the tracker-miners package.


%package locales
Summary: locales components for the tracker-miners package.
Group: Default

%description locales
locales components for the tracker-miners package.


%package man
Summary: man components for the tracker-miners package.
Group: Default

%description man
man components for the tracker-miners package.


%prep
%setup -q -n tracker-miners-2.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536124730
%configure --disable-static --disable-schemas-compile --disable-journal --disable-libstemmer --disable-upower --disable-hal --disable-libexif --disable-libiptcdata --disable-exempi --disable-extract --disable-tracker-writeback --disable-miner-apps --disable-miner-rss --disable-taglib --disable-enca --disable-icu-charset-detection --disable-libxml2 --disable-unzip-ps-gz-files --disable-poppler --disable-libgxps --disable-libgsf --disable-libosinfo --disable-libgif --disable-libjpeg --disable-libtiff --disable-libpng --disable-libvorbis --disable-libflac --disable-libcue --disable-abiword --disable-dvi --disable-mp3 --disable-ps --disable-text --disable-icon --disable-playlist --disable-guarantee-metadata
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1536124730
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/tracker-miners
cp COPYING.GPL %{buildroot}/usr/share/doc/tracker-miners/COPYING.GPL
cp COPYING.LGPL %{buildroot}/usr/share/doc/tracker-miners/COPYING.LGPL
cp src/libtracker-miners-common/COPYING.LIB %{buildroot}/usr/share/doc/tracker-miners/src_libtracker-miners-common_COPYING.LIB
%make_install
%find_lang tracker-miners

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/tracker-extract
/usr/libexec/tracker-miner-fs

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/tracker-extract.service
/usr/lib/systemd/user/tracker-miner-fs.service

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.freedesktop.Tracker1.Miner.Extract.service
/usr/share/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.TrackerMiners.enums.xml
/usr/share/tracker-miners/extract-rules/10-bmp.rule
/usr/share/tracker-miners/extract-rules/10-comics.rule
/usr/share/tracker-miners/extract-rules/10-ebooks.rule
/usr/share/tracker-miners/extract-rules/10-raw.rule
/usr/share/tracker-miners/extract-rules/10-svg.rule
/usr/share/tracker-miners/extract-rules/15-gstreamer-guess.rule
/usr/share/tracker-miners/extract-rules/90-gstreamer-audio-generic.rule
/usr/share/tracker-miners/extract-rules/90-gstreamer-image-generic.rule
/usr/share/tracker-miners/extract-rules/90-gstreamer-video-generic.rule
/usr/share/tracker/miners/org.freedesktop.Tracker1.Miner.Extract.service
/usr/share/tracker/miners/org.freedesktop.Tracker1.Miner.Files.service

%files lib
%defattr(-,root,root,-)
/usr/lib64/tracker-miners-2.0/extract-modules/libextract-bmp.so
/usr/lib64/tracker-miners-2.0/extract-modules/libextract-dummy.so
/usr/lib64/tracker-miners-2.0/extract-modules/libextract-gstreamer.so
/usr/lib64/tracker-miners-2.0/extract-modules/libextract-raw.so
/usr/lib64/tracker-miners-2.0/libtracker-extract.so
/usr/lib64/tracker-miners-2.0/libtracker-extract.so.0
/usr/lib64/tracker-miners-2.0/libtracker-extract.so.0.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/tracker-miners/COPYING.GPL
/usr/share/doc/tracker-miners/COPYING.LGPL
/usr/share/doc/tracker-miners/src_libtracker-miners-common_COPYING.LIB

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/tracker-extract.1
/usr/share/man/man1/tracker-miner-fs.1
/usr/share/man/man1/tracker-writeback.1

%files locales -f tracker-miners.lang
%defattr(-,root,root,-)

