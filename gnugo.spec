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
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)

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
%apply_patches
autoconf

%build
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
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO 
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*.el
%{_gamesbindir}/*
%{_datadir}/emacs/site-lisp/*.el
%{_infodir}/*
%{_mandir}/man6/*

