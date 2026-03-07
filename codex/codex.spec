Name:           codex
Version:        0.111.0
Release:        1%{?dist}
Summary:        OpenAI Codex CLI tool (Rust version)
License:        MIT
URL:            https://github.com/openai/codex

BuildRequires:  systemd-rpm-macros

Source0:        https://github.com/openai/codex/releases/download/rust-v%{version}/codex-x86_64-unknown-linux-gnu.tar.gz

%description
A CLI tool for interacting with OpenAI Codex, written in Rust.

%prep
%autosetup -c -n %{name}-%{version}

%build
chmod +x codex

%install
install -D -m 755 codex %{buildroot}%{_bindir}/codex

%files
%{_bindir}/codex

%changelog
* Sat Mar 07 2026 Leo Jia <im.leojia@gmail.com> - 0.111.0-1
- Update to v0.111.0
