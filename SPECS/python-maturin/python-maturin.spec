# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname maturin

Name:           python-%{srcname}
Version:        1.13.3
Release:        %autorelease
Summary:        Build and publish Rust crates as Python packages
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
#!RemoteAsset:  sha256:771e1e9e71a278e56db01552e0d1acfd1464259f9575b6e72842f893cd299079
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:54efe94ac7fb7b28fb7c8c97ff6d77f854295d782c43e3f033e61617df1e1b5d
Source1:        https://github.com/TakoPack/python-%{srcname}-vendor/releases/download/vendor-%{version}/%{srcname}-%{version}-vendor.tar.bz2
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  cargo

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%prep -a
sed -i '1{/env python/d}' maturin/__init__.py
sed -i 's/--locked/--frozen/' setup.py

mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license license-apache license-mit
%doc README.md Changelog.md
%{_bindir}/maturin

%changelog
%autochangelog
