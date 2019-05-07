%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global foreman_min_version 1.23.0
%global plugin_name katello
%global gem_name katello
%global prerelease .pre.master
%global mainver 3.13.0
%global release 1

Name:    %{?scl_prefix}rubygem-%{gem_name}
Summary: Content and Subscription Management plugin for Foreman

Version: %{mainver}
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Group:   Applications/Systems
License: GPLv2
URL:     https://theforeman.org/plugins/katello
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}%{?prerelease}.gem

Requires: katello-selinux
Requires: foreman-postgresql
# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(rails)
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix}rubygem(activerecord-import)
Requires: %{?scl_prefix}rubygem(anemone)
Requires: %{?scl_prefix}rubygem(angular-rails-templates)
Requires: %{?scl_prefix}rubygem(apipie-rails) >= 0.5.14
Requires: %{?scl_prefix}rubygem(deface) < 2.0.0
Requires: %{?scl_prefix}rubygem(deface) >= 1.0.2
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.2.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.14.1
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails)
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix}rubygem(qpid_messaging)
Requires: %{?scl_prefix}rubygem(rabl)
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix}rubygem(runcible) >= 2.11.0
Requires: %{?scl_prefix}rubygem(runcible) < 3.0.0
Requires: %{?scl_prefix}rubygem(zest)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ror}rubygem(rails)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix}rubygem(activerecord-import)
BuildRequires: %{?scl_prefix}rubygem(anemone)
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates)
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) >= 0.5.14
BuildRequires: %{?scl_prefix}rubygem(deface) >= 1.0.2
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.2.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.14.1
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails)
BuildRequires: %{?scl_prefix}rubygem(oauth)
BuildRequires: %{?scl_prefix}rubygem(qpid_messaging)
BuildRequires: %{?scl_prefix}rubygem(rabl)
BuildRequires: %{?scl_prefix}rubygem(rest-client)
BuildRequires: %{?scl_prefix}rubygem(runcible) >= 2.11.0
BuildRequires: %{?scl_prefix}rubygem(runcible) < 3.0.0
BuildRequires: %{?scl_prefix}rubygem(zest)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies
Obsoletes: %{?scl_prefix}rubygem-%{gem_name}_ostree
Obsoletes: %{?scl_prefix}rubygem-bastion
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

