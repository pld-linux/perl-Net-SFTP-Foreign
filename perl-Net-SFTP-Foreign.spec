#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	SFTP-Foreign
Summary:	Net::SFTP-Foreign - SSH File Transfer Protocol client
Name:		perl-Net-SFTP-Foreign
Version:	1.77
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd17242a0bf90206f3edf6ef051be873
URL:		http://search.cpan.org/dist/Net-SFTP-Foreign/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-SSH-Perl >= 1.24
%endif
Requires:	openssh-clients
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SFTP::Foreign is a Perl client for the SFTP version 3 as defined
in the SSH File Transfer Protocol IETF draft.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/SFTP/Foreign*.pm
%{perl_vendorlib}/%{pdir}/SFTP/Foreign
%{_mandir}/man3/*
