%define oname BibTool

Summary:	A Tool for manipulating BibTeX data bases
Name:		bibtool
Version:	2.55
Release:	1
License:	GPLv1+
Group:		Publishing
Url:		http://www.ctan.org/tex-archive/biblio/bibtex/utils/bibtool
Source0:	ftp://ctan.tug.org/tex-archive/biblio/bibtex/utils/bibtool/%{oname}-%{version}.tar.gz
Patch0:		BibTool-2.51-regex.patch
BuildRequires:	texlive

%description
BibTeX provides an easy to use means to integrate citations and
bibliographies into LaTeX documents. But the user is left alone with
the management of the BibTeX files. The program BibTool is intended to
fill this gap. BibTool allows the manipulation of BibTeX files which
goes beyond the possibilities --- and intentions --- of BibTeX.

%files
%doc COPYING README THANKS ToDo
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}
%patch0 -p1 -b .regex
sed -i -e 's%^#!/usr/local/bin/tclsh%#! %{_bindir}/tclsh%' Tcl/bibtool.tcl
sed -i -e 's%^#!/usr/local/bin/perl%#! %{_bindir}/perl%' Perl/bibtool.pl
# configure will recreate the directory, but only with config.h within
rm -rf regex-0.12

%build
%configure2_5x
sed -i -e 's#@kpathsea_lib_static@##' makefile
%make
cd Doc
make all

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 bibtool %{buildroot}%{_bindir}
install -m 644 Lib/* %{buildroot}%{_datadir}/%{name}
install -m 644 Doc/bibtool.1 %{buildroot}%{_mandir}/man1

