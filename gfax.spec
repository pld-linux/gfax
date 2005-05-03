Summary:	The GNOME Fax Application
Summary(pl):	Aplikacja GNOME do faksów
Name:		gfax
Version:	0.7.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gfax.cowlug.org/%{name}-%{version}-1.tar.gz
# Source0-md5:	59e1430ae0936508ef3814185890213c
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-paths.patch
URL:		http://gfax.cowlug.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel
# wants {gtk,gnome,gconf,glade}-sharp
BuildRequires:	dotnet-gtk-sharp-gnome-devel >= 0.93
BuildRequires:	intltool >= 0.25
# for directory name detection
BuildRequires:	libgnomeprint-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 0.93
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
%requires_eq	libgnomeprint
Requires:	dotnet-gtk-sharp-gnome >= 0.93
Requires:	mono >= 0.93
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gfax is a popup tool for easily sending facsimilies by printing to a
fax printer.

Gfax works with GNOME.

%description -l pl
Gfax jest narzêdziem do ³atwego wysy³ania faksów poprzez drukowanie
ich na drukarce faksowej. Gfax dzia³a z GNOME.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gfax.schemas

%preun
%gconf_schema_uninstall gfax.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README INSTALL NEWS TODO
%attr(755,root,root) %{_bindir}/gfax
%attr(755,root,root) %{_bindir}/gfaxlpr
%dir %{_libdir}/gfax
%attr(755,root,root) %{_libdir}/gfax/gfax.exe
%{_datadir}/libgnomeprint/*/models/GNOME-GFAX-PS.xml
%{_datadir}/libgnomeprint/*/printers/GFAX.xml
%{_pixmapsdir}/*.png
%{_desktopdir}/gfax.desktop
%{_sysconfdir}/gconf/schemas/*.schemas
%attr(1777,root,root) %dir %{_var}/spool/gfax
%attr(1777,root,root) %dir %{_var}/spool/gfax/doneq
%attr(1777,root,root) %dir %{_var}/spool/gfax/recq
