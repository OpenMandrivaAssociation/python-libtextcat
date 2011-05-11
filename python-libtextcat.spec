%define	oname	pylibtextcat
%define	module	libtextcat

Name:		python-%{module}
Version:	0.2
Release:	1
Summary:	Python bindings for libTextCat
Source0:	http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.xz
License:	BSD
Group:		Development/Python
Url:		http://launchpad.net/pylibtextcat
BuildRequires:	python-devel python-setuptools

%description
PylibTextCat provides a python interface for the libTextCat
library.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%check
python setup.py test

%files
%doc COPYING ChangeLog NEWS README
%{py_platsitedir}/textcat.so
%{py_platsitedir}/pylibtextcat*.egg-info

