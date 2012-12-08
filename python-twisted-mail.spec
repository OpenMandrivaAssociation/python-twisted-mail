%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        An STMP/POP2/IMAP protocol implementation together with clients and servers
Name:           python-twisted-mail
Version:        12.2.0
Release:        1
Source0:        http://tmrc.mit.edu/mirror/twisted/Mail/%{mainver}/TwistedMail-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedMail
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# for mail/relaymanager.py
Requires:       python-twisted-names

%description
Twisted Mail contains high-level, efficient protocol implementations for both
clients and servers of SMTP, POP3, and IMAP4. Additionally, it contains an
"out of the box" combination SMTP/POP3 virtual-hosting mail server. Also
included is a read/write Maildir implementation and a basic Mail Exchange
calculator (depends on Twisted Names).

%prep
%setup -q -n TwistedMail-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%dir %py_platsitedir/twisted/mail
%py_platsitedir/twisted/mail/*
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
%_mandir/man1/*
