#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-vegan
Version  : 2.6.6
Release  : 62
URL      : https://cran.r-project.org/src/contrib/vegan_2.6-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vegan_2.6-6.tar.gz
Summary  : Community Ecology Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-vegan-lib = %{version}-%{release}
Requires: R-permute
BuildRequires : R-permute
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
functions for community and vegetation ecologists.

%package lib
Summary: lib components for the R-vegan package.
Group: Libraries

%description lib
lib components for the R-vegan package.


%prep
%setup -q -n vegan
pushd ..
cp -a vegan buildavx2
popd
pushd ..
cp -a vegan buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715704283

%install
export SOURCE_DATE_EPOCH=1715704283
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vegan/DESCRIPTION
/usr/lib64/R/library/vegan/INDEX
/usr/lib64/R/library/vegan/Meta/Rd.rds
/usr/lib64/R/library/vegan/Meta/data.rds
/usr/lib64/R/library/vegan/Meta/features.rds
/usr/lib64/R/library/vegan/Meta/hsearch.rds
/usr/lib64/R/library/vegan/Meta/links.rds
/usr/lib64/R/library/vegan/Meta/nsInfo.rds
/usr/lib64/R/library/vegan/Meta/package.rds
/usr/lib64/R/library/vegan/Meta/vignette.rds
/usr/lib64/R/library/vegan/NAMESPACE
/usr/lib64/R/library/vegan/NEWS.md
/usr/lib64/R/library/vegan/ONEWS
/usr/lib64/R/library/vegan/OldChangeLog
/usr/lib64/R/library/vegan/R/vegan
/usr/lib64/R/library/vegan/R/vegan.rdb
/usr/lib64/R/library/vegan/R/vegan.rdx
/usr/lib64/R/library/vegan/data/BCI.env.rda
/usr/lib64/R/library/vegan/data/BCI.rda
/usr/lib64/R/library/vegan/data/dune.env.rda
/usr/lib64/R/library/vegan/data/dune.phylodis.rda
/usr/lib64/R/library/vegan/data/dune.rda
/usr/lib64/R/library/vegan/data/dune.taxon.rda
/usr/lib64/R/library/vegan/data/mite.env.rda
/usr/lib64/R/library/vegan/data/mite.pcnm.rda
/usr/lib64/R/library/vegan/data/mite.rda
/usr/lib64/R/library/vegan/data/mite.xy.rda
/usr/lib64/R/library/vegan/data/pyrifos.rda
/usr/lib64/R/library/vegan/data/sipoo.map.rda
/usr/lib64/R/library/vegan/data/sipoo.rda
/usr/lib64/R/library/vegan/data/varechem.rda
/usr/lib64/R/library/vegan/data/varespec.rda
/usr/lib64/R/library/vegan/doc/FAQ-vegan.R
/usr/lib64/R/library/vegan/doc/FAQ-vegan.Rmd
/usr/lib64/R/library/vegan/doc/FAQ-vegan.html
/usr/lib64/R/library/vegan/doc/decision-vegan.R
/usr/lib64/R/library/vegan/doc/decision-vegan.Rnw
/usr/lib64/R/library/vegan/doc/decision-vegan.pdf
/usr/lib64/R/library/vegan/doc/diversity-vegan.R
/usr/lib64/R/library/vegan/doc/diversity-vegan.Rnw
/usr/lib64/R/library/vegan/doc/diversity-vegan.pdf
/usr/lib64/R/library/vegan/doc/index.html
/usr/lib64/R/library/vegan/doc/intro-vegan.R
/usr/lib64/R/library/vegan/doc/intro-vegan.Rnw
/usr/lib64/R/library/vegan/doc/intro-vegan.pdf
/usr/lib64/R/library/vegan/doc/partitioning.R
/usr/lib64/R/library/vegan/doc/partitioning.Rnw
/usr/lib64/R/library/vegan/doc/partitioning.pdf
/usr/lib64/R/library/vegan/help/AnIndex
/usr/lib64/R/library/vegan/help/aliases.rds
/usr/lib64/R/library/vegan/help/paths.rds
/usr/lib64/R/library/vegan/help/vegan.rdb
/usr/lib64/R/library/vegan/help/vegan.rdx
/usr/lib64/R/library/vegan/html/00Index.html
/usr/lib64/R/library/vegan/html/R.css
/usr/lib64/R/library/vegan/tests/aitchison-tests.R
/usr/lib64/R/library/vegan/tests/cca-object-tests.R
/usr/lib64/R/library/vegan/tests/cca-object-tests.Rout.save
/usr/lib64/R/library/vegan/tests/decostand-tests.R
/usr/lib64/R/library/vegan/tests/oecosimu-tests.R
/usr/lib64/R/library/vegan/tests/oecosimu-tests.Rout.save
/usr/lib64/R/library/vegan/tests/vegan-tests.R
/usr/lib64/R/library/vegan/tests/vegan-tests.Rout.save

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/vegan/libs/vegan.so
/V4/usr/lib64/R/library/vegan/libs/vegan.so
/usr/lib64/R/library/vegan/libs/vegan.so
