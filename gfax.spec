Summary:	The GNOME Fax Application
Summary(pl):	Aplikacja GNOME do faksów
Name:		gfax
Version:	0.4.2
Release:	4
License:	GPL
Group:		Applications/Communications
Source0:	http://www.cowlug.org/gfax/%{name}-%{version}.tar.gz
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
URL:		http://www.cowlug.org/gfax/
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__gettextize}
aclocal -I macros
CFLAGS="%{optflags} `pkg-config libglade-gnome --cflags`"
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/Misc

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README FAQ-gfax
%attr(755,root,root) %{_bindir}/gfax
%{_datadir}/gfax
%{_pixmapsdir}/*
%{_applnkdir}/Office/Misc/*
