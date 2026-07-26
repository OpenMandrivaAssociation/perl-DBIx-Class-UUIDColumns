%define upstream_name    DBIx-Class-UUIDColumns
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	0.02006
Release:	2

Summary:	Create uuids using Win32API::GUID
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.shadowcat.co.uk/gitweb/gitweb.cgi?p=dbsrgits/DBIx-Class-UUIDColumns.git
Source0:	https://cpan.metacpan.org/authors/id/A/AB/ABRAXXA/DBIx-Class-UUIDColumns-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(Data::UUID)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(Module::Find)

BuildArch: noarch

# Adding a requires or otherwise this module fails during run-time.
Requires:	perl(Data::UUID)

%description
This the DBIx::Class manpage component resembles the behaviour of the
Class::DBI::UUID manpage, to make some columns implicitly created as uuid.

When loaded, 'UUIDColumns' will search for a suitable uuid generation
module from the following list of supported modules:

  Data::UUID
  APR::UUID*
  UUID
  Win32::Guidgen
  Win32API::GUID

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.20.50-5mdv2011.0
+ Revision: 656900
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.50-4mdv2011.0
+ Revision: 625051
- Add a run-time Requires

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.50-3mdv2011.0
+ Revision: 624996
- Add Data::UUID as a build requires
- Add SQL::Abstract as a dep
- import perl-DBIx-Class-UUIDColumns

