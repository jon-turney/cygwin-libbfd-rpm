%{?cygwin_package_header}

%define _make_verbose %{nil}

Name:           cygwin-libbfd
Version:        2.47
Release:        2%{?dist}
Summary:        Cygwin BFD and opcodes libraries

License:        GPLv2+ and LGPLv2+ and GPLv3+ and LGPLv3+
Group:          Development/Libraries
URL:            https://www.gnu.org/software/binutils/
BuildArch:      noarch

Source0:        https://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz
Patch1:         binutils-2.42-cygwin-config-rpath.patch

Patch101:       0001-aarch64-Implement-Structured-Exception-Handling-SEH-.patch
Patch102:       0002-WIP-fix-to-dll-relocations.patch
Patch103:       0003-Add-error-messages-for-invalid-relocations.patch
Patch105:       0005-Add-aarch64-pc-cygwin-target.patch
Patch107:       0007-Add-auto-import-support-to-AArch64-9.patch
Patch108:       0008-PE-COFF-AArch64-avoid-ADRP-for-ABS-small-constants.patch
Patch109:       0009-ld-pep.em-use-mingw_behavior-for-the-aarch64-cygwin-.patch
Patch110:       0010-bfd-restore-the-section_htab-guards-removed-by-b3dcd.patch


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

BuildRequires:  cygwin-aarch64-filesystem
BuildRequires:  cygwin-aarch64-gcc
BuildRequires:  cygwin-aarch64
BuildRequires:  cygwin-aarch64-gettext
BuildRequires:  cygwin-aarch64-zlib

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

%package -n cygwin-aarch64-libbfd
Summary:        Cygwin aarch64 BFD and opcodes libraries
Group:          Development/Libraries
Requires:       cygwin-aarch64-filesystem
Requires:       cygwin-aarch64
Requires:       cygwin-aarch64-gettext-static
Requires:       cygwin-aarch64-zlib-static

%description -n cygwin-aarch64-libbfd
This package contains Cygwin aarch64 cross-compiled BFD and opcodes static
libraries. Only static libraries are provided because the API is too
unstable to be used dynamically.


%prep
%autosetup -n binutils-%{version} -p1


%build
%global cygwin_aarch64_cflags %{cygwin_aarch64_cflags} -O0

%cygwin_configure \
  --enable-64-bit-bfd \
  --without-included-gettext \
  --enable-install-libiberty \
  --disable-win32-registry \
  --disable-werror

%cygwin_make_build all-libiberty all-opcodes all-bfd all-libctf


%install
%cygwin_make DESTDIR=$RPM_BUILD_ROOT install-libiberty install-opcodes install-bfd install-libctf

# These files conflict with ordinary binutils.
rm -rf $RPM_BUILD_ROOT%{cygwin32_infodir}
rm -rf $RPM_BUILD_ROOT%{cygwin32_datadir}/locale/
rm -rf $RPM_BUILD_ROOT%{cygwin64_infodir}
rm -rf $RPM_BUILD_ROOT%{cygwin64_datadir}/locale/
rm -rf $RPM_BUILD_ROOT%{cygwin_aarch64_infodir}
rm -rf $RPM_BUILD_ROOT%{cygwin_aarch64_datadir}/locale/

# Do not ship .la files
find $RPM_BUILD_ROOT -name '*.la' -delete


%files -n cygwin32-libbfd
%{cygwin32_includedir}/ansidecl.h
%{cygwin32_includedir}/bfd.h
%{cygwin32_includedir}/bfdlink.h
%{cygwin32_includedir}/ctf.h
%{cygwin32_includedir}/ctf-api.h
%{cygwin32_includedir}/diagnostics.h
%{cygwin32_includedir}/dis-asm.h
%{cygwin32_includedir}/plugin-api.h
%{cygwin32_includedir}/symcat.h
%{cygwin32_includedir}/libiberty/
%{cygwin32_libdir}/libbfd.a
%{cygwin32_libdir}/libctf.a
%{cygwin32_libdir}/libctf-nobfd.a
%{cygwin32_libdir}/libiberty.a
%{cygwin32_libdir}/libopcodes.a
%{cygwin32_includedir}/sframe-api.h
%{cygwin32_includedir}/sframe.h
%{cygwin32_libdir}/libsframe.a

%files -n cygwin64-libbfd
%{cygwin64_includedir}/ansidecl.h
%{cygwin64_includedir}/bfd.h
%{cygwin64_includedir}/bfdlink.h
%{cygwin64_includedir}/ctf.h
%{cygwin64_includedir}/ctf-api.h
%{cygwin64_includedir}/diagnostics.h
%{cygwin64_includedir}/dis-asm.h
%{cygwin64_includedir}/plugin-api.h
%{cygwin64_includedir}/symcat.h
%{cygwin64_includedir}/libiberty/
%{cygwin64_libdir}/libbfd.a
%{cygwin64_libdir}/libctf.a
%{cygwin64_libdir}/libctf-nobfd.a
%{cygwin64_libdir}/libiberty.a
%{cygwin64_libdir}/libopcodes.a
%{cygwin64_includedir}/sframe-api.h
%{cygwin64_includedir}/sframe.h
%{cygwin64_libdir}/libsframe.a

%files -n cygwin-aarch64-libbfd
%{cygwin_aarch64_includedir}/ansidecl.h
%{cygwin_aarch64_includedir}/bfd.h
%{cygwin_aarch64_includedir}/bfdlink.h
%{cygwin_aarch64_includedir}/ctf.h
%{cygwin_aarch64_includedir}/ctf-api.h
%{cygwin_aarch64_includedir}/diagnostics.h
%{cygwin_aarch64_includedir}/dis-asm.h
%{cygwin_aarch64_includedir}/plugin-api.h
%{cygwin_aarch64_includedir}/symcat.h
%{cygwin_aarch64_includedir}/libiberty/
%{cygwin_aarch64_libdir}/libbfd.a
%{cygwin_aarch64_libdir}/libctf.a
%{cygwin_aarch64_libdir}/libctf-nobfd.a
%{cygwin_aarch64_libdir}/libiberty.a
%{cygwin_aarch64_libdir}/libopcodes.a
%{cygwin_aarch64_includedir}/sframe-api.h
%{cygwin_aarch64_includedir}/sframe.h
%{cygwin_aarch64_libdir}/libsframe.a


%changelog
* Mon Sep 28 2026 Jon Turney <jon.turney@dronecode.org.uk> - 2.42-2
- add aarch64

* Mon Sep 28 2026 Jon Turney <jon.turney@dronecode.org.uk> - 2.42-1
- new version

* Thu Aug 26 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 2.37-1
- new version

* Wed Apr  1 2020 Yaakov Selkowitz <yselkowi@redhat.com> - 2.34-1
- new version

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
