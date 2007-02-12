Summary:	Portslave - RADIUS client
Summary(pl.UTF-8):   Portslave - klient RADIUS
Name:		portslave
Version:	1.2.0pre12
Release:	1
Group:		Networking/Daemons
License:	GPL
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	48d013411514bc206607217a7e410c27
#Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/portslave/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://sourceforge.net/projects/portslave/
Requires:	radius
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portslave is a RADIUS client. RADIUS (Remote Authentication Dial-In
User Service), simply put allows you to authenticate logins from a
central RADIUS server without having to keep user account information
on multiple machines. As the name states RADIUS is primarily used in
terminal servers (aka RAS: Remote Auth Servers) for logging in dial in
modem users. Portslave can 'answer the line' and act as the RADIUS
client for this as well as other Unix services such as telnet and
secure shell (ssh).

%description -l pl.UTF-8
Portslave jest klientem RADIUS-a. RADIUS (Remote Authentication
Dial-In User Service - serwis autentykacji wdzwaniających się
użytkowników) pozwala na autentykację logowania z centralnego serwera
RADIUS bez potrzeby trzymania kont użytkowników na wielu maszynach.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -D_GNU_SOURCE -DVERSION=\\\"\$(VERSION)\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{portslave,rc.d/init.d},%{_sbindir}}

install pslave.conf $RPM_BUILD_ROOT%{_sysconfdir}/portslave

install src/{portslave,radinit,ctlportslave} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LICENSE ChangeLog TODO MAINTAINERS
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%attr(640,root,root) %config %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
