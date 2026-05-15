# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Readonly-XS
Version:        1.05
Release:        %autorelease
Summary:        Companion module for Readonly.pm, to speed up read-only scalar variables
License:        CHECK(GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/Readonly-XS
#!RemoteAsset:  sha256:8ae5c4e85299e5c8bddd1b196f2eea38f00709e0dc0cb60454dc9114ae3fff0d
Source0:        http://www.cpan.org/authors/id/R/RO/ROODE/Readonly-XS-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Readonly) >= 1.02

Requires:       perl(Readonly) >= 1.02

%description
The Readonly module (q.v.) is an effective way to create non-modifiable
variables. However, it's relatively slow.

%prep
%setup -q -n Readonly-XS-%{version}

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
