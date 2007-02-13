#
%bcond_without	gtkspell	# without gtkspell support
%bcond_with	applet		# enable applet support
#
Summary:	GnomeICU is a clone of Mirabilis' popular ICQ written with GTK+
Summary(fr.UTF-8):	Programme pour la communication sur Internet
Summary(pl.UTF-8):	GnomeICU - klon Mirabilis ICQ napisany z użyciem GTK+
Name:		gnomeicu
Version:	0.99.5
Release:	2
License:	GPL
Vendor:		Jeremy Wise <jwise@pathwaynet.com>
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gnomeicu/%{name}-%{version}.tar.bz2
# Source0-md5:	59ff902171a14ad37896f6661ddedb7a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale-names.patch
URL:		http://gnomeicu.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
%{?with_applet:BuildRequires:	gnome-panel-devel >= 2.0.0}
BuildRequires:	gtk+2-devel >= 1:2.2.0
%{?with_gtkspell:BuildRequires: gtkspell-devel >= 2.0.4}
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.7
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post):	GConf2
Requires(post,postun):	scrollkeeper >= 0.3.5
Requires:	gtk+2 >= 1:2.2.0
Requires:	libxml2 >= 2.4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnomeICU is a clone of Mirabilis' popular ICQ written with GTK+. The
original source was taken from Matt Smith's mICQ. This is ment as a
replacement for the JavaICQ, which is slow and buggy.

%description -l fr.UTF-8
gnomeICU est un programme de communication par Internet qui utilise le
protocole d'ICQ.

%description -l pl.UTF-8
GnomeICU to klon Mirabilis ICQ napisany z użyciem GTK+. Oryginalne
źródła pochodzą z mICQ Matta Smitha. Ten program ma być zamiennikiem
JavaICQ, które jest wolne i ma błędy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# seems as if xss support is broken on alpha :-(
%configure \
%ifarch alpha
	--without-xss \
%endif
	%{?with_applet:--enable-applet} \
	%{?with_gtkspell:--enable-gtkspell}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING MAINTAINERS NEWS README README.SOCKS TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/sound/events/*
%{_datadir}/sounds/gnomeicu
%{_datadir}/gnomeicu
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
