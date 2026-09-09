# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ansible-core
%global pypi_name ansible_core

Name:           python-%{srcname}
Version:        2.21.4
Release:        %autorelease
Summary:        Radically simple IT automation
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT AND PSF-2.0
URL:            https://github.com/ansible/ansible
#!RemoteAsset:  sha256:81a9329f4f12cfa5008dcab5d1bf23ae69b7effc08c0f00048ab2461147ae95a
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ansible ansible_test

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(resolvelib)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Ansible is a radically simple IT automation system. It handles configuration
management, application deployment, cloud provisioning, ad-hoc task execution,
network automation, and multi-node orchestration.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc changelogs/CHANGELOG-*.rst
%doc README.md
%license COPYING
%license licenses/*.txt
%{_bindir}/ansible
%{_bindir}/ansible-*

%changelog
%autochangelog
