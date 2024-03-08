# Run tests in check section
%bcond_without check

# http://github.com/davecgh/go-spew
%global goipath		github.com/davecgh/go-spew
%global forgeurl	https://github.com/davecgh/go-spew
Version:		1.1.1

%gometa

Summary:	A deep pretty printer for Go data structures to aid in debugging
Name:		golang-github-davecgh-go-spew

Release:	1
Source0:	https://github.com/davecgh/go-spew/archive/v%{version}/go-spew-%{version}.tar.gz
URL:		https://github.com/davecgh/go-spew
License:	ISC
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Go-spew implements a deep pretty printer for Go data structures to aid in
debugging.  A comprehensive suite of tests with 100% test coverage is
provided to ensure proper functionality.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-spew-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

