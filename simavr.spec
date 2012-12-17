Summary:	A lean, mean and hackable AVR simulator
Name:		simavr
Version:	1.0
Release:	2
License:	GPL v3
Group:		Applications
Source0:	https://github.com/downloads/buserror-uk/simavr/%{name}-%{version}.tar.bz2
# Source0-md5:	82c9704a4e8569548f01931e32ebfe0c
Patch0:		%{name}-build.patch
BuildRequires:	cross_avr_libc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A lean, mean and hackable AVR simulator.

%prep
%setup -q
%patch0 -p1

%{__sed} -i "s/^\(SIMAVR_VERSION\).*/\1 = ${version}/" simavr/Makefile

%build
export CFLAGS="%{rpmcflags}"
%{__make} -j1 \
	CC="%{__cc}"			\
	SIMAVR_VERSION=1.0		\
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=%{_bindir}	\
	DESTDIR=$RPM_BUILD_ROOT	\
	INCLDIR=%{_includedir}	\
	LIBDIR=%{_libdir}

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.md
%attr(755,root,root) %{_bindir}/simavr
%attr(755,root,root) %{_libdir}/libsimavr.so.1

%if 0
%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsimavr.so
%{_includedir}/simavr
%{_pkgconfigdir}/*.pc
%endif

