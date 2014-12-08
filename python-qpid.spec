%define 	module	qpid
Summary:	Python client library for AMQP
Name:		python-%{module}
Version:	0.30
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://www.apache.org/dist/qpid/%{version}/qpid-python-%{version}.tar.gz
# Source0-md5:	f9099cfdc28b3583de0a2ed7089ae559
URL:		http://qpid.apache.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-saslwrapper
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache Qpid Python client library for AMQP.

%prep
%setup -q -n qpid-python-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/qpid/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%doc examples
%attr(755,root,root) %{_bindir}/qpid-python-test
%dir %{py_sitescriptdir}/qpid
%{py_sitescriptdir}/qpid/*.py[co]
%dir %{py_sitescriptdir}/qpid/messaging
%{py_sitescriptdir}/qpid/messaging/*.py[co]
%dir %{py_sitescriptdir}/qpid/specs
%{py_sitescriptdir}/qpid/specs/*.xml
%{py_sitescriptdir}/qpid/specs/amqp-*.pcl
%{py_sitescriptdir}/qpid/specs/amqp-*.dtd
%{py_sitescriptdir}/qpid_python-%{version}-py*.egg-info
%dir %{py_sitescriptdir}/mllib
%{py_sitescriptdir}/mllib/*.py[co]