# start package.json devDependencies BuildRequires
#BuildRequires: npm(@storybook/react) >= 3.2.17
#BuildRequires: npm(@storybook/react) < 4.0.0
#BuildRequires: npm(@storybook/storybook-deployer) >= 2.0.0
#BuildRequires: npm(@storybook/storybook-deployer) < 3.0.0
BuildRequires: npm(babel-core) >= 6.26.3
BuildRequires: npm(babel-core) < 7.0.0
#BuildRequires: npm(babel-eslint) >= 8.2.6
#BuildRequires: npm(babel-eslint) < 9.0.0
#BuildRequires: npm(babel-jest) >= 23.4.0
#BuildRequires: npm(babel-jest) < 24.0.0
BuildRequires: npm(babel-plugin-transform-class-properties) >= 6.24.1
BuildRequires: npm(babel-plugin-transform-class-properties) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) >= 6.26.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
BuildRequires: npm(babel-polyfill) >= 6.26.0
BuildRequires: npm(babel-polyfill) < 7.0.0
BuildRequires: npm(babel-preset-env) >= 1.6.0
BuildRequires: npm(babel-preset-env) < 2.0.0
BuildRequires: npm(babel-preset-react) >= 6.24.1
BuildRequires: npm(babel-preset-react) < 7.0.0
#BuildRequires: npm(coveralls) >= 3.0.0
#BuildRequires: npm(coveralls) < 4.0.0
#BuildRequires: npm(enzyme) >= 3.4.0
#BuildRequires: npm(enzyme) < 4.0.0
#BuildRequires: npm(enzyme-adapter-react-16) >= 1.4.0
#BuildRequires: npm(enzyme-adapter-react-16) < 2.0.0
#BuildRequires: npm(enzyme-to-json) >= 3.1.2
#BuildRequires: npm(enzyme-to-json) < 4.0.0
#BuildRequires: npm(eslint) >= 4.19.1
#BuildRequires: npm(eslint) < 5.0.0
#BuildRequires: npm(eslint-config-airbnb) >= 16.0.0
#BuildRequires: npm(eslint-config-airbnb) < 17.0.0
#BuildRequires: npm(eslint-plugin-babel) >= 5.1.0
#BuildRequires: npm(eslint-plugin-babel) < 6.0.0
#BuildRequires: npm(eslint-plugin-import) >= 2.7.0
#BuildRequires: npm(eslint-plugin-import) < 3.0.0
#BuildRequires: npm(eslint-plugin-jest) >= 21.18.0
#BuildRequires: npm(eslint-plugin-jest) < 22.0.0
#BuildRequires: npm(eslint-plugin-jsx-a11y) >= 6.0.2
#BuildRequires: npm(eslint-plugin-jsx-a11y) < 7.0.0
#BuildRequires: npm(eslint-plugin-react) >= 7.4.0
#BuildRequires: npm(eslint-plugin-react) < 8.0.0
BuildRequires: npm(identity-obj-proxy) >= 3.0.0
BuildRequires: npm(identity-obj-proxy) < 4.0.0
#BuildRequires: npm(jest) >= 23.4.1
#BuildRequires: npm(jest) < 24.0.0
#BuildRequires: npm(prettier) >= 1.7.4
#BuildRequires: npm(prettier) < 2.0.0
#BuildRequires: npm(react-test-renderer) >= 16.0.0
#BuildRequires: npm(react-test-renderer) < 17.0.0
#BuildRequires: npm(redux-mock-store) >= 1.3.0
#BuildRequires: npm(redux-mock-store) < 2.0.0
BuildRequires: npm(redux-thunk) >= 2.2.0
BuildRequires: npm(redux-thunk) < 3.0.0
# end package.json devDependencies BuildRequires
# start package.json dependencies BuildRequires
BuildRequires: npm(angular) = 1.5.5
BuildRequires: npm(axios) >= 0.17.1
BuildRequires: npm(axios) < 1.0.0
#BuildRequires: npm(axios-mock-adapter) >= 1.10.0
#BuildRequires: npm(axios-mock-adapter) < 2.0.0
BuildRequires: npm(bootstrap-select) = 1.12.4
BuildRequires: npm(classnames) >= 2.2.5
BuildRequires: npm(classnames) < 3.0.0
BuildRequires: npm(downshift) >= 1.28.0
BuildRequires: npm(downshift) < 2.0.0
BuildRequires: npm(jed) >= 1.1.1
BuildRequires: npm(jed) < 2.0.0
BuildRequires: npm(lodash) >= 4.17.5
BuildRequires: npm(lodash) < 5.0.0
BuildRequires: npm(ngreact) >= 0.5.0
BuildRequires: npm(ngreact) < 1.0.0
BuildRequires: npm(patternfly) >= 3.41.1
BuildRequires: npm(patternfly) < 4.0.0
BuildRequires: npm(patternfly-react) >= 2.5.1
BuildRequires: npm(patternfly-react) < 3.0.0
BuildRequires: npm(prop-types) >= 15.6.0
BuildRequires: npm(prop-types) < 16.0.0
BuildRequires: npm(query-string) >= 6.1.0
BuildRequires: npm(query-string) < 7.0.0
BuildRequires: npm(react) >= 16.4.0
BuildRequires: npm(react) < 17.0.0
BuildRequires: npm(react-bootstrap) >= 0.32.1
BuildRequires: npm(react-bootstrap) < 1.0.0
BuildRequires: npm(react-dom) >= 16.4.0
BuildRequires: npm(react-dom) < 17.0.0
BuildRequires: npm(react-ellipsis-with-tooltip) >= 1.0.7
BuildRequires: npm(react-ellipsis-with-tooltip) < 2.0.0
BuildRequires: npm(react-helmet) >= 5.2.0
BuildRequires: npm(react-helmet) < 6.0.0
BuildRequires: npm(react-redux) >= 5.0.6
BuildRequires: npm(react-redux) < 6.0.0
BuildRequires: npm(react-router) >= 4.2.0
BuildRequires: npm(react-router) < 5.0.0
BuildRequires: npm(react-router-bootstrap) = 0.24.4
BuildRequires: npm(react-router-dom) >= 4.2.2
BuildRequires: npm(react-router-dom) < 5.0.0
BuildRequires: npm(redux) >= 3.7.2
BuildRequires: npm(redux) < 4.0.0
BuildRequires: npm(seamless-immutable) >= 7.1.2
BuildRequires: npm(seamless-immutable) < 8.0.0
# end package.json dependencies BuildRequires

