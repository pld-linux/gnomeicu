# Note that this is NOT a relocatable package
# defaults for redhat
%define prefix		/usr
%define sysconfdir	/etc
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Summary: GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
Name: gnomeicu
Version: 0.67
Release: %rel
Copyright: GPL
Group: Applications/Communications
URL: http://gnomeicu.gdev.net/
Source: ftp://gnomeicu.gdev.net/pub/gnomeicu/%{name}-%{version}.tar.gz
Requires: gnome-libs >= 1.0.0
Requires: ORBit >= 0.4.0
Requires: gtk+ >= 1.2.0
Packager: Jeremy Wise <jwise@pathwaynet.com>
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK.
The original source was taken from Matt Smith's mICQ.  This is ment as
a replacement for the JavaICQ, which is slow and buggy.  If you would
like to contribute, please contact Jeremy Wise <jwise@pathwaynet.com>.


%prep
%setup -q

# seems as if xss support is broken on alpha :-(
%ifarch alpha
  ARCH_FLAGS="--host=alpha-redhat-linux --without-xss"
%endif

if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir}
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir}
fi

%build

if [ "$SMP" != "" ]; then
  make -j$SMP "MAKE=make -j$SMP"
else
  make
fi

%install
make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir}  install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{sysconfdir}/CORBA/servers/GnomeICU.gnorba
%config %{sysconfdir}/sound/events/GnomeICU.soundlist
%{prefix}/bin/gnomeicu
%{prefix}/share/applets/Network/GnomeICU.desktop
%{prefix}/share/pixmaps/*
%{prefix}/share/sounds/gnomeicu/*
%{prefix}/share/gnome/help/gnomeicu/*
%{prefix}/share/locale/*/*/*

###################################################################
%changelog
* Fri Sep 10 1999 Herbert Valerio Riedel <hvr@gnu.org>
- added support for SMP builds

* Sun Jul 25 1999 Herbert Valerio Riedel <hvr@gnu.org>
- added online documentation
- added locale files

* Sat Jul 10 1999 Herbert Valerio Riedel <hvr@gnu.org>
- no need to define %{name} and %{version} explicitly (thanks to 
  Graham Cole <dybbuk@earthlink.net> for this hint)

* Tue Jun 29 1999 Herbert Valerio Riedel <hvr@gnu.org>
- first try at an official RPM
