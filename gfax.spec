Summary:	The GNOME Fax Application
Summary(pl):	Aplikacja GNOME do faksów
Name:		gfax
Version:	0.6.4
Release:	4
License:	GPL
Group:		Applications/Communications
Source0:	http://gfax.cowlug.org/%{name}-%{version}.tar.gz
# Source0-md5:	9ec7185ed012607fa529b5758e02e0d2
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-amd64.patch
Patch2:		%{name}-desktop.patch
URL:		http://gfax.cowlug.org/
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	mono-csharp
Requires:	dotnet-gtk-sharp >= 0.93
Requires:	mono >= 0.93
ExcludeArch:	alpha
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} schema
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_sysconfdir}/gconf/schemas,%{_var}/spool/gfax}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -m 644 data/gfax.schema $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/gfax.schemas

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
%{_datadir}/gfax/printer-setup.sh --install

%preun
%{_datadir}/gfax/printer-setup.sh --remove

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README INSTALL NEWS TODO
%attr(755,root,root) %{_bindir}/gfax
%attr(755,root,root) %{_bindir}/gfaxlpr
%attr(755,root,root) %{_bindir}/mono-gfax.exe
%dir %{_datadir}/gfax
%{_datadir}/gfax/*.xml
%{_datadir}/gfax/fax-g3.profile
%attr(755,root,root) %{_datadir}/gfax/printer-setup.sh
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%attr(1777,root,root) %dir %{_var}/spool/gfax
