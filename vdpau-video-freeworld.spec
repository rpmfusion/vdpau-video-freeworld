#global preversion .pre6

Name:		vdpau-video-freeworld
Version:	0.7.3
Release:	1%{?preversion}%{?dist}
Summary:	VDPAU backend for Video Acceleration (VA) API
Group:		System Environment/Libraries
License:	GPLv2+
URL:		http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/
Source0:	http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/vdpau-video-%{version}%{?preversion}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libtool
BuildRequires:	libva-devel >= 1.0.10
BuildRequires:	libvdpau-devel
BuildRequires:	mesa-libGL-devel

%description
Vdpau-video is a VDPAU backend for VA API. It allows applications which
use the VA API for accelerated video playback to work with hardware
that supports the VDPAU API.

%prep
%setup -q -n vdpau-video-%{version}%{?preversion}


%build
%configure --enable-glx

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_libdir}/dri/*.so

%changelog
* Fri Mar 04 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Mon Feb 21 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.3.pre6
- Update to 0.7.3-pre6

* Sun Jan 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.2.pre4
- Update to 0.7.3 pre4

* Wed Dec 15 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-0.1.pre2
- Update to 0.7.3.pre2
- Switch to vdpau-video-freeworld

* Mon Mar 15 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.5-1
- new release

* Thu Jan 21 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.2-1
- new release

* Thu Jan 14 2010 Adam Williamson <adamwill AT shaw.ca> - 0.6.1-1
- new release

* Thu Dec 3 2009 Adam Williamson <adamwill AT shaw.ca> - 0.6.0-1
- new release

* Tue Nov 17 2009 Adam Williamson <adamwill AT shaw.ca> - 0.5.2-1
- new release

* Wed Oct 7 2009 Adam Williamson <adamwill AT shaw.ca> - 0.5.0-1
- new release

* Thu Sep 10 2009 Adam Williamson <adamwill AT shaw.ca> - 0.4.1-1
- new release

* Thu Sep 3 2009 Adam Williamson <adamwill AT shaw.ca> - 0.4.0-1
- initial package
