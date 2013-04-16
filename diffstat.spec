Summary: 	A utility which provides statistics based on the output of diff
Name: 		diffstat
Version: 	1.57
Release: 	1
Group: 		Development/Other
License: 	GPL-like
Url: 		http://dickey.his.com/diffstat/diffstat.html
Source0: 	ftp://invisible-island.net/diffstat/%name-%version.tgz

%description
The diff command compares files line by line.  Diffstat reads the output
of the diff command and displays a histogram of the insertions, deletions
and modifications in each file.  Diffstat is commonly used to provide
a summary of the changes in large, complex patch files.

Install diffstat if you need a program which provides a summary of the
diff command's output.  You'll need to also install diffutils.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc CHANGES
%{_bindir}/diffstat
%{_mandir}/man1/*

