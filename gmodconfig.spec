Summary:	Graphic interface to configure Linux kernel modules
Summary(pl):	Graficzny interfejs do konfiguracji modu³ów j±dra Linuksa
Name:		gmodconfig
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c9968a96120a478325554b7de46c06c1
Patch0:		%{name}-assert.patch
URL:		http://gmodconfig.sourceforge.net/
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libxml++-devel >= 0.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gmodconfig is a GNOME application which allows (or will allow) Linux
users to:

 - configure kernel modules' parameters,
 - check for new versions of kernel modules, as well as download, build
   and install those
 - access kernel modules informations (license, authors, link to
   website).

%description -l pl
gmodconfig jest aplikacj± GNOME, pozwalaj±c± u¿ytkownikowi:

 - konfigurowaæ parametry modu³ów j±dra,
 - sprawdzaæ czy s± nowsze wersje modu³ów j±dra, oraz ¶ci±gaæ je,
   budowaæ i instalowaæ,
 - odczytaæ informacjê o modu³ach (licencja, autorzy, odno¶nik do
   strony WWW).

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
