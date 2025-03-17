%global build_cxxflags %{build_cxxflags} -std=gnu++20

Name:		mosh
Version:	1.4.0
Release:	3
Source0:	https://github.com/mobile-shell/mosh/releases/download/mosh-%{version}/mosh-%{version}.tar.gz
Summary:	Mobile shell that supports roaming and intelligent local echo
URL:		https://github.com/mobile-shell/mosh
License:	GPL-3.0
Group:		Applications/Internet
BuildSystem:	autotools
BuildOption:	--enable-compile-warnings=error
BuildRequires:	protobuf-compiler
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	utempter-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
Requires:	ssh
Requires:	perl(IO::Socket::IP)

%description
Mosh is a remote terminal application that supports:
  - intermittent network connectivity,
  - roaming to different IP address without dropping the connection, and
  - intelligent local echo and line editing to reduce the effects
    of "network lag" on high-latency connections.

%files
%{_bindir}/mosh*
%{_mandir}/man1/mosh*.1*
