Name:           mihomo
Version:        1.19.20
Release:        1%{?dist}
Summary:        Mihomo (Clash Meta) Prebuilt Binary for Madoka OS

License:        GPLv3
URL:            https://github.com/MetaCubeX/mihomo

BuildRequires:  systemd-rpm-macros

Source0:        https://github.com/MetaCubeX/mihomo/releases/download/v%{version}/mihomo-linux-amd64-v%{version}.gz
Source1:        mihomo.service

%description
A rule-based tunnel in Go, packaged for the Madoka OS project.

%prep
gunzip -c %{SOURCE0} > mihomo

%build
chmod +x mihomo

%install
install -p -D -m 755 mihomo %{buildroot}%{_bindir}/mihomo

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/mihomo.service

mkdir -p %{buildroot}%{_sysconfdir}/mihomo

%files
%{_bindir}/mihomo
%{_unitdir}/mihomo.service
%dir %{_sysconfdir}/mihomo

%changelog
* Sat Mar 07 2026 Leo Jia <im.leojia@gmail.com> - 1.19.20-1
- Fix %{_unitdir} macro issue for Fedora 43
- Add systemd-rpm-macros to BuildRequires
