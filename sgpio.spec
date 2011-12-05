Summary: SGPIO captive backplane tool
Name: sgpio
Version: 1.2.0.10
Release: 5%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing
Source: sgpio-1.2-0.10-src.tar.gz
# there is no official download link for the latest package
#Source: http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing?action=AttachFile&do=get&target=sgpio-1.2.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch0: sgpio-1.2-makefile.patch
BuildRequires: dos2unix

%description
Intel SGPIO enclosure management utility

%prep
%setup -q -n sgpio
%patch0 -p1 -b .makefile
dos2unix --keepdate README
chmod a-x *

%build
#@@@ workaround for #474755 - remove with next update
make clean
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT SBIN_DIR=$RPM_BUILD_ROOT/sbin MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc README LICENSE_GPL
/sbin/sgpio
%{_mandir}/man1/sgpio.*

%changelog
* Wed Feb 24 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 1.2.0.10-5
- added license file
- Related: rhbz#543948 

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.0.10-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009  Jiri Moskovcak <jmoskovc@redhat.com> 1.2.0.10-3
- rebuild for F12

* Tue Apr 14 2009  Jiri Moskovcak <jmoskovc@redhat.com> 1.2.0.10-2
- move the EOL conversion and the removal of 
  executable bits from %%install to %%prep section

* Wed Dec 10 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.2.0_10-1
- initial Fedora release