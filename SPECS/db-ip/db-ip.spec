# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version 2026-09

Name:           db-ip
Version:        2026.09
Release:        %autorelease
Summary:        DB-IP City Lite Database
License:        CC-BY-4.0
URL:            https://db-ip.com/
#!RemoteAsset:  sha256:c5d05b35a45c3eea0cadc728c8f5ad751693d4e270529b731442172a73f05954
Source0:        https://download.db-ip.com/free/dbip-city-lite-%{upstream_version}.mmdb.gz
#!RemoteAsset:  sha256:25f5c2e9b98d1a479567e654927c6b34867aaadc96a01ee25d5790c478685ab5
Source1:        https://download.db-ip.com/free/dbip-asn-lite-%{upstream_version}.mmdb.gz
#!RemoteAsset:  sha256:9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411
Source2:        https://creativecommons.org/licenses/by/4.0/legalcode.txt
BuildArch:      noarch

%description
This package contains the free DB-IP City Lite database in MMDB format.
It provides IPv4 and IPv6 routing data with city-level geolocation.
This data is updated monthly by DB-IP.

%prep
%setup -c -T
gunzip -c %{SOURCE0} > dbip-city-lite.mmdb
gunzip -c %{SOURCE1} > dbip-asn-lite.mmdb
cp %{SOURCE2} LICENSE

%install
mkdir -p %{buildroot}%{_datadir}/db-ip
install -p -m 0644 dbip-city-lite.mmdb %{buildroot}%{_datadir}/db-ip/
install -p -m 0644 dbip-asn-lite.mmdb %{buildroot}%{_datadir}/db-ip/

%files
%license LICENSE
%dir %{_datadir}/db-ip
%{_datadir}/db-ip/dbip-city-lite.mmdb
%{_datadir}/db-ip/dbip-asn-lite.mmdb

%changelog
%autochangelog
