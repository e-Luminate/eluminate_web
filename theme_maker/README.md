e-Luminate theme
================

This is based on a clone of the swatchmaker directory from https://github.com/thomaspark/bootswatch.git,
with swatch/bootswatch.less and swatch/variables.less originally from the cyborg theme.


1. Download Bootstrap
------
Run the command `make bootstrap` to update to the latest version of Bootstrap.


2. Install LESS
------
If you haven't already, install LESS to your machine via NPM. More information on that here: http://lesscss.org/#-server-side-usage


3. Customize Bootstrap
------
Make your customizations to the two files found in the `swatch` directory, `variables.less` and `bootswatch.less`.


4. Build Customized Bootstrap
------
In this  directory, run `make bootswatch` (or just `make`). The compiled CSS files will be created in the `swatch` directory, and copied to the e-Luminate static/css directory.

You can run the watcher to automatically build Bootstrap whenever changes are saved with `ruby watcher.rb`. Requires `gem install directory_watcher`.


5. Reset Bootstrap
------
If you want to reset `variables.less` and `bootswatch.less` to defaults, run `make default`.