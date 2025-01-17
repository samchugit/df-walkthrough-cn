#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PeridexisErrant's DF Walkthrough documentation build configuration file,
# created by sphinx-quickstart.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex
from time import strftime

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.extlinks',
    'sphinxcontrib.textstyle'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['misc/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of strings:
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PeridexisErrant\'s DF Walkthrough Chinese Edition'
author = 'Sam Chu'
copyright = '{}, {}'.format(strftime('%Y'), author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.  version is x.y; release includes .alpha1 or w/e.
version = release = '0.2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'zh_CN'

# If true, Sphinx will warn about all references where the target cannot
# be found. Default is False.
nitpicky = True

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used,
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build/**', '**.md']

# The reST default role (used for this markup: `text`) for all documents.
default_role = 'ref'

# This config value must be a dictionary of external sites, mapping unique
# short alias names to a base URL and a prefix.
# See http://sphinx-doc.org/ext/extlinks.html
extlinks = {
    'wiki': ('http://dwarffortresswiki.org/%s', None),
    'forums': ('http://www.bay12forums.com/smf/index.php?topic=%s',
               'Bay12 forums thread %s'),
    'reddit': ('https://www.reddit.com/r/dwarffortress/comments/%s', None),
    'dffd': ('http://dffd.bay12games.com/file.php?id=%s', 'DFFD file %s')
}
# some aliases for link directives
extlinks['forum'] = extlinks['forums']
extlinks['DFFD'] = extlinks['dffd']


# -- Options for HTML output ----------------------------------------------

# See https://github.com/bitprophet/alabaster#variables-and-feature-toggles

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
html_style = 'dftext.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'logo': 'logo.png',
    'description': '学习（和失败）可以很有趣！',
    'github_button': False,
    'show_powered_by': False,
    'font_family': "'Noto Serif SC', 'Georgia', serif",
}

# The name for this set of Sphinx documents.
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = None

# The name of an image file (within the static path) to use as the favicon
html_favicon = 'misc/df-icon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['misc/_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = ''

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# "misc/_templates/searchbox.html" is customised to remove API-related text
html_sidebars = {'**': ['about.html', 'localtoc.html', 'searchbox.html']}

# If false, no index or module index is generated.
html_use_index = html_domain_indices = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
      (master_doc,
       'PeridexisErrantsDFWalkthrough.tex',
       'PeridexisErrant 矮人要塞攻略',
       'PeridexisErrant, Sam Chu',
       'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to
# save visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'https://df-walkthrough-zh.readthedocs.org'

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
epub_fix_images = True

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True
