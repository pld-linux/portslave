# $Revision: 1.9 $
Summary:	Portslave - RADIUS client
Name:		portslave
Version:	1.2.0pre12
Release:	1
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
License:	GPL
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.miquels.cistron.nl/radius/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	radius

%description
Portslave is a RADIUS client. RADIUS (Remote Authentication Dial-In
User Service), simply put allows you to authenticate logins from a
central RADIUS server without having to keep user account information
on multiple machines. As the name states RADIUS is primarily used in
terminal servers (aka RAS: Remote Auth Servers) for logging in dial in
modem users. Portslave can 'answer the line' and act as the RADIUS
client for this as well as other Unix services such as telnet and
secure shell (ssh).

%prep
%setup -q
%patch -p1
%build
cd src
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{portslave,rc.d/init.d},%{_sbindir}}

install pslave.conf $RPM_BUILD_ROOT%{_sysconfdir}/portslave

install src/{portslave,radinit,ctlportslave $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf README* LICENSE ChangeLog TODO MAINTAINERS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README*,LICENSE,ChangeLog,TODO,MAINTAINERS}.gz
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/portslave/*
