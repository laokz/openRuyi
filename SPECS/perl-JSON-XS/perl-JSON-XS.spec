# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-JSON-XS
Version:        4.04
Release:        %autorelease
Summary:        JSON serialising/deserialising, done correctly and fast
License:        CHECK(Distributable)
URL:            https://metacpan.org/dist/JSON-XS
#!RemoteAsset:  sha256:8eff1e9f304c5625b59ab7b42258415f6d3e3681c1ddab6b725518a018a7f5e0
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/JSON-XS-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(common::sense)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(Canary::Stability)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

%prep
%setup -q -n JSON-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
