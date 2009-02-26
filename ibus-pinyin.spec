%define	version 1.1.0.20090225
%define	release %mkrel 1

Name:      ibus-pinyin
Summary:   ibus - Chinese Pinyin engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:   http://ibus.googlecode.com/files/pinyin-database-0.1.10.6.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: swig
Requires:	ibus >= 1.1.0

%description
ibus - Chinese Pinyin engine.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} engine

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml
