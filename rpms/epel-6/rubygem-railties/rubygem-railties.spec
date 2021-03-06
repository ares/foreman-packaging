%define rbname railties
%define version 3.2.13
%define release 2

Summary: Tools for creating, working with, and running Rails applications.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem

BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
Requires: rubygem-rake >= 0.8.7
Requires: rubygem-rack-ssl => 1.3.2
Requires: rubygem-rack-ssl < 1.4
Requires: rubygem-thor >= 0.14.6
Requires: rubygem-thor < 2.0
Requires: rubygem-rdoc => 3.4
Requires: rubygem-rdoc < 4
Requires: rubygem-activesupport = 3.2.13
Requires: rubygem-actionpack = 3.2.13

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10

BuildArch: noarch

Provides: rubygem(railties) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Rails internals: application bootup, plugins, generators, and rake tasks.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/rails
%{gemdir}/gems/railties-%{version}/CHANGELOG.md
%{gemdir}/gems/railties-%{version}/README.rdoc
%{gemdir}/gems/railties-%{version}/bin/rails
%{gemdir}/gems/railties-%{version}/guides/assets/images/belongs_to.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/book_icon.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/bullet.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/challenge.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/chapters_icon.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/check_bullet.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/credits_pic_blank.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/csrf.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/customized_error_messages.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/edge_badge.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/error_messages.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/feature_tile.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/footer_tile.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/fxn.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/grey_bullet.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/habtm.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/has_many.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/has_many_through.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/has_one.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/has_one_through.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/header_backdrop.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/header_tile.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/i18n/demo_html_safe.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/i18n/demo_localized_pirate.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/i18n/demo_translated_en.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/i18n/demo_translated_pirate.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/i18n/demo_translation_missing.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/i18n/demo_untranslated.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/1.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/10.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/11.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/12.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/13.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/14.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/15.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/2.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/3.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/4.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/5.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/6.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/7.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/8.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/callouts/9.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/caution.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/example.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/home.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/important.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/next.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/note.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/prev.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/README
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/tip.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/up.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/icons/warning.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/jaimeiniesta.jpg
%{gemdir}/gems/railties-%{version}/guides/assets/images/nav_arrow.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/polymorphic.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/posts_index.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/radar.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/rails_guides_kindle_cover.jpg
%{gemdir}/gems/railties-%{version}/guides/assets/images/rails_guides_logo.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/rails_logo_remix.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/rails_welcome.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/session_fixation.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/tab_grey.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/tab_info.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/tab_note.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/tab_red.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/tab_yellow.gif
%{gemdir}/gems/railties-%{version}/guides/assets/images/tab_yellow.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/validation_error_messages.png
%{gemdir}/gems/railties-%{version}/guides/assets/images/vijaydev.jpg
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/guides.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushAppleScript.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushAS3.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushBash.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushColdFusion.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushCpp.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushCSharp.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushCss.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushDelphi.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushDiff.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushErlang.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushGroovy.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushJava.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushJavaFX.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushJScript.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPerl.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPhp.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPlain.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPowerShell.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPython.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushRuby.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushSass.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushScala.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushSql.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushVb.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushXml.js
%{gemdir}/gems/railties-%{version}/guides/assets/javascripts/syntaxhighlighter/shCore.js
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/fixes.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/kindle.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/main.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/print.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/reset.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/style.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCore.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreDefault.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreDjango.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreEclipse.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreEmacs.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreFadeToGrey.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreMDUltra.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreMidnight.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreRDark.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeDefault.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeDjango.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeEclipse.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeEmacs.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeFadeToGrey.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeMDUltra.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeMidnight.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeRailsGuides.css
%{gemdir}/gems/railties-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeRDark.css
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/images/rails.png
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/javascripts/application.js
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/javascripts/comments.js.coffee
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/javascripts/home.js.coffee
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/javascripts/posts.js.coffee
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/stylesheets/application.css
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/stylesheets/comments.css.scss
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/stylesheets/home.css.scss
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/stylesheets/posts.css.scss
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/assets/stylesheets/scaffolds.css.scss
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/controllers/application_controller.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/controllers/comments_controller.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/controllers/home_controller.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/controllers/posts_controller.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/helpers/application_helper.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/helpers/comments_helper.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/helpers/home_helper.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/helpers/posts_helper.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/models/comment.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/models/post.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/models/tag.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/comments/_comment.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/comments/_form.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/home/index.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/layouts/application.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/posts/_form.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/posts/edit.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/posts/index.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/posts/new.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/posts/show.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/app/views/tags/_form.html.erb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/application.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/boot.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/database.yml
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/environment.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/environments/development.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/environments/production.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/environments/test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/initializers/inflections.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/initializers/mime_types.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/initializers/secret_token.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/initializers/session_store.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/initializers/wrap_parameters.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/locales/en.yml
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config/routes.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/config.ru
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/db/migrate/20110901012504_create_posts.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/db/migrate/20110901012815_create_comments.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/db/migrate/20110901013701_create_tags.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/db/schema.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/db/seeds.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/doc/README_FOR_APP
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/Gemfile
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/public/404.html
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/public/422.html
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/public/500.html
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/public/favicon.ico
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/public/robots.txt
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/Rakefile
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/README.rdoc
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/script/rails
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/fixtures/comments.yml
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/fixtures/posts.yml
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/fixtures/tags.yml
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/functional/comments_controller_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/functional/home_controller_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/functional/posts_controller_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/performance/browsing_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/test_helper.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/unit/comment_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/unit/helpers/comments_helper_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/unit/helpers/home_helper_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/unit/helpers/posts_helper_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/unit/post_test.rb
%{gemdir}/gems/railties-%{version}/guides/code/getting_started/test/unit/tag_test.rb
%{gemdir}/gems/railties-%{version}/guides/rails_guides/generator.rb
%{gemdir}/gems/railties-%{version}/guides/rails_guides/helpers.rb
%{gemdir}/gems/railties-%{version}/guides/rails_guides/indexer.rb
%{gemdir}/gems/railties-%{version}/guides/rails_guides/levenshtein.rb
%{gemdir}/gems/railties-%{version}/guides/rails_guides/textile_extensions.rb
%{gemdir}/gems/railties-%{version}/guides/rails_guides.rb
%{gemdir}/gems/railties-%{version}/guides/source/2_2_release_notes.textile
%{gemdir}/gems/railties-%{version}/guides/source/2_3_release_notes.textile
%{gemdir}/gems/railties-%{version}/guides/source/3_0_release_notes.textile
%{gemdir}/gems/railties-%{version}/guides/source/3_1_release_notes.textile
%{gemdir}/gems/railties-%{version}/guides/source/3_2_release_notes.textile
%{gemdir}/gems/railties-%{version}/guides/source/_license.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/_welcome.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/action_controller_overview.textile
%{gemdir}/gems/railties-%{version}/guides/source/action_mailer_basics.textile
%{gemdir}/gems/railties-%{version}/guides/source/action_view_overview.textile
%{gemdir}/gems/railties-%{version}/guides/source/active_model_basics.textile
%{gemdir}/gems/railties-%{version}/guides/source/active_record_basics.textile
%{gemdir}/gems/railties-%{version}/guides/source/active_record_querying.textile
%{gemdir}/gems/railties-%{version}/guides/source/active_record_validations_callbacks.textile
%{gemdir}/gems/railties-%{version}/guides/source/active_resource_basics.textile
%{gemdir}/gems/railties-%{version}/guides/source/active_support_core_extensions.textile
%{gemdir}/gems/railties-%{version}/guides/source/api_documentation_guidelines.textile
%{gemdir}/gems/railties-%{version}/guides/source/asset_pipeline.textile
%{gemdir}/gems/railties-%{version}/guides/source/association_basics.textile
%{gemdir}/gems/railties-%{version}/guides/source/caching_with_rails.textile
%{gemdir}/gems/railties-%{version}/guides/source/command_line.textile
%{gemdir}/gems/railties-%{version}/guides/source/configuring.textile
%{gemdir}/gems/railties-%{version}/guides/source/contributing_to_ruby_on_rails.textile
%{gemdir}/gems/railties-%{version}/guides/source/credits.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/debugging_rails_applications.textile
%{gemdir}/gems/railties-%{version}/guides/source/documents.yaml
%{gemdir}/gems/railties-%{version}/guides/source/engines.textile
%{gemdir}/gems/railties-%{version}/guides/source/form_helpers.textile
%{gemdir}/gems/railties-%{version}/guides/source/generators.textile
%{gemdir}/gems/railties-%{version}/guides/source/getting_started.textile
%{gemdir}/gems/railties-%{version}/guides/source/i18n.textile
%{gemdir}/gems/railties-%{version}/guides/source/index.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/initialization.textile
%{gemdir}/gems/railties-%{version}/guides/source/kindle/copyright.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/kindle/KINDLE.md
%{gemdir}/gems/railties-%{version}/guides/source/kindle/layout.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/kindle/rails_guides.opf.erb
%{gemdir}/gems/railties-%{version}/guides/source/kindle/toc.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/kindle/toc.ncx.erb
%{gemdir}/gems/railties-%{version}/guides/source/kindle/welcome.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/layout.html.erb
%{gemdir}/gems/railties-%{version}/guides/source/layouts_and_rendering.textile
%{gemdir}/gems/railties-%{version}/guides/source/migrations.textile
%{gemdir}/gems/railties-%{version}/guides/source/nested_model_forms.textile
%{gemdir}/gems/railties-%{version}/guides/source/performance_testing.textile
%{gemdir}/gems/railties-%{version}/guides/source/plugins.textile
%{gemdir}/gems/railties-%{version}/guides/source/rails_application_templates.textile
%{gemdir}/gems/railties-%{version}/guides/source/rails_on_rack.textile
%{gemdir}/gems/railties-%{version}/guides/source/routing.textile
%{gemdir}/gems/railties-%{version}/guides/source/ruby_on_rails_guides_guidelines.textile
%{gemdir}/gems/railties-%{version}/guides/source/security.textile
%{gemdir}/gems/railties-%{version}/guides/source/testing.textile
%{gemdir}/gems/railties-%{version}/guides/w3c_validator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/all.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application/bootstrap.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application/configuration.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application/finisher.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application/railties.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application/route_inspector.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application/routes_reloader.rb
%{gemdir}/gems/railties-%{version}/lib/rails/application.rb
%{gemdir}/gems/railties-%{version}/lib/rails/backtrace_cleaner.rb
%{gemdir}/gems/railties-%{version}/lib/rails/cli.rb
%{gemdir}/gems/railties-%{version}/lib/rails/code_statistics.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/application.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/benchmarker.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/console.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/dbconsole.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/destroy.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/generate.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/plugin.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/plugin_new.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/profiler.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/runner.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/server.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands/update.rb
%{gemdir}/gems/railties-%{version}/lib/rails/commands.rb
%{gemdir}/gems/railties-%{version}/lib/rails/configuration.rb
%{gemdir}/gems/railties-%{version}/lib/rails/console/app.rb
%{gemdir}/gems/railties-%{version}/lib/rails/console/helpers.rb
%{gemdir}/gems/railties-%{version}/lib/rails/engine/commands.rb
%{gemdir}/gems/railties-%{version}/lib/rails/engine/configuration.rb
%{gemdir}/gems/railties-%{version}/lib/rails/engine/railties.rb
%{gemdir}/gems/railties-%{version}/lib/rails/engine.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/actions.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/active_model.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/app_base.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/base.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/css/assets/assets_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/css/assets/templates/stylesheet.css
%{gemdir}/gems/railties-%{version}/lib/rails/generators/css/scaffold/scaffold_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/controller/controller_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/controller/templates/view.html.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/mailer/mailer_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/mailer/templates/view.text.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/scaffold/scaffold_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/scaffold/templates/_form.html.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/scaffold/templates/edit.html.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/scaffold/templates/index.html.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/scaffold/templates/new.html.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb/scaffold/templates/show.html.erb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/erb.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/generated_attribute.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/js/assets/assets_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/js/assets/templates/javascript.js
%{gemdir}/gems/railties-%{version}/lib/rails/generators/migration.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/named_base.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/app_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/app/assets/images/rails.png
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/app/assets/javascripts/application.js.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/app/assets/stylesheets/application.css
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/app/controllers/application_controller.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/app/helpers/application_helper.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/app/views/layouts/application.html.erb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/application.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/boot.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/frontbase.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/ibm_db.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbc.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbcmysql.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbcpostgresql.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbcsqlite3.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/mysql.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/oracle.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/postgresql.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/databases/sqlite3.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/environment.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/environments/development.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/environments/production.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/environments/test.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/initializers/inflections.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/initializers/mime_types.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/initializers/secret_token.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/initializers/session_store.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/initializers/wrap_parameters.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/locales/en.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config/routes.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/config.ru
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/db/seeds.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/doc/README_FOR_APP
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/Gemfile
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/gitignore
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/public/404.html
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/public/422.html
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/public/500.html
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/public/favicon.ico
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/public/index.html
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/public/robots.txt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/Rakefile
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/README
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/script/rails
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/test/performance/browsing_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/templates/test/test_helper.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/app/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/assets/assets_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/assets/templates/javascript.js
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/assets/templates/stylesheet.css
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/assets/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/controller/controller_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/controller/templates/controller.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/controller/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/generator/generator_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/generator/templates/%file_name%_generator.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/generator/templates/USAGE.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/generator/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/helper/helper_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/helper/templates/helper.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/helper/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/integration_test/integration_test_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/integration_test/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/migration/migration_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/migration/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/model/model_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/model/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/observer/observer_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/observer/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/performance_test/performance_test_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/performance_test/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/plugin_new_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/[%]name[%].gemspec
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/app/controllers/[%]name[%]/application_controller.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/app/helpers/[%]name[%]/application_helper.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/app/views/layouts/[%]name[%]/application.html.erb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/config/routes.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/Gemfile
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/gitignore
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/lib/[%]name[%]/engine.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/lib/[%]name[%]/version.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/lib/[%]name[%].rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/lib/tasks/[%]name[%]_tasks.rake
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/MIT-LICENSE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/rails/application.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/rails/boot.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/rails/routes.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/Rakefile
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/README.rdoc
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/script/rails.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/test/[%]name[%]_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/test/integration/navigation_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/templates/test/test_helper.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/plugin_new/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/resource/resource_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/resource/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/resource_route/resource_route_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/scaffold/scaffold_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/scaffold/templates/scaffold.css
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/scaffold/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/scaffold_controller/scaffold_controller_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/scaffold_controller/templates/controller.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/scaffold_controller/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/session_migration/session_migration_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/session_migration/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/task/task_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/task/templates/task.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/rails/task/USAGE
%{gemdir}/gems/railties-%{version}/lib/rails/generators/resource_helpers.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_case.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/controller/controller_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/controller/templates/functional_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/helper/helper_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/helper/templates/helper_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/integration/integration_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/integration/templates/integration_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/mailer/mailer_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/mailer/templates/functional_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/model/model_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/model/templates/fixtures.yml
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/model/templates/unit_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/observer/observer_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/observer/templates/unit_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/performance/performance_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/performance/templates/performance_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/plugin/plugin_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/plugin/templates/%file_name%_test.rb.tt
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/plugin/templates/test_helper.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/scaffold/scaffold_generator.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit/scaffold/templates/functional_test.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators/test_unit.rb
%{gemdir}/gems/railties-%{version}/lib/rails/generators.rb
%{gemdir}/gems/railties-%{version}/lib/rails/info.rb
%{gemdir}/gems/railties-%{version}/lib/rails/info_controller.rb
%{gemdir}/gems/railties-%{version}/lib/rails/initializable.rb
%{gemdir}/gems/railties-%{version}/lib/rails/paths.rb
%{gemdir}/gems/railties-%{version}/lib/rails/performance_test_help.rb
%{gemdir}/gems/railties-%{version}/lib/rails/plugin.rb
%{gemdir}/gems/railties-%{version}/lib/rails/rack/debugger.rb
%{gemdir}/gems/railties-%{version}/lib/rails/rack/log_tailer.rb
%{gemdir}/gems/railties-%{version}/lib/rails/rack/logger.rb
%{gemdir}/gems/railties-%{version}/lib/rails/rack.rb
%{gemdir}/gems/railties-%{version}/lib/rails/railtie/configurable.rb
%{gemdir}/gems/railties-%{version}/lib/rails/railtie/configuration.rb
%{gemdir}/gems/railties-%{version}/lib/rails/railtie.rb
%{gemdir}/gems/railties-%{version}/lib/rails/ruby_version_check.rb
%{gemdir}/gems/railties-%{version}/lib/rails/rubyprof_ext.rb
%{gemdir}/gems/railties-%{version}/lib/rails/script_rails_loader.rb
%{gemdir}/gems/railties-%{version}/lib/rails/source_annotation_extractor.rb
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/annotations.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/documentation.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/engine.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/framework.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/log.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/middleware.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/misc.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/routes.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/statistics.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks/tmp.rake
%{gemdir}/gems/railties-%{version}/lib/rails/tasks.rb
%{gemdir}/gems/railties-%{version}/lib/rails/test_help.rb
%{gemdir}/gems/railties-%{version}/lib/rails/test_unit/railtie.rb
%{gemdir}/gems/railties-%{version}/lib/rails/test_unit/sub_test_task.rb
%{gemdir}/gems/railties-%{version}/lib/rails/test_unit/testing.rake
%{gemdir}/gems/railties-%{version}/lib/rails/version.rb
%{gemdir}/gems/railties-%{version}/lib/rails.rb


%doc %{gemdir}/doc/railties-%{version}
%{gemdir}/cache/railties-%{version}.gem
%{gemdir}/specifications/railties-%{version}.gemspec

%changelog
* Fri Apr 12 2013 shk@redhat.com 3.2.13-1
- Updated to 3.2.13
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
