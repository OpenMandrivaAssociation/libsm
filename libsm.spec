%define	major	6
%define	libname	%mklibname sm %{major}
%define	devname	%mklibname sm -d

Name:		libsm
Summary:	X Session Management Library
Version:	1.2.1
Release:	5
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.bz2

BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	x11-xtrans-devel >= 1.0.0

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
Conflicts:	libxorg-x11-devel < 7.0

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

%changelog
* Thu Jan 31 2013 Per Øyvind Karlsen <peroyvind@mandriva.org 1.2.1-4
- drop useless provides
- cleanups after ABF merge

* Tue Mar 06 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.1-1
+ Revision: 782307
- 1.2.1

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-4
+ Revision: 745629
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3
+ Revision: 662415
- mass rebuild

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 638499
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Thu Oct 28 2010 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 589800
- new release
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2010.1
+ Revision: 520908
- rebuilt for 2010.1

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.1-1mdv2010.0
+ Revision: 411530
- Update to new version 1.1.1

* Tue Jul 15 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.1.0-1mdv2009.0
+ Revision: 236193
- Compile without libuuid
- Update to version 1.1.0

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-4mdv2009.0
+ Revision: 214370
- Rebuild to match changes in xtrans.
- Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 151480
- Update BuildRequires and rebuild.

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2008.1
+ Revision: 150828
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon May 14 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 26644
- new release


* Fri Mar 16 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0.1-3mdv2007.1
+ Revision: 144824
- Rebuild to allow automated pkgconfig Provides: to be added.

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description

