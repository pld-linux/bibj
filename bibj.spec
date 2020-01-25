Summary:	Extracts journals names
Summary(pl.UTF-8):	Wyciąganie nazw czasopism
Name:		bibj
Version:	1.1
Release:	1
License:	unknown
Group:		Applications
Source0:	http://www.ecst.csuchico.edu/~jacobsd/bib/archives/%{name}
# Source0-md5:	711d05f757f91023e3822d73ff05e414
URL:		http://www.ecst.csuchico.edu/~jacobsd/bib/tools/bibtex.html
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extracts journals names, which can be used to check for misspellings
and duplicates.

%description -l pl.UTF-8
bibj wyciąga nazwy czasopism, co można wykorzystać do sprawdzania
pisowni i wyszukiwania duplikatów.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
sed -i -e 's#/usr/local/bin/perl#/usr/bin/perl#' $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
