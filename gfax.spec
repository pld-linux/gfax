Summary:	The GNOME Fax Application
Name:		gfax
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://raven.cc.mala.bc.ca/pub/Linux/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-devel
URL:		http://www.gmsys.com/gnome-gfax.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gfax is a popup tool for easily sending facsimilies by printing to a
fax printer.

Gfax works with GNOME.

%description -l pl
Gfax jest narzêdziem do ³atwego wysy³ania faksów poprzez drukowanie
ich na drukarce faksowej. Gfax dzia³a z GNOME.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/Misc

gzip -9nf AUTHORS ChangeLog NEWS README FAQ-gfax

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gfax
%{_datadir}/gfax
%{_datadir}/pixmaps/*
%{_applnkdir}/Office/Misc/*
