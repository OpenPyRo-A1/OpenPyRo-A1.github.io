# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenPyRo-A1 Docs'
copyright = '2025, Helong Huang'
author = 'Helong Huang'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.video',
    # other extensions
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
      'css/custom.css',
  ]


# invisable
html_meta = {
    'robots': 'noindex, nofollow',  
}
html_theme_options = {
    'show_powered_by': False,      
    'analytics_id': '',            
}