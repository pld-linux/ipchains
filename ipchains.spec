Summary:	IP firewall and accounting administration tool
Summary(pl):	Narzêdzie do zarz±dzania filterm pakietów IP.
Name:		ipchains
Version:	1.3.9
Release:	2
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.rustcorp.com/ipchains/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.rustcorp.com/ipchains/%{name}-HOWTOs-1.0.7.tar.bz2
URL:		http://www.rustcorp.com/linux/ipchains/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr
%define		_sbindir	/sbin

%description
This is the Linux IP Firewalling Chains accounting and administration tool.

Linux IP Firewalling Chains is an update to (and hopefully an improvement
upon) the normal Linux Firewalling code, for 2.2 and 2.3 kernels.

%description -l pl
W j±drach 2.2.xxx/2.3 filtr IP zosta³ znacznie zmodyfikowany (i, miejmy
nadziejê, ulepszony). Ipchains (zastêpuj±c dawny ipfwadm) s³u¿y
do konfigurowania filtru oraz mechanizmów logowania przychodz±cych
pakietów.

%prep
%setup -q -a1

%build
ln -sf %{name}-HOWTOs-1.0.7	doc

make COPTS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_sbindir},%{_bindir},%{_mandir}/man{4,8}}

install -s ipchains	$RPM_BUILD_ROOT%{_sbindir}
install *.4		$RPM_BUILD_ROOT%{_mandir}/man4
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[48]/* READ* doc/HOWT*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/HOWTO.txt.gz README.gz doc/*.html.gz
%attr(755,root,root) /sbin/*
%{_mandir}/man?/*
