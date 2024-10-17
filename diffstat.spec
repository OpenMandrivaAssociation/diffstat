Summary: 	A utility which provides statistics based on the output of diff
Name: 		diffstat
Version: 	1.66
Release: 	1
Group: 		Development/Other
License: 	GPL-like
Url: 		https://dickey.his.com/diffstat/diffstat.html
Source0: 	https://invisible-mirror.net/archives/diffstat/%{name}-%{version}.tgz

%description
The diff command compares files line by line.  Diffstat reads the output
of the diff command and displays a histogram of the insertions, deletions
and modifications in each file.  Diffstat is commonly used to provide
a summary of the changes in large, complex patch files.

Install diffstat if you need a program which provides a summary of the
diff command's output.  You'll need to also install diffutils.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGES
%{_bindir}/diffstat
%{_mandir}/man1/*
