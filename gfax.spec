Summary:	The GNOME Fax Application
Summary(pl):	Aplikacja GNOME do faks�w
Name:		gfax
Version:	0.4.2
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	ftp://raven.cc.mala.bc.ca/pub/Linux/%{name}-%{version}.tar.gz
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
Patch1:		%{name}-add_uk_to_ALL_LINGUAS.aptch
Patch2:		%{name}-time.h.patch
BuildRequires:	bison
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	libglade-devel
URL:		http://www.gmsys.com/gnome-gfax.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gfax is a popup tool for easily sending facsimilies by printing to a
fax printer.

Gfax works with GNOME.

%description -l pl
Gfax jest narz�dziem do �atwego wysy�ania faks�w poprzez drukowanie
ich na drukarce faksowej. Gfax dzia�a z GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
aclocal -I macros
autoconf
automake -a -c
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
%{_pixmapsdir}/*
%{_applnkdir}/Office/Misc/*
