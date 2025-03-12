# libSM is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 6
%define libname %mklibname sm %{major}
%define devname %mklibname sm -d
%if %{with compat32}
%define lib32name libsm%{major}
%define dev32name libsm-devel
%endif

%global optflags %{optflags} -O3

Summary:	X Session Management Library
Name:		libsm
Version:	1.2.6
Release:	1
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.xz

BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libICE)
BuildRequires:	devel(libuuid)
%endif

%description
This is the X Session Management Library.

%package -n	%{libname}
Summary:	X Session Management Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0

%description -n %{libname}
This is the X Session Management Library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}sm6-devel < 1.2.1
Obsoletes:	%{_lib}sm-static-devel < 1.2.1

%description -n	%{devname}
Development files for %{name}.

%if %{with compat32}
%package -n	%{lib32name}
Summary:	X Session Management Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
This is the X Session Management Library.

%package -n	%{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{EVRD}

%description -n	%{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libSM-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
rm -rf %{buildroot}%{_datadir}/doc/libSM

%files -n %{libname}
%{_libdir}/libSM.so.%{major}*

%files -n %{devname}
%doc doc/*.xml
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libSM.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libSM.so
%{_prefix}/lib/pkgconfig/sm.pc
%endif
