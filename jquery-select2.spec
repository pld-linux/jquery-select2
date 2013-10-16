%define		plugin	select2
Summary:	a jQuery based replacement for select boxes
Name:		jquery-%{plugin}
Version:	3.4.3
Release:	1
License:	Apache v2.0 or GPL v2
Group:		Applications/WWW
Source0:	https://github.com/ivaynberg/select2/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	3495af40e84915c7f1f94570c8d220e6
URL:		https://github.com/ivaynberg/select2
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

cp -p %{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p %{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p %{plugin}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

cp -p *.png *.gif $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{_appdir}
