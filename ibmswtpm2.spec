Summary:	IBM's Software TPM 2.0
Summary(pl.UTF-8):	Programowy TPM 2.0 stworzony przez IBM
Name:		ibmswtpm2
Version:	1682
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://downloads.sourceforge.net/ibmswtpm2/ibmtpm%{version}.tar.gz
# Source0-md5:	d929acc296cf2eb2dd481bc97fe42fa9
URL:		https://sourceforge.net/projects/ibmswtpm2/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is an implementation of the TCG TPM 2.0 specification. It
is based on the TPM specification Parts 3 and 4 source code donated by
Microsoft, with additional files to complete the implementation.

%description -l pl.UTF-8
Ten projekt jest implementacją specyfikacji TCG TPM 2.0. Jest oparty
na kodzie źródłowym części 3 i 4 specyfikacji TPM udostępnionym przez
Microsoft z dodatkowymi plikami dopełniającymi implementację.

%prep
%setup -q -c

%build
%{__make} -C src \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Werror -Wsign-compare -Wno-uninitialized -Wno-error=deprecated-declarations -DTPM_POSIX -D_POSIX_ -DTPM_NUVOTON -I. -c" \
	LNFLAGS="%{rpmldflags} %{rpmcflags} -lcrypto -lpthread -lrt"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE ibmtpm.doc
%attr(755,root,root) %{_bindir}/tpm_server
