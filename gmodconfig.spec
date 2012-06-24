Summary:	Graphic interface to configure Linux kernel modules
Summary(pl):	Graficzny interfejs do konfiguracji modu��w j�dra Linuksa
Name:		gmodconfig
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gmodconfig.sourceforge.net/
BuildRequires:	libxml++-devel >= 0.22
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gmodconfig is a Gnome application which allows (or will allow) Linux
users to:

 - configure kernel modules' parameters,
 - check for new versions of kernel modules, as well as download, build
   and install those
 - access kernel modules informations (license, authors, link to
   website).

%description -l pl
gmodconfig jest aplikacj� Gnome, pozwalaj�c� u�ytkownikowi:

 - konfigurowa� parametry modu��w j�dra,
 - sprawdza� czy s� nowsze wersje modu��w j�dra, oraz �ci�ga� je,
   budowa� i instalowa�,
 - odczyta� informacj� o modu�ach (licencja, autorzy, odno�nik do
   strony WWW).

%prep
%setup -q

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/*
%{_datadir}/%{name}