%description
Content and Subscription Management plugin for Foreman.


%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for %{pkg_name}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}.

%package assets
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Rebuild the assets for %{pkg_name}

Requires: foreman-assets >= %{foreman_min_version}
# start package.json devDependencies Requires
#Requires: npm(@storybook/react) >= 3.2.17
#Requires: npm(@storybook/react) < 4.0.0
#Requires: npm(@storybook/storybook-deployer) >= 2.0.0
#Requires: npm(@storybook/storybook-deployer) < 3.0.0
Requires: npm(babel-core) >= 6.26.3
Requires: npm(babel-core) < 7.0.0
#Requires: npm(babel-eslint) >= 8.2.6
#Requires: npm(babel-eslint) < 9.0.0
#Requires: npm(babel-jest) >= 23.4.0
#Requires: npm(babel-jest) < 24.0.0
Requires: npm(babel-plugin-transform-class-properties) >= 6.24.1
Requires: npm(babel-plugin-transform-class-properties) < 7.0.0
Requires: npm(babel-plugin-transform-object-rest-spread) >= 6.26.0
Requires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
Requires: npm(babel-polyfill) >= 6.26.0
Requires: npm(babel-polyfill) < 7.0.0
Requires: npm(babel-preset-env) >= 1.6.0
Requires: npm(babel-preset-env) < 2.0.0
Requires: npm(babel-preset-react) >= 6.24.1
Requires: npm(babel-preset-react) < 7.0.0
#Requires: npm(coveralls) >= 3.0.0
#Requires: npm(coveralls) < 4.0.0
#Requires: npm(enzyme) >= 3.4.0
#Requires: npm(enzyme) < 4.0.0
#Requires: npm(enzyme-adapter-react-16) >= 1.4.0
#Requires: npm(enzyme-adapter-react-16) < 2.0.0
#Requires: npm(enzyme-to-json) >= 3.1.2
#Requires: npm(enzyme-to-json) < 4.0.0
#Requires: npm(eslint) >= 4.19.1
#Requires: npm(eslint) < 5.0.0
#Requires: npm(eslint-config-airbnb) >= 16.0.0
#Requires: npm(eslint-config-airbnb) < 17.0.0
#Requires: npm(eslint-plugin-babel) >= 5.1.0
#Requires: npm(eslint-plugin-babel) < 6.0.0
#Requires: npm(eslint-plugin-import) >= 2.7.0
#Requires: npm(eslint-plugin-import) < 3.0.0
#Requires: npm(eslint-plugin-jest) >= 21.18.0
#Requires: npm(eslint-plugin-jest) < 22.0.0
#Requires: npm(eslint-plugin-jsx-a11y) >= 6.0.2
#Requires: npm(eslint-plugin-jsx-a11y) < 7.0.0
#Requires: npm(eslint-plugin-react) >= 7.4.0
#Requires: npm(eslint-plugin-react) < 8.0.0
Requires: npm(identity-obj-proxy) >= 3.0.0
Requires: npm(identity-obj-proxy) < 4.0.0
#Requires: npm(jest) >= 23.4.1
#Requires: npm(jest) < 24.0.0
#Requires: npm(prettier) >= 1.7.4
#Requires: npm(prettier) < 2.0.0
#Requires: npm(react-test-renderer) >= 16.0.0
#Requires: npm(react-test-renderer) < 17.0.0
#Requires: npm(redux-mock-store) >= 1.3.0
#Requires: npm(redux-mock-store) < 2.0.0
Requires: npm(redux-thunk) >= 2.2.0
Requires: npm(redux-thunk) < 3.0.0
# end package.json devDependencies Requires
# start package.json dependencies Requires
Requires: npm(angular) = 1.5.5
Requires: npm(axios) >= 0.17.1
Requires: npm(axios) < 1.0.0
#Requires: npm(axios-mock-adapter) >= 1.10.0
#Requires: npm(axios-mock-adapter) < 2.0.0
Requires: npm(bootstrap-select) = 1.12.4
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
Requires: npm(downshift) >= 1.28.0
Requires: npm(downshift) < 2.0.0
Requires: npm(jed) >= 1.1.1
Requires: npm(jed) < 2.0.0
Requires: npm(lodash) >= 4.17.5
Requires: npm(lodash) < 5.0.0
Requires: npm(ngreact) >= 0.5.0
Requires: npm(ngreact) < 1.0.0
Requires: npm(patternfly) >= 3.41.1
Requires: npm(patternfly) < 4.0.0
Requires: npm(patternfly-react) >= 2.5.1
Requires: npm(patternfly-react) < 3.0.0
Requires: npm(prop-types) >= 15.6.0
Requires: npm(prop-types) < 16.0.0
Requires: npm(query-string) >= 6.1.0
Requires: npm(query-string) < 7.0.0
Requires: npm(react) >= 16.4.0
Requires: npm(react) < 17.0.0
Requires: npm(react-bootstrap) >= 0.32.1
Requires: npm(react-bootstrap) < 1.0.0
Requires: npm(react-dom) >= 16.4.0
Requires: npm(react-dom) < 17.0.0
Requires: npm(react-ellipsis-with-tooltip) >= 1.0.7
Requires: npm(react-ellipsis-with-tooltip) < 2.0.0
Requires: npm(react-helmet) >= 5.2.0
Requires: npm(react-helmet) < 6.0.0
Requires: npm(react-redux) >= 5.0.6
Requires: npm(react-redux) < 6.0.0
Requires: npm(react-router) >= 4.2.0
Requires: npm(react-router) < 5.0.0
Requires: npm(react-router-bootstrap) = 0.24.4
Requires: npm(react-router-dom) >= 4.2.2
Requires: npm(react-router-dom) < 5.0.0
Requires: npm(redux) >= 3.7.2
Requires: npm(redux) < 4.0.0
Requires: npm(seamless-immutable) >= 7.1.2
Requires: npm(seamless-immutable) < 8.0.0
# end package.json dependencies Requires

