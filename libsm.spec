%define	major	6
%define	libname	%mklibname sm %{major}
%define	devname	%mklibname sm -d

Summary:	X Session Management Library
Name:		libsm
Version:	1.2.2
Release:	10
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.bz2

BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)

%description
This is the X Session Management Library.

%package -n	%{libname}
Summary:	X Session Management Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
This is the X Session Management Library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}sm6-devel < 1.2.1
Obsoletes:	%{_lib}sm-static-devel < 1.2.1

%description -n	%{devname}
Development files for %{name}

%prep
%setup -qn libSM-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std
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

