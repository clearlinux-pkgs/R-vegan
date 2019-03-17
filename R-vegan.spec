#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vegan
Version  : 2.5.4
Release  : 24
URL      : https://cran.r-project.org/src/contrib/vegan_2.5-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vegan_2.5-4.tar.gz
Summary  : Community Ecology Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-vegan-lib = %{version}-%{release}
BuildRequires : R-ade4
BuildRequires : R-cclust
BuildRequires : R-permute
BuildRequires : buildreq-R

%description
functions for community and vegetation ecologists.

%package lib
Summary: lib components for the R-vegan package.
Group: Libraries

%description lib
lib components for the R-vegan package.


%prep
%setup -q -c -n vegan

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552803920

%install
export SOURCE_DATE_EPOCH=1552803920
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vegan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vegan
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vegan
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  vegan || :


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
/usr/lib64/R/library/vegan/NEWS.Rd
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
/usr/lib64/R/library/vegan/tests/cca-object-tests.R
/usr/lib64/R/library/vegan/tests/cca-object-tests.Rout.save
/usr/lib64/R/library/vegan/tests/oecosimu-tests.R
/usr/lib64/R/library/vegan/tests/oecosimu-tests.Rout.save
/usr/lib64/R/library/vegan/tests/vegan-tests.R
/usr/lib64/R/library/vegan/tests/vegan-tests.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/vegan/libs/vegan.so
/usr/lib64/R/library/vegan/libs/vegan.so.avx2
/usr/lib64/R/library/vegan/libs/vegan.so.avx512
