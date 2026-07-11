%global tl_name ksp-thesis
%global tl_revision 39080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	A LaTeX class for theses published with KIT Scientific Publishing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ksp-thesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ksp-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ksp-thesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class intended for authors who want to
publish their thesis or other scientific work with KIT Scientific
Publishing (KSP). The class is based on the scrbook class of the KOMA-
script bundle in combination with the ClassicThesis and ArsClassica
packages. It modifies some of the layout and style definitions of these
packages in order to provide a document layout that should be compatible
with the requirements by KSP.

