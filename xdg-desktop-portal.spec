%define _disable_lto 1
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: xdg-desktop-portal
Version: 1.10.1
Release: 1
Source0: https://github.com/flatpak/xdg-desktop-portal/archive/%{version}/%{name}-%{version}.tar.xz
Summary: D-Bus service providing native file dialogs
URL: http://github.com/flatpak/xdg-desktop-portal
License: GPL
Group: System/Libraries
BuildRequires: autoconf automake libtool gettext-devel make
BuildRequires: xmlto
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libgeoclue-2.0) >= 2.5.2
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libportal)
Requires: xdg-desktop-portal-implementation
Requires: dbus

%description
D-Bus service providing native file dialogs.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The pkg-config file for %{name}.

%prep
%autosetup -p1
[ -e autogen.sh ] && ./autogen.sh
%configure --with-systemduserunitdir=%{_userunitdir}

%build
%make_build

%install
%make_install
# This directory is used by implementations such as xdg-desktop-portal-gtk.
install -dm 755 %{buildroot}%{_datadir}/%{name}/portals

%find_lang %{name} --all-name --with-html

%post
%systemd_user_post %{name}.service
%systemd_user_post xdg-document-portal.service
%systemd_user_post xdg-permission-store.service

%preun
%systemd_user_preun %{name}.service
%systemd_user_preun xdg-document-portal.service
%systemd_user_preun xdg-permission-store.service

%files -f %{name}.lang
%{_userunitdir}/xdg-*.service
%{_libexecdir}/xdg-desktop-portal
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_datadir}/%{name}/portals
%{_datadir}/dbus-1/interfaces/org.freedesktop.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.*.service
%doc %{_docdir}/xdg-desktop-portal

%files devel
%{_datadir}/pkgconfig/xdg-desktop-portal.pc
