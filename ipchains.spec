Summary:	IP firewall and accounting administration tool
Summary(es):	Herramienta para administraci�n de reglas de firewall
Summary(pl):	Narz�dzie do zarz�dzania filtrem pakiet�w IP
Summary(pt_BR):	Ferramentas para gerenciamento de regras de firewall
Name:		ipchains
Version:	1.3.10
Release:	12
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://netfilter.filewatcher.org/ipchains/%{name}-%{version}.tar.gz
Source1:	http://netfilter.filewatcher.org/ipchains/%{name}-HOWTOs-1.0.7.tar.bz2
Source2:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-fixman.patch
Patch1:		%{name}-Makefile.patch
URL:		http://netfilter.filewatcher.org/ipchains/
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
Herramienta para administraci�n de reglas de firewall.

%description -l pl
W j�drach 2.2.xxx/2.3 filtr IP zosta� znacznie zmodyfikowany (i,
miejmy nadziej�, ulepszony). Ipchains (zast�puj�c dawny ipfwadm) s�u�y
do konfigurowania filtru oraz mechanizm�w logowania przychodz�cych
pakiet�w.

%description -l pt_BR
O ipchains do Linux � uma atualiza��o (e esperamos uma melhoria em
rela��o) ao c�digo normal de firewall do Linux, para os kernels 2.0,
2.1 e 2.2. Elas lhe permitem usar firewalls, mascaramento IP, etc.

%package -n libipfwc
Summary:	Library which manipulates firewall rules
Summary(pl):	Biblioteka do manipulacji regu�ami filtrowania
Version:	0.2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����

%description -n libipfwc
Library which manipulates firewall rules.

%description -n libipfwc -l pl
Biblioteka do manipulacji regu�ami filtrowania.

%package BOOT
Summary:	ipchains for bootdisk
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description BOOT
ipchains for bootdisk.

%prep
%setup -q -a1
%patch -p1
%patch1 -p1

%build
rm -f ipchains
%{__make} -C libipfwc clean
ln -sf %{name}-HOWTOs-1.0.7	doc

%if %{?BOOT:1}%{!?BOOT:0}
%{__make} \
	COPTS="-Os -I%{_kernelsrcdir}/include -I%{_libdir}/bootdisk%{_includedir}" \
	LDFLAGS="-nostdlib -static -s" \
	LDLIBS="%{_libdir}/bootdisk%{_libdir}/crt0.o %{_libdir}/bootdisk%{_libdir}/libc.a -lgcc"
mv -f %{name} %{name}-BOOT
%{__make} clean
%endif

%{__make} COPTS="%{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT


%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_sbindir}
for i in *-BOOT; do 
	install $i $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_sbindir}/`basename $i -BOOT`
done
%endif

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir}/man{4,8}} \
	$RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install ipchains	$RPM_BUILD_ROOT%{_sbindir}
install *.4		$RPM_BUILD_ROOT%{_mandir}/man4
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install libipfwc/*.a	$RPM_BUILD_ROOT%{_libdir}
install libipfwc/*.h	$RPM_BUILD_ROOT%{_includedir}
bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf READ* doc/HOWT*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/HOWTO.txt.gz README.gz doc/*.html.gz
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

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk%{_sbindir}/*
%endif
