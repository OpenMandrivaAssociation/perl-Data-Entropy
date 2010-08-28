%define upstream_name    Data-Entropy
%define upstream_version 0.006

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Download entropy from
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires: perl(Carp)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Data::Float)
BuildRequires: perl(Errno)
BuildRequires: perl(Exporter)
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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


