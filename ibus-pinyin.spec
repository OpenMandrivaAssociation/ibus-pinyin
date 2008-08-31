%define	version 0.1.1.20080823
%define	release %mkrel 1

Name:      ibus-pinyin
Summary:   ibus - Chinese Pinyin engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:    http://scim-python.googlecode.com/files/pinyin-database-0.1.10.5.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: swig
BuildArch:	noarch
Requires:	ibus

%description
ibus - Chinese Pinyin engine.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} engine

%build
%configure2_5x --build=%_host
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/ibus/engine/*.engine
