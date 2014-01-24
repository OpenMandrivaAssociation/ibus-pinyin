Summary:	ibus - Chinese Pinyin engine
Name:		ibus-pinyin
Version:	1.5.0
Release:	1
Group:		System/Internationalization
License:	GPLv2+
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		ibus-pinyin-support-set-content-type-method.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(ibus-1.0) >= 1.3.99
BuildRequires:	pkgconfig(pyzy-1.0) >= 0.0.8
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	sqlite3-tools
Requires:	ibus >= 1.3.99
Obsoletes:	ibus-pinyin-open-phrase < 1.5.0

%description
ibus - Chinese Pinyin engine.

%files -f %{name}.lang
%{_libexecdir}/ibus-engine-pinyin
%{_libexecdir}/ibus-setup-pinyin
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-lua-extension
%make

%install
%makeinstall_std

%find_lang %{name}

