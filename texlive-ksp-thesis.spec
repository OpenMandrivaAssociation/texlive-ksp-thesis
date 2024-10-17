Name:		texlive-ksp-thesis
Version:	39080
Release:	2
Summary:	A LaTeX class for theses published with KIT Scientific Publishing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ksp-thesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ksp-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ksp-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class intended for authors who
want to publish their thesis or other scientific work with KIT
Scientific Publishing (KSP). The class is based on the scrbook
class of the KOMA-script bundle in combination with the
ClassicThesis and ArsClassica packages. It modifies some of the
layout and style definitions of these packages in order to
provide a document layout that should be compatible with the
requirements by KSP.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ksp-thesis
%doc %{_texmfdistdir}/doc/latex/ksp-thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
