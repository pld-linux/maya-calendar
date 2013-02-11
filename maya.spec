%define		rel		0.1
%define		subver	408
Summary:	GCal-syncing GTK+ Calendar application
Name:		maya
Version:	0.1.0
Release:	0.%{subver}.%{rel}
License:	GPL v3
Group:		X11/Applications
Source0:	%{name}.tar.bz2
# Source0-md5:	e4df43c43a68d6764298fa7a31476db4
URL:		https://launchpad.net/maya
BuildRequires:	cmake
BuildRequires:	evolution-data-server-devel >= 3.2.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	granite-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libgee0.6-devel
BuildRequires:	libical-devel
BuildRequires:	pkgconfig
BuildRequires:	vala
Requires:	glib2 >= 1:2.26.0
Requires:	gtk-update-icon-cache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maya is a slim, lightweight, GCal-syncing GTK+ Calendar application
written in Vala, specifically for the elementary project.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%glib_compile_schemas

%postun
%update_desktop_database
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
