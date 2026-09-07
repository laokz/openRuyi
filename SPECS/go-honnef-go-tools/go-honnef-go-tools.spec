# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tools
%define go_import_path  honnef.co/go/tools

Name:           go-honnef-go-tools
Version:        0.8.1
Release:        %autorelease
Summary:        Staticcheck tools for Go
License:        MIT
URL:            https://github.com/dominikh/go-tools
#!RemoteAsset:  sha256:7f16b3c7450f7ab62791dfb2e6d40d57d3b74dd01eef30f24a71822db8d45848
Source0:        https://github.com/dominikh/go-tools/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet reports fmt.Sprintf %q with an int64 argument in
# staticcheck/sa1030; keep tests enabled but disable vet. - HNO3Miracle
#####################################BuildOption(check):  -vet=off

BuildRequires:  go >= 1.26.0
BuildRequires:  go(github.com/BurntSushi/toml) >= 1.4.1
BuildRequires:  go(github.com/google/go-cmp) >= 0.7.0
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod) >= 0.35.0
BuildRequires:  go(golang.org/x/sync) >= 0.20.0
BuildRequires:  go(golang.org/x/tools) >= 0.44.1
BuildRequires:  go-golang-x-tools-go-expect >= 0.1.1
BuildRequires:  go-rpm-macros

Provides:       go(honnef.co/go/tools) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/google/go-cmp)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)

%description
This package provides Staticcheck tools and supporting libraries for Go.

%files
%doc README.md
%license LICENSE
%license LICENSE-THIRD-PARTY
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
