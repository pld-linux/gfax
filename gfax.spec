Summary:	The GNOME Fax Application
Summary(pl):	Aplikacja GNOME do faksów
Name:		gfax
Version:	0.6.4
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.cowlug.org/gfax/%{name}-%{version}.tar.gz
# Source0-md5:	9ec7185ed012607fa529b5758e02e0d2
Patch1:		%{name}-destdir.patch
URL:		http://www.cowlug.org/gfax/
BuildRequires:	mono-csharp
BuildRequires:	dotnet-gtk-sharp-devel
BuildArch:	noarch
Requires:	mono >= 0.93
Requires:	dotnet-gtk-sharp >= 0.93
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gfax is a popup tool for easily sending facsimilies by printing to a
fax printer.

Gfax works with GNOME.

%description -l pl
Gfax jest narzêdziem do ³atwego wysy³ania faksów poprzez drukowanie
ich na drukarce faksowej. Gfax dzia³a z GNOME.

%prep
%setup -q
%patch1 -p1

%build
rm -f missing

%{__make} schema
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},/usr/share/applications,%{_sysconfdir}/gconf/schemas,%{_var}/spool/gfax}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -m 644 data/gfax.schema $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/gfax.schemas

%post
%gconf_schema_install
%{_datadir}/gfax/printer-setup.sh --install

%preun
%{_datadir}/gfax/printer-setup.sh --remove


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config %{_sysconfdir}/gconf/schemas/*.schemas
%doc AUTHORS COPYING ChangeLog README INSTALL NEWS TODO
%attr(755,root,root) %{_bindir}/gfax
%attr(755,root,root) %{_bindir}/gfaxlpr
%attr(755,root,root) %{_bindir}/mono-gfax.exe
%dir %{_datadir}/gfax
%{_datadir}/gfax/*.xml
%{_datadir}/gfax/fax-g3.profile
%attr(755,root,root) %{_datadir}/gfax/printer-setup.sh
%{_pixmapsdir}/*
%{_desktopdir}/*
%attr(1777,root,root) %dir %{_var}/spool/gfax
