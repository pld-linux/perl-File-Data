#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Data
Summary:	File::Data - interface to file data
Summary(pl):	File::Data - interfejs do danych w pliku
Name:		perl-File-Data
Version:	1.12
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%description -l pl
File::Data owija dostêp do pliku w wygodny zbiór metod do czytania i
zapisywania danych, w³±czaj±c w to prosty interfejs wyra¿eñ regularnych.

Pomys³ polega na standaryzacji dostêpu do plików w przypadku powtarzalnych
i prostych zadañ, oraz usuniêciu powtarzaj±cych siê, czyli sk³onnych
do b³êdów dostêpów do plików spotykanych w wielu miejscach, gdzie
ró¿ne metody (z ró¿nym skutkiem) u¿ywane s± do osi±gniêcia w zasadzie
tego samego rezultatu -- prostego wyszukiwania i zastêpowania i/lub
dopasowania wzorca.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
