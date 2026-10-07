Name:           oosleep
Version:        0.1.0
Release:        1%{?dist}
Summary:        High-precision timer sleep supporting nanosecond resolution and monotonic clock loops.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosleep
Source0:        oosleep-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosleep is a sovereign, capability-bounded PRECISE PAUSE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosleep
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosleep-uninstall

%files
/usr/bin/oosleep
/usr/bin/oosleep-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
