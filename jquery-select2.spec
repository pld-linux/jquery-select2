%define		plugin	select2
Summary:	A jQuery based replacement for select boxes
Name:		jquery-%{plugin}
Version:	3.5.1
Release:	1
License:	Apache v2.0 or GPL v2
Group:		Applications/WWW
Source0:	https://github.com/ivaynberg/select2/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	3555acad53ecab30cd3c8843030dedb2
URL:		http://ivaynberg.github.io/select2/
Requires:	jquery >= 1.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Select2 is a jQuery-based replacement for select boxes. It supports
searching, remote data sets, and infinite scrolling of results.

Use cases:
- Enhancing native selects with search.
- Enhancing native selects with a better multi-select interface.
- Loading data from JavaScript: easily load items via ajax and have
  them searchable.
- Nesting optgroups: native selects only support one level of nested.
  Select2 does not have this restriction.
- Tagging: ability to add new items on the fly.
- Working with large, remote datasets: ability to partially load a
  dataset based on the search term.
- Paging of large datasets: easy support for loading more pages when
  the results are scrolled to the end.
- Templating: support for custom rendering of results and selections.

%prep
%setup -q -n %{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p %{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

cp -p %{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

cp -p %{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css
cp -p %{plugin}-bootstrap.css $RPM_BUILD_ROOT%{_appdir}

cp -p *.png *.gif $RPM_BUILD_ROOT%{_appdir}

cp -p %{plugin}_locale_*.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{_appdir}
%{_appdir}/select2.js
%{_appdir}/select2[.-]*.js
%{_appdir}/select2*.css
%{_appdir}/select2*.gif
%{_appdir}/select2*.png

%lang(ar) %{_appdir}/select2_locale_ar.js
%lang(az) %{_appdir}/select2_locale_az.js
%lang(bg) %{_appdir}/select2_locale_bg.js
%lang(ca) %{_appdir}/select2_locale_ca.js
%lang(cs) %{_appdir}/select2_locale_cs.js
%lang(da) %{_appdir}/select2_locale_da.js
%lang(de) %{_appdir}/select2_locale_de.js
%lang(el) %{_appdir}/select2_locale_el.js
%lang(es) %{_appdir}/select2_locale_es.js
%lang(et) %{_appdir}/select2_locale_et.js
%lang(eu) %{_appdir}/select2_locale_eu.js
%lang(fa) %{_appdir}/select2_locale_fa.js
%lang(fi) %{_appdir}/select2_locale_fi.js
%lang(fr) %{_appdir}/select2_locale_fr.js
%lang(gl) %{_appdir}/select2_locale_gl.js
%lang(he) %{_appdir}/select2_locale_he.js
%lang(hr) %{_appdir}/select2_locale_hr.js
%lang(hu) %{_appdir}/select2_locale_hu.js
%lang(id) %{_appdir}/select2_locale_id.js
%lang(is) %{_appdir}/select2_locale_is.js
%lang(it) %{_appdir}/select2_locale_it.js
%lang(ja) %{_appdir}/select2_locale_ja.js
%lang(ka) %{_appdir}/select2_locale_ka.js
%lang(ko) %{_appdir}/select2_locale_ko.js
%lang(lt) %{_appdir}/select2_locale_lt.js
%lang(lv) %{_appdir}/select2_locale_lv.js
%lang(mk) %{_appdir}/select2_locale_mk.js
%lang(ms) %{_appdir}/select2_locale_ms.js
%lang(nl) %{_appdir}/select2_locale_nl.js
%lang(no) %{_appdir}/select2_locale_no.js
%lang(pl) %{_appdir}/select2_locale_pl.js
%lang(pt_BR) %{_appdir}/select2_locale_pt-BR.js
%lang(pt_PT) %{_appdir}/select2_locale_pt-PT.js
%lang(ro) %{_appdir}/select2_locale_ro.js
%lang(rs) %{_appdir}/select2_locale_rs.js
%lang(ru) %{_appdir}/select2_locale_ru.js
%lang(sk) %{_appdir}/select2_locale_sk.js
%lang(sv) %{_appdir}/select2_locale_sv.js
%lang(th) %{_appdir}/select2_locale_th.js
%lang(tr) %{_appdir}/select2_locale_tr.js
%lang(ug_CN) %{_appdir}/select2_locale_ug-CN.js
%lang(uk) %{_appdir}/select2_locale_uk.js
%lang(vi) %{_appdir}/select2_locale_vi.js
%lang(zh_CN) %{_appdir}/select2_locale_zh-CN.js
%lang(zh_TW) %{_appdir}/select2_locale_zh-TW.js
