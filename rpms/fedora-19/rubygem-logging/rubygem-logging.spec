%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gemdocdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gemcachedir %{gem_dir}/cache
%global gemspecdir %{gem_dir}/specifications

%global gem_name logging

Summary: A flexible and extendable logging library for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.1
Release: 22%{?dist}
Group: Development/Languages
License: Ruby or BSD
URL: http://rubygems.org/gems/logging
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix}ruby(rubygems)

%if 0%{?fedora} && 0%{?fedora} < 17
Requires: %{?scl_prefix}ruby(abi) = 1.8
%else
%if 0%{?fedora} && 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
%if 0%{?fedora} == 18
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%else
%if 0%{?rhel}
Requires: %{?scl_prefix}ruby(abi) = 1.8
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
%endif
%endif
%endif

Requires: %{?scl_prefix}rubygem(little-plugger) >= 1.1.2
%if 0%{?fedora}
BuildRequires: %{?scl_prefix}rubygems-devel
%endif

BuildRequires: %{?scl_prefix}rubygem(little-plugger) >= 1.1.2
# BuildRequires: %{?scl_prefix}rubygem(flexmock) >= 0.9.0
# BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Logging is a flexible logging library for use in Ruby programs based on the
design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
This package contains documentation for %{pkg_name}.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/data
# contains licensing information
%doc %{gem_instdir}/README.rdoc
# version.txt is needed for runtime
%{gem_instdir}/version.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/lib
%{gemspecdir}/%{gem_name}-%{version}.gemspec
%{gemcachedir}/%{gem_name}-%{version}.gem

%files doc
%{gem_instdir}/examples
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%doc %{gemdocdir}/ri
%doc %{gemdocdir}/rdoc
%doc %{gem_instdir}/History.txt

%changelog
* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.8.1-22
- Remove SCL conditional

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.8.1-21
- Fix SCL logic (shk@redhat.com)

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.8.1-20
- Fix dep issues with ruby-abi (again) (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-19
- Fix ruby-abi version on RHEL (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-18
- Fix ruby-abi version on RHEL (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-17
- gem_dir -> gem_instdir (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-16
- Remove superfluous excludes (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-15
- Add more rubygem-devel stuff (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-14
- Fix gem_instdir (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-13
- Remove test running (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-12
- Remove excessive conditional (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-11
- Fixed a minor syntax error (shk@redhat.com)
- Ensure the correct ABI version or release is used (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 1.8.1-10
- Final bump for release

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 1.8.1-9
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com>
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com>
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.8.1-5
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.6.2-4
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.6.2-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.2-1
- Rebuilt for Ruby 1.9.3.
- Updated to version 1.6.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.1-1
- New version.
- Removed unnecessary defattr macro in files section.
- Removed unnecessary clean section.
- Replaced define macros with more appropriate global.
- Moved gem install to the prep section.
- Added check section to run tests.
- BuildRequires now contain rubygem(little-plugger) and rubygem(flexmock) due to running tests.
- Introduced doc subpackage.

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 1.4.3-1
- Initial package
