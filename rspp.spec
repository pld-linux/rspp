Summary:	RPM Spec Pre Processor
Summary(pl):	Preprocessor dla specy
Name:		rspp
Version:	0.0.1
Release:	1
License:	Academic Free License v1.2
Group:		Development/Building
Vendor:		Michal Moskal <malekith@pld-linux.org>
Source0:	ftp://ftp.pld-linux.org/people/malekith/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0ac495bc04adb0ae157fcc434c292e0a
URL:		http://www.kernel.pl/~malekith/
BuildRequires:	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple tool that process rpm macros and spec files. It can either
output preprocessed spec or evaluate specific macro. It doesn't handle
some more bizarre rpm syntax. It is aimed as help with automatic spec
processing (like looking for list of BuildRequires and so on).

%description -l pl
Proste narzêdzie do przetwarzania plików z makrami rpm i specy. Mo¿e
wy¶wietliæ przetworzony spec, lub rozwiniêt± warto¶æ makra. Nie
obs³uguje co dziwniejszej sk³adni rpm. Celem tego narzêdzia jest
automatyczne przetwarzanie specy (np. szukanie listy pakietów
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
