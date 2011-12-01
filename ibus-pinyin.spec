%define	version 1.3.11
%define	release %mkrel 3

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
BuildRequires: ibus-devel >= 1.3.9-5
BuildRequires: sqlite3-tools
BuildRequires: sqlite3-devel
BuildRequires: libuuid-devel
BuildRequires: boost-devel
BuildRequires: intltool
BuildRequires: opencc-devel
Requires:	ibus >= 1.3.0
Requires(post,preun): GConf2

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
%configure2_5x --enable-db-open-phrase --enable-opencc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%post
%post_ibus_register_engine pinyin zh_CN
%post_ibus_register_engine bopomofo zh_TW

%preun
%preun_ibus_unregister_engine pinyin
%preun_ibus_unregister_engine bopomofo

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/ibus*
%{_datadir}/%{name}
%exclude %{_datadir}/ibus-pinyin/db/open-phrase.db
%{_datadir}/ibus/component/*.xml

%files open-phrase
%defattr(-,root,root)
%{_datadir}/ibus-pinyin/db/open-phrase.db
