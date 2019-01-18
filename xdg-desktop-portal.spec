%define _disable_lto 1
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: xdg-desktop-portal
Version: 1.1.1
Release: 1
Source0: https://github.com/flatpak/xdg-desktop-portal/archive/%{name}-%{version}.tar.xz
Summary: D-Bus service providing native file dialogs
URL: http://github.com/flatpak/xdg-desktop-portal
License: GPL
Group: System/Libraries
BuildRequires: autoconf automake libtool gettext-devel make
BuildRequires: xmlto
BuildRequires: systemd-macros
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(fontconfig)
BuildRequires: pkgconfig(libpipewire-0.2)
BuildRequires: pkgconfig(libgeoclue-2.0) >= 2.5.2
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
Requires: xdg-desktop-portal-implementation

%description
D-Bus service providing native file dialogs.

%prep
%autosetup -p1
[ -e autogen.sh ] && ./autogen.sh
%configure

%build
%make_build

%install
%make_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_prefix}/lib/systemd/user/xdg-desktop-portal.service
%{_prefix}/lib/systemd/user/xdg-document-portal.service
%{_prefix}/lib/systemd/user/xdg-permission-store.service
%{_libexecdir}/xdg-desktop-portal-validate-icon
%{_libexecdir}/xdg-desktop-portal
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Access.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Account.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.AppChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Email.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.FileChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Inhibit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Lockdown.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Notification.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.PermissionStore.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Print.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.RemoteDesktop.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Request.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.ScreenCast.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Settings.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Account.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Email.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.FileChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Inhibit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.NetworkMonitor.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Notification.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.OpenURI.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Print.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.ProxyResolver.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.RemoteDesktop.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Request.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.ScreenCast.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Settings.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Trash.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
%doc %{_docdir}/xdg-desktop-portal
%{_datadir}/pkgconfig/xdg-desktop-portal.pc
