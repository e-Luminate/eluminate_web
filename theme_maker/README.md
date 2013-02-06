e-Luminate theme
================

Based on a clone of the swatchmaker directory from https://github.com/thomaspark/bootswatch.git

Sourcefiles
-------------
- theme_maker/swatch/variables.less and theme_maker/swatch/bootswatch.less: cyborg theme
- theme_maker/swatch/pinax_theme.less: pinax source
- theme_maker/eluminate_addons.less: site-specific over-rides and additional styling (this 
    replaces eluminate_web/static/less/style.less)

Generated files
---------------
The following files are generated courtesy of honcho parameters in Procfile.dev
Allow a few seconds for this happen
- theme_maker/swatch/bootstrap-responsive.min.css (via theme_maker/swatch/bootstrap-responsive.css)
- theme_maker/swatch/bootstrap.min.css (via theme_maker/swatch/bootstrap.css)

The generated *.min.css files above are then copied into:
- eluminate_web/static/css/
(These replace eluminate_web/static/css/style.css)


