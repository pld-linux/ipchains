Summary:	IP firewall and accounting administration tool
Summary(es):	Herramienta para administraciСn de reglas de firewall
Summary(pl):	NarzЙdzie do zarz╠dzania filtrem pakietСw IP
Summary(pt_BR):	Ferramentas para gerenciamento de regras de firewall
Summary(ru):	Утилиты для управления пакетными фильтрами ядра Linux
Summary(uk):	Утил╕ти для керування пакетними ф╕льтрами ядра Linux
Summary(zh_CN):	Linux IPv4╥ю╩Пг╫
Name:		ipchains
Version:	1.3.10
Release:	17
License:	GPL
Group:		Applications/System
Source0:	http://www.netfilter.org/ipchains/%{name}-%{version}.tar.gz
# Source0-md5:	44b6df672a6e7bce8902dc67aef6b12a
#Source1:	http://netfilter.filewatcher.org/ipchains/%{name}-HOWTOs-1.0.7.tar.bz2
Source1:	%{name}-HOWTOs-1.0.7.tar.bz2
# Source1-md5:	f4548c7fb6cdfc1015012c8860a5856a
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	460a8227af67f289ac9868706cf89e54
Patch0:		%{name}-fixman.patch
Patch1:		%{name}-vlanallowing.patch
URL:		http://netfilter.filewatcher.org/ipchains/
Provides:	firewall-userspace-tool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_sbindir	/sbin

%description
This is the Linux IP Firewalling Chains accounting and administration
tool.

Linux IP Firewalling Chains is an update to (and hopefully an
improvement upon) the normal Linux Firewalling code, for 2.2 and 2.3
kernels.

%description -l es
Herramienta para administraciСn de reglas de firewall.

%description -l pl
W j╠drach 2.2.xxx/2.3 filtr IP zostaЁ znacznie zmodyfikowany (i,
miejmy nadziejЙ, ulepszony). Ipchains (zastЙpuj╠c dawny ipfwadm) sЁu©y
do konfigurowania filtru oraz mechanizmСw logowania przychodz╠cych
pakietСw.

%description -l pt_BR
O ipchains do Linux И uma atualizaГЦo (e esperamos uma melhoria em
relaГЦo) ao cСdigo normal de firewall do Linux, para os kernels 2.0,
2.1 e 2.2. Elas lhe permitem usar firewalls, mascaramento IP, etc.

%description -l ru
Linux IP Firewalling Chains - это новый набор утилит для управления
пакетными фильтрами ядра Linux. Ipchains позволяют настроить firewall,
IP masquerading и т.п.

%description -l uk
Linux IP Firewalling Chains - це новий наб╕р утил╕т для керування
пакетними ф╕льтрами ядра Linux. Ipchains дозволяють налагодити
firewall, IP masquerading ╕ т.╕.

%package -n libipfwc
Summary:	Library which manipulates firewall rules
Summary(pl):	Biblioteka do manipulacji reguЁami filtrowania
Version:	0.2
Group:		Development/Libraries

%description -n libipfwc
Library which manipulates firewall rules.

%description -n libipfwc -l pl
Biblioteka do manipulacji reguЁami filtrowania.

%prep
%setup -q -a1
%patch -p1
%patch1 -p1

%build
rm -f ipchains
%{__make} -C libipfwc clean
ln -sf %{name}-HOWTOs-1.0.7	doc

%{__make} COPTS="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir}/man{4,8}} \
	$RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install ipchains	$RPM_BUILD_ROOT%{_sbindir}
install *.4		$RPM_BUILD_ROOT%{_mandir}/man4
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install libipfwc/*.a	$RPM_BUILD_ROOT%{_libdir}
install libipfwc/*.h	$RPM_BUILD_ROOT%{_includedir}
bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/HOWTO.txt README doc/*.html
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%lang(es) %{_mandir}/es/man?/*
%lang(it) %{_mandir}/it/man?/*
%lang(ja) %{_mandir}/ja/man?/*
%lang(pl) %{_mandir}/pl/man?/*

%files -n libipfwc
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
