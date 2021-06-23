# -*- coding: utf-8 -*-

import glob
import os
import sys
import subprocess

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("21cmfish").version
except DistributionNotFound:
    __version__ = "unknown version"

sys.path.insert(0, os.path.abspath('.'))

# Convert the tutorials
for fn in glob.glob("_static/notebooks/*.ipynb"):
    name = os.path.splitext(os.path.split(fn)[1])[0]
    outfn = os.path.join("tutorials", name + ".rst")
    print("Building {0}...".format(name))
    subprocess.check_call(
        "jupyter nbconvert --template tutorials/tutorial_rst --to rst "
        + fn
        + " --output-dir tutorials",
        shell=True,
    )
    subprocess.check_call("python fix_internal_links.py " + outfn, shell=True)


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = "21cmfish"
copyright = "2021, Charlotte Mason & contributors"
version = __version__
release = __version__

# Readthedocs.
on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if not on_rtd:
    import sphinx_rtd_theme

    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# #
# # 21cmfish documentation build configuration file, created by
# # sphinx-quickstart on Thu Jun 28 12:35:56 2018.
# #
# # This file is execfile()d with the current directory set to its
# # containing dir.
# #
# # Note that not all possible configuration values are present in this
# # autogenerated file.
# #
# # All configuration values have a default; values that are commented out
# # serve to show the default.
#
# # If extensions (or modules to document with autodoc) are in another directory,
# # add these directories to sys.path here. If the directory is relative to the
# # documentation root, use os.path.abspath to make it absolute, like shown here.
# #
# # import os
# # import sys
# # sys.path.insert(0, os.path.abspath('.'))
#
#
# # -- General configuration ------------------------------------------------
#
# # If your documentation needs a minimal Sphinx version, state it here.
# #
# # needs_sphinx = '1.0'
#
# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = [
#     'sphinx.ext.autodoc',
#     # 'sphinx.ext.autosummary',
#     'sphinx.ext.githubpages',
#     'sphinx.ext.intersphinx',
#     'sphinx.ext.mathjax',
#     'sphinx.ext.viewcode',
#     'IPython.sphinxext.ipython_directive',
#     'IPython.sphinxext.ipython_console_highlighting',
#     'matplotlib.sphinxext.plot_directive',
#     'numpydoc',
#     # 'sphinx_copybutton',
#     'sphinx.ext.napoleon'
# ]
#
# # Configuration options for plot_directive. See:
# # https://github.com/matplotlib/matplotlib/blob/f3ed922d935751e08494e5fb5311d3050a3b637b/lib/matplotlib/sphinxext/plot_directive.py#L81
# plot_html_show_source_link = False
# plot_html_show_formats = False
#
# # Generate the API documentation when building
# autosummary_generate = True
# numpydoc_show_class_members = False
# napoleon_numpy_docstring = True
# napoleon_use_param = False
# napoleon_type_aliases = False
#
# # Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']
#
# # The suffix(es) of source filenames.
# # You can specify multiple suffix as a list of string:
# #
# # source_suffix = ['.rst', '.md']
# source_suffix = '.rst'
#
# # The master toctree document.
# master_doc = 'index'
#
# # General information about the project.
# project = '21cmfish'
# copyright = '2021, Charlotte Mason'
# author = 'Charlotte Mason'
#
# # The version info for the project you're documenting, acts as replacement for
# # |version| and |release|, also used in various other places throughout the
# # built documents.
# #
# import py21cmfish
# # The short X.Y version.
# version = py21cmfish.__version__
# # The full version, including alpha/beta/rc tags.
# release = py21cmfish.__version__
#
# # The language for content autogenerated by Sphinx. Refer to documentation
# # for a list of supported languages.
# #
# # This is also used if you do content translation via gettext catalogs.
# # Usually you set "language" from the command line for these cases.
# language = None
#
# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This patterns also effect to html_static_path and html_extra_path
# exclude_patterns = []
#
# # The name of the Pygments (syntax highlighting) style to use.
# # pygments_style = 'sphinx'
#
# # If true, `todo` and `todoList` produce output, else they produce nothing.
# todo_include_todos = True
#
#
# # -- Options for HTML output ----------------------------------------------
#
# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# #
# html_theme = 'sphinx_rtd_theme'
# import sphinx_rtd_theme
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#
# # Theme options are theme-specific and customize the look and feel of a theme
# # further.  For a list of options available for each theme, see the
# # documentation.
# #
# # html_theme_options = {}
#
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
#
# # Custom sidebar templates, must be a dictionary that maps document names
# # to template names.
# #
# # This is required for the alabaster theme
# # refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#     ]
# }
#
#
# # -- Options for HTMLHelp output ------------------------------------------
#
# # Output file base name for HTML help builder.
# htmlhelp_basename = 'py21cmfish'
#
#
# # -- Options for LaTeX output ---------------------------------------------
#
# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     #
#     # 'papersize': 'letterpaper',
#
#     # The font size ('10pt', '11pt' or '12pt').
#     #
#     # 'pointsize': '10pt',
#
#     # Additional stuff for the LaTeX preamble.
#     #
#     # 'preamble': '',
#
#     # Latex figure (float) alignment
#     #
#     # 'figure_align': 'htbp',
# }
#
# # Grouping the document tree into LaTeX files. List of tuples
# # (source start file, target name, title,
# #  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, '21cmfish.tex', '21cmfish Documentation',
#      'Contributors', 'manual'),
# ]
#
#
# # -- Options for manual page output ---------------------------------------
#
# # One entry per manual page. List of tuples
# # (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, '21cmfish', '21cmfish Documentation',
#      [author], 1)
# ]
#
#
# # -- Options for Texinfo output -------------------------------------------
#
# # Grouping the document tree into Texinfo files. List of tuples
# # (source start file, target name, title, author,
# #  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, '21cmfish', '21cmfish Documentation',
#      author, '21cmfish', 'A python package for doing Fisher matrix analyses with 21cmFAST',
#      'Miscellaneous'),
# ]
#
#
#
#
# # Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'numpy': ('https://numpy.org/doc/stable/', None),
#     'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
#     'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
#     'matplotlib': ('https://matplotlib.org/stable', None),
# }
