# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libclang

Name:           python-%{srcname}
Version:        22.1.4.2
Release:        %autorelease
Summary:        Python bindings for libclang
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/sighingnow/libclang
#!RemoteAsset:  sha256:a459faae992ce87be30620e2303df797f1145dcf2a04dd6c2e7b719fc875a1b9
Source:         https://github.com/kunitoki/libclang-ng/archive/refs/tags/v%{version}.tar.gz#%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l clang

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       clang

%description
This package provides Python bindings for the Clang C library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.TXT
%doc README.md

%changelog
%autochangelog
