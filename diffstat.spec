Summary:	A utility which provides statistics based on the output of diff
Name:		diffstat
Version:	1.55
Release:	%mkrel 1
Group:		Development/Other
License:	GPL-like
URL:		http://dickey.his.com/diffstat/diffstat.html
Source:		ftp://invisible-island.net/diffstat/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES
%{_bindir}/diffstat
%{_mandir}/man1/*
