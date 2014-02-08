%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

Summary:        An STMP/POP2/IMAP protocol implementation together with clients and servers
Name:           python-twisted-mail
Version:        13.0.0
Release:        2
Source0:        http://twistedmatrix.com/Releases/Mail/13.0/TwistedMail-%{version}.tar.bz2
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
