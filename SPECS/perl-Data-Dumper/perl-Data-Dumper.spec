# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Data-Dumper
Version:        2.183
Release:        %autorelease
Summary:        Stringified perl data structures, suitable for both printing and eval
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Data-Dumper
#!RemoteAsset:  sha256:e42736890b7dae1b37818d9c5efa1f1fdc52dec04f446a33a4819bf1d4ab5ad3
Source0:        http://www.cpan.org/authors/id/N/NW/NWCLARK/Data-Dumper-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.

%prep
%setup -q -n Data-Dumper-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Todo

%changelog
%autochangelog
