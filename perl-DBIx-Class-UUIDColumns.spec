%define upstream_name    DBIx-Class-UUIDColumns
%define upstream_version 0.02005

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Create uuids using Win32API::GUID
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

