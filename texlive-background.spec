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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers the placement of background material on the pages of
a document. The user can control many aspects (contents, position,
color, opacity) of the background material that will be displayed; all
placement and attribute settings are controlled by setting key values.
The package makes use of the everypage package, and uses pgf/tikz for
attribute control.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/background
%dir %{_datadir}/texmf-dist/source/latex/background
%dir %{_datadir}/texmf-dist/tex/latex/background
%doc %{_datadir}/texmf-dist/doc/latex/background/README
%doc %{_datadir}/texmf-dist/doc/latex/background/background.pdf
%doc %{_datadir}/texmf-dist/source/latex/background/background.dtx
%doc %{_datadir}/texmf-dist/source/latex/background/background.ins
%{_datadir}/texmf-dist/tex/latex/background/background.sty
