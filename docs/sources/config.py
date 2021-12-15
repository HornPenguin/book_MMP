from docutils.writers.latex2e import Babel
Babel.language_codes = {'ko':'korean', 'en':'english'}

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Mathematical Methods for Physicsts'
copyright = '2021, Hyun Seong, Kim'
author = 'Hyun Seong, Kim'

release = '2.7.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinxcontrib.proof"
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
epub_author ='Hyun Seong, Kim'
epub_publisher = 'OFPublisher'

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{Noto Serif CJK KR}
\setsansfont{Noto Sans CJK KR}
\setmonofont{Noto Sans Mono CJK KR}
    '''
}
