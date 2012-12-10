%define name    bibtool
%define Name    BibTool
%define version 2.48
%define release %mkrel 7

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.48-7mdv2011.0
+ Revision: 616753
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.48-6mdv2010.0
+ Revision: 424618
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.48-5mdv2009.0
+ Revision: 243255
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.48-3mdv2008.1
+ Revision: 122379
- kill re-definition of %%buildroot on Pixel's request
- import bibtool


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.48-3mdv2007.0
- %%mkrel

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.48-2mdk 
- spec cleanup

* Mon Jul 19 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.48-1mdk 
- new version
- rpmbuildupdate aware

* Tue Sep 23 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.47-2mdk
- changed name to bibtool, mixed cases sucks
- mdk optimisations

* Tue May 06 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.47-1mdk
- 2.47
- data files in %%{_datadir}/%%{name}

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.46-2mdk
- rebuild

* Fri Dec 13 2002  Lenny Cartier <lenny@mandrakesoft.com> 2.46-1mdk
- updated (noticed by Patrice Dumas)

* Mon Sep 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.44-1mdk
- added in contribs by Guillaume Rousse <g.rousse@linux-mandrake.com> :
    - first mdk release
