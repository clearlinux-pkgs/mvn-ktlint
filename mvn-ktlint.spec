#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-ktlint
Version  : 0.30.0
Release  : 3
URL      : https://github.com/pinterest/ktlint/archive/0.30.0.tar.gz
Source0  : https://github.com/pinterest/ktlint/archive/0.30.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/0.30.0/ktlint-0.30.0.jar
Source2  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/0.30.0/ktlint-0.30.0.pom
Source3  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-core/0.30.0/ktlint-core-0.30.0.jar
Source4  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-core/0.30.0/ktlint-core-0.30.0.pom
Source5  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0/ktlint-reporter-checkstyle-0.30.0.jar
Source6  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0/ktlint-reporter-checkstyle-0.30.0.pom
Source7  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0/ktlint-reporter-json-0.30.0.jar
Source8  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0/ktlint-reporter-json-0.30.0.pom
Source9  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0/ktlint-reporter-plain-0.30.0.jar
Source10  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0/ktlint-reporter-plain-0.30.0.pom
Source11  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-test/0.30.0/ktlint-test-0.30.0.jar
Source12  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/ktlint-test/0.30.0/ktlint-test-0.30.0.pom
Source13  : https://repo1.maven.org/maven2/com/github/shyiko/ktlint/pom/0.30.0/pom-0.30.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-ktlint-data = %{version}-%{release}
Requires: mvn-ktlint-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
<h1 align="center">
<a href="https://ktlint.github.io/">
<img src="https://cloud.githubusercontent.com/assets/370176/26518284/38b680da-4262-11e7-8d27-2b9e849fb55f.png"/>
</a>
</h1>

%package data
Summary: data components for the mvn-ktlint package.
Group: Data

%description data
data components for the mvn-ktlint package.


%package license
Summary: license components for the mvn-ktlint package.
Group: Default

%description license
license components for the mvn-ktlint package.


%prep
%setup -q -n ktlint-0.30.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-ktlint
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-ktlint/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/0.30.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/0.30.0/ktlint-0.30.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/0.30.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/0.30.0/ktlint-0.30.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-core/0.30.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-core/0.30.0/ktlint-core-0.30.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-core/0.30.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-core/0.30.0/ktlint-core-0.30.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0/ktlint-reporter-checkstyle-0.30.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0/ktlint-reporter-checkstyle-0.30.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0/ktlint-reporter-json-0.30.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0/ktlint-reporter-json-0.30.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0/ktlint-reporter-plain-0.30.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0/ktlint-reporter-plain-0.30.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-test/0.30.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-test/0.30.0/ktlint-test-0.30.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-test/0.30.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-test/0.30.0/ktlint-test-0.30.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/pom/0.30.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/com/github/shyiko/ktlint/pom/0.30.0/pom-0.30.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/0.30.0/ktlint-0.30.0.jar
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/0.30.0/ktlint-0.30.0.pom
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-core/0.30.0/ktlint-core-0.30.0.jar
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-core/0.30.0/ktlint-core-0.30.0.pom
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0/ktlint-reporter-checkstyle-0.30.0.jar
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-checkstyle/0.30.0/ktlint-reporter-checkstyle-0.30.0.pom
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0/ktlint-reporter-json-0.30.0.jar
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-json/0.30.0/ktlint-reporter-json-0.30.0.pom
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0/ktlint-reporter-plain-0.30.0.jar
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-reporter-plain/0.30.0/ktlint-reporter-plain-0.30.0.pom
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-test/0.30.0/ktlint-test-0.30.0.jar
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/ktlint-test/0.30.0/ktlint-test-0.30.0.pom
/usr/share/java/.m2/repository/com/github/shyiko/ktlint/pom/0.30.0/pom-0.30.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-ktlint/LICENSE
