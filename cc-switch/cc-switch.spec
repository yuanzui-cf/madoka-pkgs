Name:           cc-switch
Version:        3.11.1
Release:        1%{?dist}
Summary:        Repackaging of cc-switch official rpm
License:        Unknown

Source0:        https://github.com/farion1231/cc-switch/releases/download/v%{version}/CC-Switch-%{version}-Linux-x86_64.rpm

%prep

%install
mkdir -p %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idmv -D %{buildroot}

%files
/*

%changelog
* Mon Mar 09 2026 Leo Jia <im.leojia@gmail.com> - 1.2.3-1
- Import official rpm into Madoka OS
