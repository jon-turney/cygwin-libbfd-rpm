%{?cygwin_package_header}

Name:           cygwin-libbfd
Version:        2.31.1
Release:        1%{?dist}
Summary:        Cygwin BFD and opcodes libraries

License:        GPLv2+ and LGPLv2+ and GPLv3+ and LGPLv3+
Group:          Development/Libraries
URL:            http://www.gnu.org/software/binutils/
BuildArch:      noarch

Source0:        http://ftpmirror.gnu.org/binutils/binutils-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  texinfo

BuildRequires:  cygwin32-filesystem
BuildRequires:  cygwin32-gcc
BuildRequires:  cygwin32
BuildRequires:  cygwin32-gettext
BuildRequires:  cygwin32-zlib

BuildRequires:  cygwin64-filesystem
BuildRequires:  cygwin64-gcc
BuildRequires:  cygwin64
BuildRequires:  cygwin64-gettext
BuildRequires:  cygwin64-zlib

%description
This package contains Cygwin cross-compiled BFD and opcodes static
libraries.

%package -n cygwin32-libbfd
Summary:        Cygwin32 BFD and opcodes libraries
Group:          Development/Libraries
Requires:       cygwin32-filesystem
Requires:       cygwin32
Requires:       cygwin32-gettext-static
Requires:       cygwin32-zlib-static

%description -n cygwin32-libbfd
This package contains Cygwin i686 cross-compiled BFD and opcodes static
libraries. Only static libraries are provided because the API is too
unstable to be used dynamically.

%package -n cygwin64-libbfd
Summary:        Cygwin64 BFD and opcodes libraries
Group:          Development/Libraries
Requires:       cygwin64-filesystem
Requires:       cygwin64
Requires:       cygwin64-gettext-static
Requires:       cygwin64-zlib-static

%description -n cygwin64-libbfd
This package contains Cygwin x86_64 cross-compiled BFD and opcodes static
libraries. Only static libraries are provided because the API is too
unstable to be used dynamically.


%prep
%setup -q -n binutils-%{version}


%build
%cygwin_configure \
  --without-included-gettext \
  --enable-install-libiberty \
  --disable-win32-registry \
  --disable-werror

%cygwin_make %{?_smp_flags} all-libiberty all-opcodes all-bfd


%install
%cygwin_make DESTDIR=$RPM_BUILD_ROOT install-libiberty install-opcodes install-bfd

# These files conflict with ordinary binutils.
rm -rf $RPM_BUILD_ROOT%{cygwin32_infodir}
rm -rf $RPM_BUILD_ROOT%{cygwin32_datadir}/locale/
rm -rf $RPM_BUILD_ROOT%{cygwin64_infodir}
rm -rf $RPM_BUILD_ROOT%{cygwin64_datadir}/locale/

# Do not ship .la files
find $RPM_BUILD_ROOT -name '*.la' -delete


%files -n cygwin32-libbfd
%{cygwin32_includedir}/ansidecl.h
%{cygwin32_includedir}/bfd.h
%{cygwin32_includedir}/bfdlink.h
%{cygwin32_includedir}/diagnostics.h
%{cygwin32_includedir}/dis-asm.h
%{cygwin32_includedir}/plugin-api.h
%{cygwin32_includedir}/symcat.h
%{cygwin32_includedir}/libiberty/
%{cygwin32_libdir}/libbfd.a
%{cygwin32_libdir}/libiberty.a
%{cygwin32_libdir}/libopcodes.a

%files -n cygwin64-libbfd
%{cygwin64_includedir}/ansidecl.h
%{cygwin64_includedir}/bfd.h
%{cygwin64_includedir}/bfdlink.h
%{cygwin64_includedir}/diagnostics.h
%{cygwin64_includedir}/dis-asm.h
%{cygwin64_includedir}/plugin-api.h
%{cygwin64_includedir}/symcat.h
%{cygwin64_includedir}/libiberty/
%{cygwin64_libdir}/libbfd.a
%{cygwin64_libdir}/libiberty.a
%{cygwin64_libdir}/libopcodes.a


%changelog
* Thu Dec 20 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 2.31.1-1
- new version

* Tue Dec 05 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 2.29.1-1
- new version

* Mon Sep 12 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.25.1-1
- new version

* Sun Jun 30 2013 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.23.52-1
- Version bump.
- Adapt to new Cygwin packaging scheme.
- Add cygwin64 package.

* Sun Mar 09 2013 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.23.51-1
- Version bump.

* Thu Jan 24 2013 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.22.51-2
- Renamed package.
- Rebuilt for cygwin-gettext-0.18.1.1-2 changes.

* Sun Oct 23 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.22.51-1
- Version bump.

* Sun Aug 21 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.21.53-1
- Version bump.

* Sun Jul 10 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.21.1-1
- Version bump.

* Sun Mar 13 2011 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.21-1
- Initial RPM release.
