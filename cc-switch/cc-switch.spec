Name:           cc-switch
Version:        3.12.0
Release:        1%{?dist}
Summary:        Repackaging of cc-switch official rpm
License:        Unknown

Source0:        https://github.com/farion1231/cc-switch/releases/download/v%{version}/CC-Switch-v%{version}-Linux-x86_64.rpm

%description
Repackaging of cc-switch official rpm

%prep

%install
mkdir -p %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idmv -D %{buildroot}

%files
%{_bindir}/cc-switch
"%{_datadir}/applications/CC Switch.desktop"
%{_datadir}/icons/hicolor/*/apps/cc-switch.*

%changelog
* Thu Mar 11 2026 Leo Jia <im.leojia@gmail.com> - 3.12.0-1
- Update to 3.12.0
