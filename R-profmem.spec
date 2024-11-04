#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-profmem
Version  : 0.6.0
Release  : 24
URL      : https://cran.r-project.org/src/contrib/profmem_0.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/profmem_0.6.0.tar.gz
Summary  : Simple Memory Profiling for R
Group    : Development/Tools
License  : LGPL-2.1
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n profmem
cd %{_builddir}/profmem

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641079656

%install
export SOURCE_DATE_EPOCH=1641079656
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profmem
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profmem
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profmem
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc profmem || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/profmem/DESCRIPTION
/usr/lib64/R/library/profmem/INDEX
/usr/lib64/R/library/profmem/Meta/Rd.rds
/usr/lib64/R/library/profmem/Meta/features.rds
/usr/lib64/R/library/profmem/Meta/hsearch.rds
/usr/lib64/R/library/profmem/Meta/links.rds
/usr/lib64/R/library/profmem/Meta/nsInfo.rds
/usr/lib64/R/library/profmem/Meta/package.rds
/usr/lib64/R/library/profmem/Meta/vignette.rds
/usr/lib64/R/library/profmem/NAMESPACE
/usr/lib64/R/library/profmem/NEWS
/usr/lib64/R/library/profmem/R/profmem
/usr/lib64/R/library/profmem/R/profmem.rdb
/usr/lib64/R/library/profmem/R/profmem.rdx
/usr/lib64/R/library/profmem/WORDLIST
/usr/lib64/R/library/profmem/doc/index.html
/usr/lib64/R/library/profmem/doc/profmem.html
/usr/lib64/R/library/profmem/doc/profmem.md.rsp
/usr/lib64/R/library/profmem/extdata/broken.Rprofmem.out
/usr/lib64/R/library/profmem/extdata/example.Rprofmem.out
/usr/lib64/R/library/profmem/help/AnIndex
/usr/lib64/R/library/profmem/help/aliases.rds
/usr/lib64/R/library/profmem/help/paths.rds
/usr/lib64/R/library/profmem/help/profmem.rdb
/usr/lib64/R/library/profmem/help/profmem.rdx
/usr/lib64/R/library/profmem/html/00Index.html
/usr/lib64/R/library/profmem/html/R.css
/usr/lib64/R/library/profmem/tests/capableOfProfmem.R
/usr/lib64/R/library/profmem/tests/exceptions.R
/usr/lib64/R/library/profmem/tests/profmem,error.R
/usr/lib64/R/library/profmem/tests/profmem,nested.R
/usr/lib64/R/library/profmem/tests/profmem.R
/usr/lib64/R/library/profmem/tests/readRprofmem.R
