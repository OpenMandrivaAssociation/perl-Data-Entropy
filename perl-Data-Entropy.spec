%define upstream_name    Data-Entropy
%define upstream_version 0.007

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Download entropy from
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Data::Float)
BuildRequires: perl(Errno)
BuildRequires: perl(Exporter)
Buildrequires: perl(HTTP::Lite)
BuildRequires: perl(IO::File)
BuildRequires: perl(LWP)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Params::Classify)
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(integer)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch

%description
This module maintains a concept of a current selection of entropy source.
Algorithms that require entropy, such as those in the
Data::Entropy::Algorithms manpage, can use the source nominated by this
module, avoiding the need for entropy source objects to be explicitly
passed around. This is convenient because usually one entropy source will
be used for an entire program run and so an explicit entropy source
parameter would rarely vary. There is also a default entropy source,
avoiding the need to explicitly configure a source at all.

If nothing is done to set a source then it defaults to the use of Rijndael
(AES) in counter mode (see the Data::Entropy::RawSource::CryptCounter
manpage and the Crypt::Rijndael manpage), keyed using Perl's built-in
'rand' function. This gives a data stream that looks like concentrated
entropy, but really only has at most the entropy of the 'rand' seed. Within
a single run it is cryptographically difficult to detect the correlation
between parts of the pseudo-entropy stream. If more true entropy is
required then it is necessary to configure a different entropy source.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sat May 07 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 672165
- new version 0.007
- clean spec
- update Source0
- add a BR on HTTP::Lite

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.6.0-2
+ Revision: 653561
- rebuild for updated spec-helper

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 573814
- import perl-Data-Entropy

