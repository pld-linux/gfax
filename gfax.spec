Summary:	The GNOME Fax Application.
Name:		gfax
Version:	0.2.1
Release:	1
Copyright:	GPL
Group:		Applications/Communications
Source:		ftp://raven.cc.mala.bc.ca/pub/Linux/%{name}-%{version}.tar.gz
Requires:	gnome-libs >= 1.0.0
Requires:	gnome-objc >= 1.0.2
URL:		http://www.gmsys.com/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%description
Gfax is a popup tool for easily sending facsimilies by printing to a fax
printer.

Gfax works with GNOME.

GNOME is the GNU Network Object Model Environment. That's a fancy name, but
really GNOME is a nice GUI desktop environment.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install
strip $RPM_BUILD_ROOT%{prefix}/bin/* || :

%post
# Set up the lpr link
BINDIR=/usr/bin
LPRBINDIR=/usr/bin

if [ ! -x $LPRBINDIR/lpr.dist ]; then
        mv $LPRBINDIR/lpr $LPRBINDIR/lpr.dist
        ln -s $BINDIR/lpr.gfax $BINDIR/lpr
        chmod +x $BINDIR/lpr
fi

%postun
# Reset the lpr link
BINDIR=/usr/bin
LPRBINDIR=/usr/bin

if [ -x $LPRBINDIR/lpr.dist ]; then
        rm -rf $LPRBINDIR/lpr
        mv $LPRBINDIR/lpr.dist $LPRBINDIR/lpr
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README FAQ-gfax
%{prefix}/bin/*
%{prefix}/share/gnome/apps/Applications/*
%{prefix}/share/gnome/help/gfax/*
