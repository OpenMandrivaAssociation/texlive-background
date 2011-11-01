Name:		texlive-background
Version:	1.0
Release:	1
Summary:	Placement of background material on pages of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/background
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/background.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/background.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/background.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package offers the placement of background material on the
pages of a document. The user can control many aspects
(contents, position, color, opacity) of the background material
that will be displayed. The package makes use of the everypage
package, and uses pgf/tikz for attribute control.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
