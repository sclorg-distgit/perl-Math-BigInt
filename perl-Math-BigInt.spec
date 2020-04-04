%{?scl:%scl_package perl-Math-BigInt}

# Run optional test
%if ! (0%{?scl:1})
%bcond_without perl_Math_BigInt_enables_optional_test
%else
%bcond_with perl_Math_BigInt_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Math-BigInt
Epoch:          1
%global cpan_version 1.999818
# Keep 4-digit version to compete with perl.spec
Version:        %(echo %{cpan_version} | sed 's/\(\.....\)/\1./')
Release:        3%{?dist}
Summary:        Arbitrary-size integer and float mathematics
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Math-BigInt
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# File::Spec not used on recent perl
BuildRequires:  %{?scl_prefix}perl(integer)
BuildRequires:  %{?scl_prefix}perl(Math::Complex) >= 1.39
BuildRequires:  %{?scl_prefix}perl(overload)
# Tests:
BuildRequires:  %{?scl_prefix}perl(base)
# Config::Tiny not used
BuildRequires:  %{?scl_prefix}perl(lib)
# Module::Signature not used
# Scalar::Util not used
# Socket not used
# Test::CPAN::Changes not used
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.94
# Optional tests:
# This core module must be buildable without non-core modules at bootstrap.
# Test::Pod 1.22 not used
# Test::Pod::Coverage 1.08 not used
# Test::Portability::Files not used
# Test::Whitespaces not used
# Pod::Coverage 0.18 not used
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Math::Complex) >= 1.39
Conflicts:      %{?scl_prefix}perl < 4:5.22.0-347

# Do not export unversioned module
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^%{?scl_prefix}perl\\(Math::BigInt\\)\\s*$

%description
This provides Perl modules for arbitrary-size integer and float mathematics.

%prep
%setup -q -n Math-BigInt-%{cpan_version}
%{?scl:scl enable %{scl} '}perl -MConfig -i -pe %{?scl:'"}'%{?scl:"'}s{^#!/usr/bin/perl}{$Config{startperl}}%{?scl:'"}'%{?scl:"'} examples/*.pl%{?scl:'}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
# NEW file is useless
%doc BUGS CHANGES CREDITS examples GOALS HISTORY README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Mar 26 2020 Petr Pisar <ppisar@redhat.com> - 1:1.9998.18-3
- Normalize the shebangs (bug #1817411)

* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.18-2
- SCL

* Mon Oct 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.18-1
- 1.999818 bump

* Mon Oct 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.17-1
- 1.999817 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.16-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.16-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Petr Pisar <ppisar@redhat.com> - 1:1.9998.16-1
- 1.999816 bump

* Tue Oct 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.15-1
- 1.999815 bump

* Fri Oct 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.14-1
- 1.999814 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.13-2
- Perl 5.28 rebuild

* Wed Apr 18 2018 Petr Pisar <ppisar@redhat.com> - 1:1.9998.13-1
- 1.999813 bump

* Wed Apr 18 2018 Petr Pisar <ppisar@redhat.com> - 1:1.9998.12-1
- 1.999812 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.11-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.11-2
- Perl 5.26 rebuild

* Fri Mar 17 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.11-1
- 1.999811 bump

* Thu Mar 02 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.10-1
- 1.999810 bump

* Mon Feb 13 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.09-1
- 1.999809 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9998.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Paul Howarth <paul@city-fan.org> - 1.9998.08-1
- 1.999808 bump

* Mon Jan 02 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.07-1
- 1.999807 bump

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9998.06-1
- 1.999806 bump

* Mon Dec 12 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.05-1
- 1.999805 bump

* Fri Dec 09 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.04-1
- 1.999804 bump

* Mon Dec 05 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.03-1
- 1.999803 bump

* Thu Dec 01 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.02-1
- 1.999802 bump

* Fri Nov 25 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.01-1
- 1.999801 bump

* Fri Nov 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.00-1
- 1.999800 bump

* Tue Nov 08 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.27-1
- 1.999727 bump

* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.26-1
- 1.999726 bump

* Mon Jun 20 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.24-1
- 1.999724 bump

* Wed Jun 15 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.23-1
- 1.999723 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9997.22-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9997.22-2
- Perl 5.24 rebuild

* Wed Apr 27 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.22-1
- 1.999722 bump

* Tue Apr 26 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.20-1
- 1.999720 bump

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.17-1
- 1.999717 bump

* Tue Apr 05 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.16-1
- 1.999716 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9997.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.15-1
- 1.999715 bump

* Mon Jan 04 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.14-1
- 1.999714 bump

* Mon Nov 16 2015 Petr Pisar <ppisar@redhat.com> - 1.9997.10-1
- 1.999710 bump

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.9997.09-1
- 1.999709 bump

* Thu Nov 05 2015 Petr Pisar <ppisar@redhat.com> - 1.9997.08-1
- 1.999708 bump

* Mon Nov 02 2015 Petr Pisar <ppisar@redhat.com> 1.9997.07-354
- Specfile autogenerated by cpanspec 1.78.
- Use bundled modules when bootstrapping
