# revision 25957
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/friulan
# catalog-date 2012-04-13 12:36:19 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-friulan
Version:	20120413
Release:	2
Summary:	Babel/Polyglossia support for Friulan(Furlan)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/friulan
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/friulan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/friulan.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/friulan.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a language description file that enables
support of Friulan either with babel or with polyglossia.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/friulan/friulan.ldf
%{_texmfdistdir}/tex/latex/friulan/furlan.ldf
%doc %{_texmfdistdir}/doc/latex/friulan/friulan.pdf
#- source
%doc %{_texmfdistdir}/source/latex/friulan/friulan.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
