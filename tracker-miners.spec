#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : tracker-miners
Version  : 3.5.0
Release  : 47
URL      : https://download.gnome.org/sources/tracker-miners/3.5/tracker-miners-3.5.0.tar.xz
Source0  : https://download.gnome.org/sources/tracker-miners/3.5/tracker-miners-3.5.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: tracker-miners-data = %{version}-%{release}
Requires: tracker-miners-lib = %{version}-%{release}
Requires: tracker-miners-libexec = %{version}-%{release}
Requires: tracker-miners-license = %{version}-%{release}
Requires: tracker-miners-locales = %{version}-%{release}
Requires: tracker-miners-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gstreamer-dev
BuildRequires : libseccomp-dev
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-audio-1.0)
BuildRequires : pkgconfig(gstreamer-pbutils-1.0)
BuildRequires : pkgconfig(gstreamer-tag-1.0)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(tracker-sparql-3.0)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pygobject
BuildRequires : tracker-dev
BuildRequires : upower-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Tracker Miners
Tracker is an efficient search engine and
[triplestore](https://en.wikipedia.org/wiki/Triplestore) for desktop, embedded
and mobile.

%package data
Summary: data components for the tracker-miners package.
Group: Data

%description data
data components for the tracker-miners package.


%package lib
Summary: lib components for the tracker-miners package.
Group: Libraries
Requires: tracker-miners-data = %{version}-%{release}
Requires: tracker-miners-libexec = %{version}-%{release}
Requires: tracker-miners-license = %{version}-%{release}

%description lib
lib components for the tracker-miners package.


%package libexec
Summary: libexec components for the tracker-miners package.
Group: Default
Requires: tracker-miners-license = %{version}-%{release}

%description libexec
libexec components for the tracker-miners package.


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


%package services
Summary: services components for the tracker-miners package.
Group: Systemd services

%description services
services components for the tracker-miners package.


%prep
%setup -q -n tracker-miners-3.5.0
cd %{_builddir}/tracker-miners-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679939965
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dabiword=false \
-Dbattery_detection=none \
-Dcharset_detection=icu \
-Dcue=disabled \
-Dexif=disabled \
-Dextract=true \
-Dgeneric_media_extractor=gstreamer \
-Dgif=disabled \
-Dgsf=disabled \
-Dguarantee_metadata=false \
-Dicon=false \
-Diptc=disabled \
-Diso=disabled \
-Djpeg=disabled \
-Dman=false \
-Dminer_fs=true \
-Dminer_rss=false \
-Dmp3=false \
-Dpdf=disabled \
-Dplaylist=disabled \
-Dpng=disabled \
-Dps=false \
-Draw=enabled \
-Dtext=false \
-Dtiff=disabled \
-Dunzip_ps_gz_files=false \
-Dwriteback=false \
-Dxml=disabled \
-Dxmp=disabled \
-Dxps=disabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/tracker-miners
cp %{_builddir}/tracker-miners-%{version}/COPYING.GPL %{buildroot}/usr/share/package-licenses/tracker-miners/33fabce185708a9b17df7a9f37c7ed44eddc7e48 || :
cp %{_builddir}/tracker-miners-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/tracker-miners/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/tracker-miners-%{version}/src/libtracker-miners-common/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker-miners/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tracker3-miners
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/.
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.Files.Index.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.xml
/usr/share/dbus-1/services/org.freedesktop.Tracker3.Miner.Extract.service
/usr/share/dbus-1/services/org.freedesktop.Tracker3.Miner.Files.Control.service
/usr/share/dbus-1/services/org.freedesktop.Tracker3.Miner.Files.service
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker3.Extract.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker3.FTS.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker3.Miner.Files.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.TrackerMiners3.enums.xml
/usr/share/tracker3-miners/domain-ontologies/default.rule
/usr/share/tracker3-miners/extract-rules/10-bmp.rule
/usr/share/tracker3-miners/extract-rules/10-comics.rule
/usr/share/tracker3-miners/extract-rules/10-desktop.rule
/usr/share/tracker3-miners/extract-rules/10-ebooks.rule
/usr/share/tracker3-miners/extract-rules/10-folder.rule
/usr/share/tracker3-miners/extract-rules/10-raw.rule
/usr/share/tracker3-miners/extract-rules/10-svg.rule
/usr/share/tracker3-miners/extract-rules/15-executable.rule
/usr/share/tracker3-miners/extract-rules/15-games.rule
/usr/share/tracker3-miners/extract-rules/15-gstreamer-guess.rule
/usr/share/tracker3-miners/extract-rules/90-gstreamer-audio-generic.rule
/usr/share/tracker3-miners/extract-rules/90-gstreamer-video-generic.rule
/usr/share/tracker3-miners/miners/org.freedesktop.Tracker3.Miner.Files.service
/usr/share/xdg/autostart/tracker-miner-fs-3.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/tracker-miners-3.0/extract-modules/libextract-bmp.so
/usr/lib64/tracker-miners-3.0/extract-modules/libextract-desktop.so
/usr/lib64/tracker-miners-3.0/extract-modules/libextract-dummy.so
/usr/lib64/tracker-miners-3.0/extract-modules/libextract-gstreamer.so
/usr/lib64/tracker-miners-3.0/extract-modules/libextract-raw.so
/usr/lib64/tracker-miners-3.0/libtracker-extract.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/tracker-extract-3
/usr/libexec/tracker-miner-fs-3
/usr/libexec/tracker-miner-fs-control-3
/usr/libexec/tracker3/daemon
/usr/libexec/tracker3/extract
/usr/libexec/tracker3/index
/usr/libexec/tracker3/info
/usr/libexec/tracker3/reset
/usr/libexec/tracker3/search
/usr/libexec/tracker3/status
/usr/libexec/tracker3/tag

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tracker-miners/33fabce185708a9b17df7a9f37c7ed44eddc7e48
/usr/share/package-licenses/tracker-miners/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/tracker-extract-3.service
/usr/lib/systemd/user/tracker-miner-fs-3.service
/usr/lib/systemd/user/tracker-miner-fs-control-3.service

%files locales -f tracker3-miners.lang
%defattr(-,root,root,-)

