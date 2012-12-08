Summary: 	A utility which provides statistics based on the output of diff
Name: 		diffstat
Version: 	1.54
Release: 	%mkrel 5
Group: 		Development/Other
License: 	GPL-like
URL: 		http://dickey.his.com/diffstat/diffstat.html
Source: 	ftp://invisible-island.net/diffstat/%name-%version.tgz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
The diff command compares files line by line.  Diffstat reads the output
of the diff command and displays a histogram of the insertions, deletions
and modifications in each file.  Diffstat is commonly used to provide
a summary of the changes in large, complex patch files.

Install diffstat if you need a program which provides a summary of the
diff command's output.  You'll need to also install diffutils.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES
%{_bindir}/diffstat
%{_mandir}/man1/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.54-4mdv2011.0
+ Revision: 663775
- mass rebuild

* Tue Nov 23 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.54-3mdv2011.0
+ Revision: 600265
- New version 1.54.

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.53-3mdv2011.0
+ Revision: 564251
- rebuild
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 1.53-1mdv2011.0
+ Revision: 555536
- New version 1.53

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.51-1mdv2010.1
+ Revision: 462836
- update to new version 1.51

* Tue Sep 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.49-1mdv2010.0
+ Revision: 423677
- update to new version 1.49

* Wed Aug 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.48-1mdv2010.0
+ Revision: 415655
- update to new version 1.48

* Tue May 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1.47-1mdv2010.0
+ Revision: 372233
- update to new version 1.47

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.46-2mdv2009.1
+ Revision: 350788
- rebuild

* Thu Sep 04 2008 Thierry Vignaud <tv@mandriva.org> 1.46-1mdv2009.0
+ Revision: 280827
- new release

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.45-3mdv2009.0
+ Revision: 220624
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.45-2mdv2008.1
+ Revision: 149181
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 1.45-1mdv2008.0
+ Revision: 80157
- new release

* Fri Jun 22 2007 Adam Williamson <awilliamson@mandriva.org> 1.43-2mdv2008.0
+ Revision: 42848
- rebuild for 2008
- Import diffstat



* Tue Jul 18 2006 Erwan Velu <erwan@mandriva.org> 1.43-1mdv2007.0
- 1.43

* Sun Jul 16 2006 Emmanuel Andry <eandry@mandriva.org> 1.42-1mdv2007.0
- new release

* Sun May 14 2006 Stefan van der Eijk <stefan@eijk.nu> 1.41-2mdk
- rebuild for sparc

* Thu Nov 03 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.41-1mdk
- new release

* Fri May 13 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.39-1mdk
- new release

* Fri Feb 11 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.38-1mdk
- new release

* Thu Nov 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.35-1mdk
- new release

* Thu Dec 11 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.34-1mdk
- new release

* Wed Jul 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.33-1mdk
- new release

* Mon Jan 06 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.32-1mdk
- new release

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.31-2mdk
- build release

* Thu Oct 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.31-1mdk
- new release
- fix source url

* Tue Nov 13 2001 Yves Duret <yduret@mandrakesoft.com> 1.28-3mdk
- spec clean up, macros, rebuild

* Mon Jul 16 2001 Yves Duret <yduret@mandrakesoft.com> 1.28-2mdk
- rebuild
- spec clean up

* Mon Dec 25 2000 Yves Duret <yduret@mandrakesoft.com> 1.28-1mdk
- new and shiny version 1.28
- macros
- added URL tag, fixed Source: tag
- added doc

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.27-12mdk
- BM, macros, spec-helper

* Thu Apr 4 2000 Denis Havlik <denis@mandrakesoft.com> 1.27-11mdk
- New group: Development/Other

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Sun Jul 18 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 1.27

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
