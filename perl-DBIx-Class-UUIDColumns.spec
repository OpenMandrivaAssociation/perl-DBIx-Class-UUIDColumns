%define upstream_name    DBIx-Class-UUIDColumns
%define upstream_version 0.02005

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Create uuids using Win32API::GUID
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Grouped)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