%description assets
This package can be used to rebuild the assets for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}%{?prerelease}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/app
%{gem_instdir}/ca
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/engines
%{gem_libdir}
%{gem_instdir}/locale
%{gem_instdir}/public/assets/bastion
%{gem_instdir}/public/assets/bastion_katello
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_foreman}
%{foreman_webpack_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%files assets
%{gem_instdir}/package.json
%{gem_instdir}/webpack

%changelog
* Thu Apr 25 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.13.0-0.1.pre.master
- Bump version to 3.13

* Mon Apr 15 2019 Ondrej Prazak <oprazak@redhat.com> - 3.12.0-0.8.pre.master
- Remove foreman_docker as a dependency

* Tue Apr 02 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-0.7.pre.master
- Properly obsolete bastion

* Tue Apr 2 2019 Tomer Brisker- 3.12.0-0.6.pre.master
- Add zest dependency

* Fri Mar 29 2019 Justin Sherrill - 3.12.0-0.5.pre.master
- Remove bastion

* Fri Mar 15 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.12.0-0.4.pre.master
- Update gem and NPM dependencies

* Thu Feb 7 2019 Justin Sherrill <jlsherrill@gmail.com> - 3.12.0-0.3.pre.master
- Require activerecord-import

* Wed Jan 23 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.12.0-0.2.pre.master
- Update gem dependencies

* Wed Jan 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-0.1.pre.master
- Bump version to 3.12

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.11.0-0.2.pre.master
- Update NPM dependencies

* Fri Nov 30 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.11.0-0.1.pre.master
- Bump version to 3.11

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.10.0-0.4.pre.master
- Stop removing JS source maps

* Thu Oct 25 2018 Adam Price <komidore64@gmail.com> - 3.10.0-0.3.pre.master
- add nightly macro

* Wed Oct 24 2018 Adam Price <komidore64@gmail.com> - 3.10.0-0.2.pre.master
- set prerelease to .pre.master

* Thu Oct 18 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.10.0-1
- Bump version to 3.10

* Thu Oct 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-6
- Update NPM dependencies
- Exclude Javascript source maps

* Mon Sep 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-5
- Add nodejs-query-string as a dependency

* Thu Sep 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-4
- Update NPM dependencies

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-3
- Update dependencies

* Tue Jul 24 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-2
- Add prerelease macro support

* Wed Jul 18 2018 Eric D. Helms <ericdhelms@gmail.com> 3.9.0-1.nightly
- Bump to 3.9

* Wed Jun 6 2018 Eric D. Helms <ericdhelms@gmail.com> 3.8.0-1.nightly
- Switch Katello to 3.8