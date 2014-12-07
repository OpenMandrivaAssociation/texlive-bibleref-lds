# revision 25526
# category Package
# catalog-ctan /macros/latex/contrib/bibleref-lds
# catalog-date 2012-02-27 12:45:12 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-bibleref-lds
Version:	1.0
Release:	9
Summary:	Bible references, including Church of Jesus Christ of Latter Day Saints
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-lds
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-lds.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 02 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 781916
- Import texlive-bibleref-lds
- Import texlive-bibleref-lds

