%define libname 		%mklibname sm 6
%define develname 	%mklibname sm -d
%define staticname 	%mklibname sm -s -d

Name: libsm
Summary:  X Session Management Library
Version: 1.2.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libice-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
This is the X Session Management Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Session Management Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
This is the X Session Management Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Requires: libice-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: libsm-devel = %{version}-%{release}
Provides: libsm6-devel = %{version}-%{release}
Obsoletes: %{mklibname sm 6}-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libSM.so
%{_libdir}/libSM.la
%{_libdir}/pkgconfig/sm.pc
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libsm-static-devel = %{version}-%{release}
Provides: libsm6-static-devel = %{version}-%{release}
Obsoletes: %{mklibname sm 6}-static-devel
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libSM.a

#-----------------------------------------------------------

%prep
%setup -q -n libSM-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}\
		--without-libuuid

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%_datadir/doc/libSM

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc doc/*.xml
%{_libdir}/libSM.so.6
%{_libdir}/libSM.so.6.0.1
