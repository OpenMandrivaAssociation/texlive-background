%global tl_name background
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Placement of background material on pages of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/background
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/background.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/background.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/background.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers the placement of background material on the pages of
a document. The user can control many aspects (contents, position,
color, opacity) of the background material that will be displayed; all
placement and attribute settings are controlled by setting key values.
The package makes use of the everypage package, and uses pgf/tikz for
attribute control.

