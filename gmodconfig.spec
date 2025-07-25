Summary:	Graphic interface to configure Linux kernel modules
Summary(pl.UTF-8):	Graficzny interfejs do konfiguracji modułów jądra Linuksa
Name:		gmodconfig
Version:	0.6
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gmodconfig/%{name}-%{version}.tar.gz
# Source0-md5:	776596b1820f2e1584ab2f8b8c666922
Patch0:		%{name}-assert.patch
Patch1:		%{name}-modules.patch
URL:		http://gmodconfig.sourceforge.net/
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxml2-devel >= 2.5.0
BuildRequires:	rpm-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gmodconfig is a GNOME application which allows (or will allow) Linux
users to:

 - configure kernel modules' parameters,
 - check for new versions of kernel modules, as well as download, build
   and install those
 - access kernel modules informations (license, authors, link to
   website).

%description -l pl.UTF-8
gmodconfig jest aplikacją GNOME, pozwalającą użytkownikowi:

 - konfigurować parametry modułów jądra,
 - sprawdzać czy są nowsze wersje modułów jądra, oraz ściągać je,
   budować i instalować,
 - odczytać informację o modułach (licencja, autorzy, odnośnik do
   strony WWW).

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_libdir}/bonobo/servers/*
