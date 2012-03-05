%define major 6
%define libname 		%mklibname sm %{major}
%define develname 	%mklibname sm -d

Name: libsm
Summary:  X Session Management Library
Version: 1.2.1
Release: 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.bz2

BuildRequires: libice-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
This is the X Session Management Library.

%package -n %{libname}
Summary:  X Session Management Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
This is the X Session Management Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libsm-devel = %{version}-%{release}
Obsoletes: %{_lib}sm6-devel
Obsoletes: %{_lib}sm-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libSM-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}\
	--without-libuuid

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%_datadir/doc/libSM

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libSM.so.%{major}*

%files -n %{develname}
%doc doc/*.xml
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h

