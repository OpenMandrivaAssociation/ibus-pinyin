%define	version 1.3.5
%define	release %mkrel 1

Name:      ibus-pinyin
Summary:   ibus - Chinese Pinyin engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:   http://ibus.googlecode.com/files/pinyin-database-1.2.99.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python
BuildRequires: ibus-devel >= 1.3.0
BuildRequires: sqlite3-tools
BuildRequires: sqlite3-devel
BuildRequires: libuuid-devel
BuildRequires: boost-devel
BuildRequires: intltool
Requires:	ibus >= 1.3.0

%description
ibus - Chinese Pinyin engine.

%package    open-phrase
Summary:    The open phrase database for ibus Pinyin
Group:      System/Internationalization
Requires:   %{name} = %{version}

%description open-phrase
The open phrase database for ibus Pinyin engine.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} data/db/open-phrase

%build
%configure2_5x --enable-db-open-phrase
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
%exclude %{_datadir}/ibus-pinyin/db/open-phrase.db
%{_datadir}/ibus/component/*.xml

%files open-phrase
%defattr(-,root,root)
%{_datadir}/ibus-pinyin/db/open-phrase.db
