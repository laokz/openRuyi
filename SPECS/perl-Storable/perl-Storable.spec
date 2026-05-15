# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Storable
Version:        3.25
Release:        %autorelease
Summary:        Persistence for Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Storable
#!RemoteAsset:  sha256:e1e96b24a076792fde52154789fe4b76034b9ad39c8a1a819ead77d50d5f1817
Source0:        http://www.cpan.org/authors/id/N/NW/NWCLARK/Storable-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.41
BuildRequires:  perl(XSLoader)

%description
The Storable package brings persistence to your Perl data structures
containing SCALAR, ARRAY, HASH or REF objects, i.e. anything that can be
conveniently stored to disk and retrieved at a later time.

%prep
%setup -q -n Storable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README stacksize

%changelog
%autochangelog
