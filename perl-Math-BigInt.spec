%{?scl:%scl_package perl-Math-BigInt}

Name:           %{?scl_prefix}perl-Math-BigInt
%global cpan_version 1.999726
# Keep 4-digit version to compete with perl.spec
Version:        %(echo %{cpan_version} | sed 's/\(\.....\)/\1./')
Release:        2%{?dist}
Summary:        Arbitrary-size integer and float mathematics
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-BigInt/
Source0:        http://www.cpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
# This core module must be buildable without non-core modules at bootstrap.
%if %{defined perl_bootstrap} || %{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# ExtUtils::Manifest not used
# ExtUtils::MM_Cygwin not used
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MM_Unix)
# ExtUtils::MM_Win32 not used
BuildRequires:  %{?scl_prefix}perl(Fcntl)
# File::Basename not used
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
# File::Spec not used
# File::Temp not used
# FileHandle not used
BuildRequires:  %{?scl_prefix}perl(FindBin)
# JSON not used
# LWP::Simple not used
# Module::Build not used
# Net::FTP not used
# Parse::CPAN::Meta not used
# Socket not used
BuildRequires:  %{?scl_prefix}perl(vars)
# YAML::Tiny not used
%else
BuildRequires:  %{?scl_prefix}perl(inc::Module::Install)
BuildRequires:  %{?scl_prefix}perl(Module::Install::Metadata)
BuildRequires:  %{?scl_prefix}perl(Module::Install::WriteAll)
%endif
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# File::Spec not used on recent perl
BuildRequires:  %{?scl_prefix}perl(integer)
BuildRequires:  %{?scl_prefix}perl(Math::Complex) >= 1.39
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(lib)
# Module::Signature not used
# Scalar::Util not used
# Socket not used
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.9301
# Optional tests:
# This core module must be buildable without non-core modules at bootstrap.
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.22
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  %{?scl_prefix}perl(Pod::Coverage) >= 0.18
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Math::Complex) >= 1.39
Conflicts:      %{?scl_prefix}perl < 4:5.22.0-347

# Do not export unversioned module
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_provides /^%{?scl_prefix}perl(Math::BigInt)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^%{?scl_prefix}perl\\(Math::BigInt\\)\\s*$
%endif

%description
This provides Perl modules for arbitrary-size integer and float mathematics.

%prep
%setup -q -n Math-BigInt-%{cpan_version}
# This core module must be buildable without non-core modules at bootstrap.
%if !%{defined perl_bootstrap} && !%{defined perl_small}
# Remove bundled modules
rm -r inc
sed -i -e '/^inc\//d' MANIFEST
%endif
# Correct permissions
find . -type f -exec chmod -x {} +

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
# NEW file is useless
%doc BENCHMARK BUGS examples CHANGES CREDITS GOALS HISTORY README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.26-2
- SCL

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
