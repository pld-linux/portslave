# $Revision: 1.3 $
Summary:	Portslave
Name:		portslave
Version:	1.2.0pre12
Release:	1
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Copyright:	GPL
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.miquels.cistrom.nl/radius
BuildRoot:	/tmp/%{name}-%{version}-root

%description


%prep
%setup -q
%patch -p1
%build
cd src
make
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{portslave,rc.d/init.d},usr/sbin}

install pslave.conf 		$RPM_BUILD_ROOT%{_sysconfdir}/portslave
install src/portslave 		$RPM_BUILD_ROOT%{_sbindir}
install src/radinit		$RPM_BUILD_ROOT%{_sbindir}
install src/ctlportslave	$RPM_BUILD_ROOT%{_sbindir}

gzip -9nf README* LICENSE ChangeLog TODO MAINTAINERS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README*,LICENSE,ChangeLog,TODO,MAINTAINERS}.gz
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/portslave/*
