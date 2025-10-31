%define major 2
%define libname %mklibname QtColorWidgets
%define devname %mklibname QtColorWidgets -d

Name:		QtColorWidgets
Version:	3.0.0
Release:	1
Source0:	https://gitlab.com/mattbas/Qt-Color-Widgets/-/archive/%{version}/Qt-Color-Widgets-%{version}.tar.bz2
Summary:	Qt color picking widgets
URL:		https://gitlab.com/mattbas/Qt-Color-Widgets
License:	LGPL-3.0
Group:		System/Libraries
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildSystem:	cmake
BuildOption:	-DQT_VERSION_MAJOR=6

%description
Qt color picking widgets

%package -n %{libname}
Summary:	Qt color picking widgets
Group:		System/Libraries

%description -n %{libname}
Qt color picking widgets

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}:
Qt color picking widgets

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
