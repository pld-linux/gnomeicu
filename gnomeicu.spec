Summary:	GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
Name:		gnomeicu
Version:	0.90
Release:	2
License:	GPL
Vendor:		Jeremy Wise <jwise@pathwaynet.com>
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://gnomeicu.gdev.net/pub/gnomeicu/%{name}-%{version}.tar.gz
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-core-devel 
BuildRequires:	gettext-devel
Requires:	gnome-libs >= 1.0.0
Requires:	ORBit >= 0.4.0
Requires:	gtk+ >= 1.2.0
URL:		http://gnomeicu.gdev.net/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK. The original
source was taken from Matt Smith's mICQ. This is ment as a replacement for
the JavaICQ, which is slow and buggy.

%prep
%setup -q

%build
gettextize --force --copy
LDFLAGS="-s"; export LDFLAGS
# seems as if xss support is broken on alpha :-(
%configure \
%ifarch alpha
	--without-xss \
%endif
	--enable-compile-warnings=no

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install 

%find_lang %{name} --with-gnome

gzip -9fn AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%{_sysconfdir}/CORBA/servers/GnomeICU.gnorba
%config %{_sysconfdir}/sound/events/GnomeICU.soundlist
%attr(755,root,root) %{_bindir}/gnomeicu
%{_datadir}/applets/Network/GnomeICU.desktop
%{_datadir}/pixmaps/*
%{_datadir}/sounds/gnomeicu/*
