Name:           mihomo
Version:        1.19.20
Release:        1%{?dist}
Summary:        Mihomo (Clash Meta) Binary
License:        GPLv3
URL:            https://github.com/MetaCubeX/mihomo

Source0:        https://github.com/MetaCubeX/mihomo/releases/download/v%{version}/mihomo-linux-amd64-v%{version}.gz
Source1:        mihomo.service

%description
A rule-based tunnel in Go.

%prep
gunzip -c %{SOURCE0} > mihomo

%build

%install
install -p -D -m 755 mihomo %{buildroot}%{_bindir}/mihomo

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/mihomo.service

mkdir -p %{buildroot}%{_sysconfdir}/mihomo

%files
%{_bindir}/mihomo
%{_unitdir}/mihomo.service
%dir %{_sysconfdir}/mihomo

%changelog
* Sat Mar 07 2026 Leo Jia <im.leojia@gmail.com> - 1.19.20-1
- Update to 1.19.20
