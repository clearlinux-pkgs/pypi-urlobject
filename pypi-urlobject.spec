#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-urlobject
Version  : 2.4.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/e2/b8/1d0a916f4b34c4618846e6da0e4eeaa8fcb4a2f39e006434fe38acb74b34/URLObject-2.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/b8/1d0a916f4b34c4618846e6da0e4eeaa8fcb4a2f39e006434fe38acb74b34/URLObject-2.4.3.tar.gz
Summary  : A utility class for manipulating URLs.
Group    : Development/Tools
License  : Unlicense
Requires: pypi-urlobject-license = %{version}-%{release}
Requires: pypi-urlobject-python = %{version}-%{release}
Requires: pypi-urlobject-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
URLObject 2
===========
|PyPI| |Build Status| |Coverage Report| |Python Versions|

%package license
Summary: license components for the pypi-urlobject package.
Group: Default

%description license
license components for the pypi-urlobject package.


%package python
Summary: python components for the pypi-urlobject package.
Group: Default
Requires: pypi-urlobject-python3 = %{version}-%{release}

%description python
python components for the pypi-urlobject package.


%package python3
Summary: python3 components for the pypi-urlobject package.
Group: Default
Requires: python3-core
Provides: pypi(urlobject)

%description python3
python3 components for the pypi-urlobject package.


%prep
%setup -q -n URLObject-2.4.3
cd %{_builddir}/URLObject-2.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639050847
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-urlobject
cp %{_builddir}/URLObject-2.4.3/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-urlobject/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-urlobject/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
