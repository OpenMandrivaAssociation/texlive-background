Name:		texlive-background
Version:	42428
Release:	1
Summary:	Placement of background material on pages of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/background
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/background.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/background.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/background.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers the placement of background material on the
pages of a document. The user can control many aspects
(contents, position, color, opacity) of the background material
that will be displayed; all placement and attribute settings
are controlled by setting key values. The package makes use of
the everypage package, and uses pgf/tikz for attribute control.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/background/background.sty
%doc %{_texmfdistdir}/doc/latex/background/README
%doc %{_texmfdistdir}/doc/latex/background/background.pdf
#- source
%doc %{_texmfdistdir}/source/latex/background/background.dtx
%doc %{_texmfdistdir}/source/latex/background/background.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
