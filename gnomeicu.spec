Summary:	GnomeICU is a clone of Mirabilis' popular ICQ written with GTK
Summary(fr):	Programme pour la communication sur Internet
Name:		gnomeicu
Version:	0.93
Release:	1
License:	GPL
Vendor:		Jeremy Wise <jwise@pathwaynet.com>
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source:		ftp://gnomeicu.gdev.net/pub/gnomeicu/%{name}-%{version}.tar.gz
URL:		http://gnomeicu.gdev.net/
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-core-devel >= 1.1.5
BuildRequires:	gettext-devel
Requires:	gnome-libs >= 1.0.0
Requires:	ORBit >= 0.4.0
Requires:	gtk+ >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK. The original
source was taken from Matt Smith's mICQ. This is ment as a replacement for
the JavaICQ, which is slow and buggy.

%description -l fr
gnomeICU est un programme de communication par Internet qui utilise le
protocole d'ICQ.

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
	--with-statusmenu \
	--enable-compile-warnings=no

make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Networking/ICQ

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
%{_applnkdir}/Networking/ICQ/GnomeICU.desktop
%{_datadir}/pixmaps/*
%{_datadir}/sounds/gnomeicu
