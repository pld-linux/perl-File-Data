#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Data
Summary:	File::Data - interface to file data
Summary(pl.UTF-8):	File::Data - interfejs do danych w pliku
Name:		perl-File-Data
Version:	1.12
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	32c021844e4e803326eff40ebe7b2f57
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Data wraps all the accessing of a file into a convenient set of
calls for reading and writing data, including a simple regex interface.

The idea is to standardise accessing of files for repetitive and straight
forward tasks, and remove the repeated and therefore error prone file
access I have seen in many sites, where varying, (with equivalently
varying success), methods are used to achieve essentially the same result
- a simple search and replace and/or a regex match.

%description -l pl.UTF-8
File::Data owija dostęp do pliku w wygodny zbiór metod do czytania i
zapisywania danych, włączając w to prosty interfejs wyrażeń regularnych.

Pomysł polega na standaryzacji dostępu do plików w przypadku powtarzalnych
i prostych zadań, oraz usunięciu powtarzających się, czyli skłonnych
do błędów dostępów do plików spotykanych w wielu miejscach, gdzie
różne metody (z różnym skutkiem) używane są do osiągnięcia w zasadzie
tego samego rezultatu -- prostego wyszukiwania i zastępowania i/lub
dopasowania wzorca.

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
