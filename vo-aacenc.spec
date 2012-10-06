Summary:	VisualOn AAC encoder library
Summary(pl.UTF-8):	Biblioteka kodera VisualOn AAC
Name:		vo-aacenc
Version:	0.1.2
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	cc862dce14ea5d688506904160c65a02
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains an encoder implementation of the Advanced Audio
Coding audio codec. The library is based on a codec implementation by
VisualOn as part of the Stagefright framework from the Google Android
project.

%description -l pl.UTF-8
Ta biblioteka zawiera implementację kodera kodeka dźwięku AAC
(Advanced Audio Coding). Jest opaera na implementacji kodeka firmy
VisualOn jako części środowiska Stagefright z projektu Google Android.

%package devel
Summary:	Header files for VisualOn AAC encoder library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki kodera VisualOn AAC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VisualOn AAC encoder library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki kodera VisualOn AAC.

%package static
Summary:	Static VisualOn AAC encoder library
Summary(pl.UTF-8):	Statyczna biblioteka kodera VisualOn AAC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VisualOn AAC encoder library.

%description static -l pl.UTF-8
Statyczna biblioteka kodera VisualOn AAC.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no dependencies and pkg-config file present
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvo-aacenc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NOTICE README
%attr(755,root,root) %{_libdir}/libvo-aacenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvo-aacenc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvo-aacenc.so
%{_includedir}/vo-aacenc
%{_pkgconfigdir}/vo-aacenc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvo-aacenc.a
