Summary:	The GNOME Fax Application
Summary(pl):	Aplikacja GNOME do faks�w
Name:		gfax
Version:	0.4.2
Release:	5
License:	GPL
Group:		Applications/Communications
Source0:	http://www.cowlug.org/gfax/%{name}-%{version}.tar.gz
# Source0-md5:	815523780287a97133e85585f0319a20
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
Patch1:		%{name}-add_uk_to_ALL_LINGUAS.aptch
Patch2:		%{name}-time.h.patch
URL:		http://www.cowlug.org/gfax/
BuildRequires:	bison
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	libglade-gnome-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
CFLAGS="%{rpmcflags} `pkg-config libglade-gnome --cflags`"
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