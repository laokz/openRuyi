# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Devel-Caller
Version:        2.07
Release:        %autorelease
Summary:        Meatier versions of caller
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-Caller
#!RemoteAsset:  sha256:b679a2b18034b0b720de82c3708724c364b10a6ca164cbc67cdc3af283f3503f
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PadWalker) >= 0.08
BuildRequires:  perl(Test::More)

Requires:       perl(PadWalker) >= 0.08

%description
caller_cv($level)

%prep
%setup -q -n Devel-Caller-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
