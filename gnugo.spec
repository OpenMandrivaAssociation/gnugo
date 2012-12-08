%define chinese_rules 0
%{?_with_chinese: %global chinese_rules 1}

Summary:	The GNU program to play the game of Go
Name:		gnugo
Version:	3.8
Release:	5
License:	GPLv3+ 
Group:		Games/Boards
Url:		http://www.gnu.org/software/gnugo/
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:		gnugo-3.8-fix-format-errors.patch
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel

%description
Go is a game of strategy between two players usually played on a 
19x19 grid called goban. GNU Go plays a game of Go against the 
user. It has many other features: it can play against itself or 
another program, analyse and score a recorded game. GNU Go is 
compliant with Go Modem Protocol, and load / save games in the
Smart Go format.
GNU Go uses a simple alpha-numeric board display by default. If you
want to use a graphical interface with GNU Go, you'll also need 
to install other GUI clients, such as CGoban or Jago.

Build Options:
--with chinese      Use Chinese rules for endgame counting

%prep
%setup -q
%patch0 -p 1 -b .format

%build
autoconf
%configure2_5x \
	--bindir=%{_gamesbindir}	\
	--enable-color			\
	--with-readline			\
%if %chinese_rules
	--enable-chinese-rules
%endif

%make
make check

%install
%makeinstall_std

# install emacs file
install -D -m 644 interface/gnugo.el %{buildroot}%{_datadir}/emacs/site-lisp/gnugo.el
mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
echo "(autoload 'gnugo \"gnugo\" \"GNU Go\" t)" > %{buildroot}%{_sysconfdir}/emacs/site-start.d/gnugo.el

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO 
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*.el
%{_infodir}/*
%{_gamesbindir}/*
%{_mandir}/man6/*
%{_datadir}/emacs/site-lisp/*.el


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.8-3mdv2011.0
+ Revision: 664897
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.8-2mdv2011.0
+ Revision: 605489
- rebuild

* Sun Nov 29 2009 Jérôme Brenier <incubusss@mandriva.org> 3.8-1mdv2010.1
+ Revision: 471013
- new version 3.8
- drop readline patch (merged upstream)
- rediff str fmt patch
- fix license tag

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 3.6-9mdv2010.0
+ Revision: 437791
- rebuild

* Fri Feb 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.6-8mdv2009.1
+ Revision: 345792
- rebuild for latest readline
- fix format errors

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 3.6-7mdv2009.0
+ Revision: 240792
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 3.6-5mdv2008.0
+ Revision: 70288
+ rebuild (emptylog)

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 3.6-4mdv2008.0
+ Revision: 67950
- convert prereq & unregister info page before uninstalling

  + Funda Wang <fwang@mandriva.org>
    - Import gnugo




* Sat Jun 17 2006 Warly <warly@mandriva.com> 3.6-3mdv2007.0
- use mkrel

* Sat Jan 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.6-2mdk
- rebuild for new readline

* Sat Nov 20 2004 Abel Cheung <deaddog@mandrake.org> 3.6-1mdk
- New version
- Patch0: readline support (from website, slightly modified)
- Nice frontends for gnugo do exist, we shouldn't need menu entry now
- Install gnugo emacs mode

* Mon Oct 25 2004 Michael Scherer <misc@mandrake.org> 3.4-7mdk
- Rebuild

* Tue Sep 16 2003 Abel Cheung <deaddog@deaddog.org> 3.4-6mdk
- Fix menu typo
- Avoid turn on pattern reading option, it's dumping too much debug output

* Tue Sep 16 2003 Abel Cheung <deaddog@deaddog.org> 3.4-5mdk
- Fix menu section, it fits into board game better than strategy game
- Add missing buildrequires
- Why make html doc if it's not bundled?
- make check
- Optionally allow experimental build options

* Sun Sep 14 2003 Pascal Terjan <Cmoi@tuxfamily.org> 3.4-4mdk
- Buildrequires autoconf2.5 is the solution

* Wed Sep 10 2003 Pascal Terjan <Cmoi@tuxfamily.org> 3.4-3mdk
- this time is the right one for autoconf 2.5 :)

* Sun Sep 07 2003 Pascal Terjan <Cmoi@tuxfamily.org> 3.4-2mdk
- really use autoconf >= 2.5

* Sun Aug 31 2003 Pascal Terjan <Cmoi@tuxfamily.org> 3.4-1mdk
- 3.4
- Drop patch 

* Sun Aug 31 2003 Michael Scherer <scherer.michael@free.fr> 3.2-5mdk 
- really use autoconf >= 2.5

* Sat Aug 30 2003 Michael Scherer <scherer.michael@free.fr> 3.2-4mdk 
- BuildRequires autoconf >=2.5

* Sun Aug 24 2003 Michael Scherer <scherer.michael@free.fr> 3.2-3mdk
- fix compile ( patch #0 )
- menu macro
 
* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.2-2mdk
- buildrequires

* Fri May 10 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.2-1mdk
- 3.2

* Wed Dec 26 2001 David BAUDENS <baudens@mandrakesoft.com> 3.0.0-2mdk
- Use default strategy icon for menu entry
- Allow application to be launched from menu entry
- Fix %%post and %%postun

* Tue Aug 28 2001 Yves Bailly <ybailly@mandrakesoft.com> 3.0.0-1mdk
- upgrade to 3.0.0, 4 stones stronger than 2.6
- now uses ncurses for text play

* Thu May 31 2001 Yves Bailly <ybailly@mandrakesoft.com> 2.7.238-2mdk
- fix spec file (post-install-infos)

* Tue May 29 2001 Yves Bailly <ybailly@mandrakesoft.com> 2.7.238-1mdk
- last release

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.6-4mdk
- rebuild

* Fri Sep 01 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.6-3mdk
- macros
- BM
- menu

* Thu Apr 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.6-2mdk
- fix group

* Mon Apr  4 2000 Jerome Dumonteil <jd@mandrakesoft.com>
- upgrade to 2.6
- new doc
- fix group

* Wed Dec 29 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- small changes in description

* Thu Dec 23 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- first mandrake rpm
- patch for known bugs of 2.4
