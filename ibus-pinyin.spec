%define	version 1.3.11
%define	release %mkrel 5

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

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


%changelog
* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.3.11-3mdv2011.0
+ Revision: 669824
- rebuild

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 1.3.11-2
+ Revision: 659301
- rebuild for new ibus
- update file list

* Mon Sep 06 2010 Funda Wang <fwang@mandriva.org> 1.3.11-1mdv2011.0
+ Revision: 576253
- new version 1.3.11

* Sat Aug 14 2010 Funda Wang <fwang@mandriva.org> 1.3.10-2mdv2011.0
+ Revision: 569530
- use opencc for chinese convertion

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 1.3.10-1mdv2011.0
+ Revision: 568002
- update to new version 1.3.10

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 1.3.9-1mdv2011.0
+ Revision: 554368
- update to new version 1.3.9

* Thu Jun 24 2010 Funda Wang <fwang@mandriva.org> 1.3.8-1mdv2010.1
+ Revision: 548990
- New version 1.3.8

* Thu May 06 2010 Funda Wang <fwang@mandriva.org> 1.3.5-1mdv2010.1
+ Revision: 542827
- New version 1.3.5
  (fix double pinyin parse problem, half full punct problem)

* Mon Apr 26 2010 Funda Wang <fwang@mandriva.org> 1.3.3-1mdv2010.1
+ Revision: 538890
- BR sigc++
- New version 1.3.3

* Mon Dec 14 2009 Funda Wang <fwang@mandriva.org> 1.2.99.20091211-1mdv2010.1
+ Revision: 478614
- new version 1.2.99.20091211

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090915-1mdv2010.0
+ Revision: 443704
- new version 1.2.0.20090915

* Tue Aug 04 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090617-2mdv2010.0
+ Revision: 408865
- new version 1.2.0

* Fri Jun 12 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090612-1mdv2010.0
+ Revision: 385511
- New version 1.1.0.20090612

* Thu Mar 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090303-1mdv2009.1
+ Revision: 348998
- New version 1.1.0.20090303

* Thu Feb 26 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090225-1mdv2009.1
+ Revision: 345030
- New version 20090225

* Fri Feb 13 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090211-1mdv2009.1
+ Revision: 339995
- update to new version 1.1.0.20090211

* Thu Feb 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090205-2mdv2009.1
+ Revision: 337931
- arch package now

* Thu Feb 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090205-1mdv2009.1
+ Revision: 337895
- New version 1.1.0.20090205

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081004-2mdv2009.1
+ Revision: 318666
- rebuild for new python

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081004-1mdv2009.1
+ Revision: 292263
- New version 0.1.1.20081004

* Fri Sep 05 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080901-1mdv2009.0
+ Revision: 281262
- new version

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080823-1mdv2009.0
+ Revision: 277736
- should be no arch
- import ibus-pinyin


