Name:		texlive-bibleref-lds
Version:	25526
Release:	1
Summary:	Bible references, including Church of Jesus Christ of Latter Day Saints
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-lds
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.r25526.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.doc.r25526.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.source.r25526.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the bibleref-mouth package to support
references to the scriptures of The Church of Jesus Christ of
Latter-day Saints (LDS). The package requires bibleref-mouth to
run, and its reference syntax is the same as that of the parent
package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-lds/bibleref-lds.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-lds/README
%doc %{_texmfdistdir}/doc/latex/bibleref-lds/bibleref-lds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bibleref-lds/bibleref-lds.dtx
%doc %{_texmfdistdir}/source/latex/bibleref-lds/bibleref-lds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
