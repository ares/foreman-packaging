%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name dynflow
%global rubyabi 1.9.1

Summary: DYNamic workFLOW engine
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/apipie-params
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires:       %{?scl_prefix}ruby(release)
%else
Requires:       %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(activesupport)
Requires: %{?scl_prefix}rubygem(algebrick)
Requires: %{?scl_prefix}rubygem(multi_json)
Requires: %{?scl_prefix}rubygem(apipie-params)
Requires: %{?scl_prefix}rubygem(uuidtools)
%if 0%{?fedora} > 18
BuildRequires:       %{?scl_prefix}ruby(release)
%else
BuildRequires:       %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Generate and executed workflows dynamically based on input data and
leave it open for others to jump into it as well

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/web
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/examples

%changelog
* Mon Apr 07 2014 Ivan Nečas <inecas@redhat.com> 0.6.1-1
- Bump version (inecas@redhat.com)

* Tue Mar 25 2014 Ivan Nečas <inecas@redhat.com> 0.6.0-1
- Bump version (inecas@redhat.com)

* Tue Mar 18 2014 Ivan Nečas <inecas@redhat.com> 0.5.1-1
- Bump version (inecas@redhat.com)

* Tue Feb 25 2014 Ivan Nečas <inecas@redhat.com> 0.5.0-1
- Bump to version 0.5.0 (inecas@redhat.com)

* Wed Aug 28 2013 Partha Aji <paji@redhat.com> 0.1.0-2
- F19 Changes - made ruby abi conditional (paji@redhat.com)

* Tue May 07 2013 Ivan Necas <inecas@redhat.com> 0.1.0-1
- new package built with tito

