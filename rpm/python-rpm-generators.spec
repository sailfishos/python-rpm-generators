# Disable automatic bytecompilation. We install only one script and we will
# never "import" it.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:           python-rpm-generators
Summary:        Dependency generators for Python RPMs
Version:        12
Release:        15

# Originally all those files were part of RPM, so license is kept here
License:        GPLv2+
Url:            https://github.com/sailfishos/python-rpm-generators
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-Revert-scripts-pythondistdeps-Backport-switch-to-imp.patch
Patch2:         0002-Remove-not-needed-__pythonname_obsoletes-to-silence-.patch
Patch3:         0003-Always-generate-major-version-provides.patch
BuildArch:      noarch

%description
The python RPM dependency generator is able to automatically add
Requires/Provides and other types of dependencies based on egg/wheel
metadata.

%package -n python3-rpm-generators
Summary:        %{summary}
Requires:       python3-setuptools
# This contains the Lua functions we use:
Requires:       python-srpm-macros >= 3.11
# The point of split
Conflicts:      rpm-build < 4.14.1+git26

%description -n python3-rpm-generators
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.py

%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_fileattrsdir}/pythondist.attr
%{_fileattrsdir}/pythonname.attr
%{_rpmconfigdir}/pythondistdeps.py
%{_rpmconfigdir}/pythonbundles.py
