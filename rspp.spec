Summary:	RPM Spec Pre Processor
Summary(pl.UTF-8):	Preprocessor dla plików .spec
Name:		rspp
Version:	0.0.2
Release:	1
License:	Academic Free License v2.0
Group:		Development/Building
Vendor:		Michal Moskal <malekith@pld-linux.org>
Source0:	ftp://ftp.pld-linux.org/people/malekith/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7784d8af6c2f07867643e9ffebabe1fe
URL:		http://ep09.pld-linux.org/~malekith/
BuildRequires:	ocaml >= 3.06
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple tool that process RPM macros and spec files. It can either
output preprocessed spec or evaluate specific macro. It doesn't handle
some more bizarre RPM syntax. It is aimed as help with automatic spec
processing (like looking for list of BuildRequires and so on).

%description -l pl.UTF-8
Proste narzędzie do przetwarzania plików z makrami RPM i plików .spec.
Może wyświetlić przetworzony spec, lub rozwiniętą wartość makra. Nie
obsługuje co dziwniejszej składni RPM. Celem tego narzędzia jest
automatyczne przetwarzanie plików .spec (np. szukanie listy pakietów
wymaganych do budowania).

%prep
%setup -q

%build
%{__make} opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install rspp.opt $RPM_BUILD_ROOT%{_bindir}/rspp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README COPYING
%attr(755,root,root) %{_bindir}/*
