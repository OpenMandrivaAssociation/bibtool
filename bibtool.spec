%define name    bibtool
%define Name    BibTool
%define version 2.48
%define release %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    A Tool for manipulating BibTeX data bases
Group:      Publishing
License:    GPL
Url:        http://www.ctan.org/tex-archive/biblio/bibtex/utils/bibtool
Source:     ftp://ctan.tug.org/tex-archive/biblio/bibtex/utils/bibtool/%{Name}-%{version}.tar.bz2
Patch0:         %{name}.configure.patch.bz2
Patch1:         %{name}.makefile.patch.bz2
Patch2:         %{name}-2.48.build.patch.bz2
Provides:       %{Name}
Obsoletes:      %{Name}
BuildRequires:  tetex-latex
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
BibTeX provides an easy to use means to integrate citations and
bibliographies into LaTeX documents. But the user is left alone with
the management of the BibTeX files. The program BibTool is intended to
fill this gap. BibTool allows the manipulation of BibTeX files which
goes beyond the possibilities --- and intentions --- of BibTeX.

%prep
%setup -q -n %{Name}-%{version}
%patch0
%patch1
%patch2

%build
%configure
%make
cd Doc
make all

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 bibtool %{buildroot}%{_bindir}
install -m 644 Lib/* %{buildroot}%{_datadir}/%{name}
install -m 644 Doc/bibtool.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc Changes.xml COPYING INSTALL README THANKS ToDo Doc/*.dvi
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

