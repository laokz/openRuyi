# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kai Zhang <zhangkai@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lssbi
Version:        0.0.0
Release:        %autorelease
Summary:        List information about the active RISC-V SBI environment.
License:        GPL-2.0 OR MIT OR MulanPSL-2.0
URL:            https://github.com/rustsbi/lssbi
#!RemoteAsset:  sha256:cdc193927e591c07b6587cfbb58ec530dcf80097f265c37724d21f7cf8373831
Source:         https://github.com/rustsbi/lssbi/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  crate(clap-4/cargo) >= 4.5.0
BuildRequires:  crate(clap-4/derive) >= 4.5.0
BuildRequires:  crate(clap-4/help) >= 4.5.0
BuildRequires:  crate(clap-4/std) >= 4.5.0
BuildRequires:  crate(clap-4/usage) >= 4.5.0
BuildRequires:  crate(gettext-rs-0.8/default) >= 0.8.0
BuildRequires:  crate(gettext-rs-0.8/gettext-system) >= 0.8.0
BuildRequires:  crate(jep106-0.3) >= 0.3.0
BuildRequires:  crate(polib-0.3) >= 0.3.0
BuildRequires:  crate(sbi-spec-0.0.9/default) >= 0.0.9
BuildRequires:  crate(unicode-width-0.2/default) >= 0.2.0
BuildRequires:  linux-devel
BuildRequires:  dkms

%description
List information about the active RISC-V SBI environment.
The current backend reads values exported by the lssbi_probe
DKMS module. The command itself is unprivileged and never
loads or unloads kernel modules.

%install
PREFIX=%{prefix} PROFILE=release DESTDIR=%{buildroot} ./install.sh

%files
%doc README.md
%license LICENSE
%{_bindir}/agg

%changelog
%autochangelog
