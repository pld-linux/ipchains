%define		_scriptver	1.1.2
Summary:	IP firewall and accounting administration tool
Summary(es.UTF-8):	Herramienta para administración de reglas de firewall
Summary(pl.UTF-8):	Narzędzie do zarządzania filtrem pakietów IP
Summary(pt_BR.UTF-8):	Ferramentas para gerenciamento de regras de firewall
Summary(ru.UTF-8):	Утилиты для управления пакетными фильтрами ядра Linux
Summary(uk.UTF-8):	Утиліти для керування пакетними фільтрами ядра Linux
Summary(zh_CN.UTF-8):	Linux IPv4防火墙
Name:		ipchains
Version:	1.3.10
Release:	20
License:	GPL
Group:		Applications/System
Source0:	http://www.netfilter.org/ipchains/%{name}-%{version}.tar.gz
# Source0-md5:	44b6df672a6e7bce8902dc67aef6b12a
#Source1:	http://netfilter.filewatcher.org/ipchains/%{name}-HOWTOs-1.0.7.tar.bz2
Source1:	%{name}-HOWTOs-1.0.7.tar.bz2
# Source1-md5:	f4548c7fb6cdfc1015012c8860a5856a
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	460a8227af67f289ac9868706cf89e54
Source3:	http://people.netfilter.org/~rusty/ipchains/%{name}-scripts-%{_scriptver}.tar.gz
# Source3-md5:	c8996aef5985bddf80844b12ae833781
Patch0:		%{name}-fixman.patch
Patch1:		%{name}-vlanallowing.patch
Patch2:		%{name}-gcc.patch
URL:		http://people.netfilter.org/~rusty/ipchains/
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

%description -l es.UTF-8
Herramienta para administración de reglas de firewall.

%description -l pl.UTF-8
W jądrach 2.2.xxx/2.3 filtr IP został znacznie zmodyfikowany (i,
miejmy nadzieję, ulepszony). Ipchains (zastępując dawny ipfwadm) służy
do konfigurowania filtra oraz mechanizmów logowania przychodzących
pakietów.

%description -l pt_BR.UTF-8
O ipchains do Linux é uma atualização (e esperamos uma melhoria em
relação) ao código normal de firewall do Linux, para os kernels 2.0,
2.1 e 2.2. Elas lhe permitem usar firewalls, mascaramento IP, etc.

%description -l ru.UTF-8
Linux IP Firewalling Chains - это новый набор утилит для управления
пакетными фильтрами ядра Linux. Ipchains позволяют настроить firewall,
IP masquerading и т.п.

%description -l uk.UTF-8
Linux IP Firewalling Chains - це новий набір утиліт для керування
пакетними фільтрами ядра Linux. Ipchains дозволяють налагодити
firewall, IP masquerading і т.і.

%package -n libipfwc
Summary:	Library which manipulates firewall rules
Summary(pl.UTF-8):	Biblioteka do manipulacji regułami filtrowania
Version:	0.2
Group:		Development/Libraries

%description -n libipfwc
Library which manipulates firewall rules.

%description -n libipfwc -l pl.UTF-8
Biblioteka do manipulacji regułami filtrowania.

%prep
%setup -q -a1 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} ipchains
ln -sf %{name}-HOWTOs-1.0.7	doc

%build
%{__make} -C libipfwc clean

%{__make} \
	COPTS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir}/man{4,8}} \
	$RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install ipchains	$RPM_BUILD_ROOT%{_sbindir}
cp -p *.4		$RPM_BUILD_ROOT%{_mandir}/man4
cp -p *.8		$RPM_BUILD_ROOT%{_mandir}/man8
cp -p libipfwc/*.a	$RPM_BUILD_ROOT%{_libdir}
cp -p libipfwc/*.h	$RPM_BUILD_ROOT%{_includedir}
cd %{name}-scripts-%{_scriptver}
install ipchains-restore	$RPM_BUILD_ROOT%{_sbindir}
install ipchains-save		$RPM_BUILD_ROOT%{_sbindir}
install ipfwadm-wrapper		$RPM_BUILD_ROOT%{_sbindir}
cp -p *.8			$RPM_BUILD_ROOT%{_mandir}/man8

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/HOWTO.txt README doc/*.html
%attr(755,root,root) %{_sbindir}/ipchains
%attr(755,root,root) %{_sbindir}/ipchains-restore
%attr(755,root,root) %{_sbindir}/ipchains-save
%attr(755,root,root) %{_sbindir}/ipfwadm-wrapper
%{_mandir}/man4/ipfw.4*
%{_mandir}/man8/ipchains.8*
%{_mandir}/man8/ipchains-restore.8*
%{_mandir}/man8/ipchains-save.8*
%{_mandir}/man8/ipfwadm-wrapper.8*
%lang(es) %{_mandir}/es/man8/ipchains.8*
%lang(it) %{_mandir}/it/man4/ipfw.4*
%lang(ja) %{_mandir}/ja/man8/ipchains.8*
%lang(pl) %{_mandir}/pl/man4/ipfw.4*
%lang(pl) %{_mandir}/pl/man8/ipchains.8*

%files -n libipfwc
%defattr(644,root,root,755)
%{_libdir}/libipfwc.a
%{_includedir}/ipfwc_kernel_headers.h
%{_includedir}/libipfwc.h
