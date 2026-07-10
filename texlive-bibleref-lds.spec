%global tl_name bibleref-lds
%global tl_revision 25526

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Bible references, including those to the scriptures of the Church of Jesus Ch...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-lds
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the bibleref-mouth package to support references to
the scriptures of The Church of Jesus Christ of Latter-day Saints (LDS).
The package requires bibleref-mouth to run, and its reference syntax is
the same as that of the parent package.

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
%dir %{_datadir}/texmf-dist/doc/latex/bibleref-lds
%dir %{_datadir}/texmf-dist/source/latex/bibleref-lds
%dir %{_datadir}/texmf-dist/tex/latex/bibleref-lds
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-lds/README
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-lds/bibleref-lds.pdf
%doc %{_datadir}/texmf-dist/source/latex/bibleref-lds/bibleref-lds.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibleref-lds/bibleref-lds.ins
%{_datadir}/texmf-dist/tex/latex/bibleref-lds/bibleref-lds.sty
