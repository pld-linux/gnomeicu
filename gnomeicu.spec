Summary:	GnomeICU is a clone of Mirabilis' popular ICQ written with GTK
Summary(fr):	Programme pour la communication sur Internet
Summary(pl):	GnomeICU - klon Mirabilis ICQ napisany z u¿yciem GTK
Name:		gnomeicu
Version:	0.96.1
Release:	2
License:	GPL
Vendor:		Jeremy Wise <jwise@pathwaynet.com>
Group:		Applications/Communications
Source0:	http://download.sourceforge.net/gnomeicu/%{name}-%{version}.tar.bz2
# Source0-md5:	1286c2d250562fc416836882b89bcdf1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-desktop.patch
URL:		http://gnomeicu.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	ORBit-devel >= 0.4.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-core-devel >= 1.2.0
BuildRequires:	gettext-devel
Requires:	gnome-libs >= 1.2.0
Requires:	ORBit >= 0.5.0
Requires:	gtk+ >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK. The
original source was taken from Matt Smith's mICQ. This is ment as a
replacement for the JavaICQ, which is slow and buggy.

%description -l fr
gnomeICU est un programme de communication par Internet qui utilise le
protocole d'ICQ.

%description -l pl
GnomeICU to klon Mirabilis ICQ napisany z u¿yciem GTK. Oryginalne
¼ród³± pochodz± z mICQ Matta Smitha. Ten program ma byæ zamiennikiem
JavaICQ, które jest wolne i ma b³êdy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
aclocal -I macros
autoconf
automake -a -c
gettextize --force --copy
# seems as if xss support is broken on alpha :-(
%configure \
%ifarch alpha
	--without-xss \
%endif
	--with-statusmenu \
	--enable-compile-warnings=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Network/Communications \
	gnorbadir=%{_sysconfdir}/X11/GNOME/CORBA/servers \
	soundlistdir=%{_sysconfdir}/X11/GNOME/sound/events

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/X11/GNOME/CORBA/servers/GnomeICU.gnorba
%config(noreplace) %verify(not mtime md5 size) %{_sysconfdir}/X11/GNOME/sound/events/GnomeICU.soundlist
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/GnomeICU.desktop
%{_pixmapsdir}/*
%{_datadir}/sounds/gnomeicu
%{_datadir}/gnomeicu
