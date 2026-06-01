import datetime
import os
import pathlib
import sys

# need to inject cogent3/doc into sys.path and
# PYTHONPATH for autodoc and nbsphinx to find
# the modules
_cogent3_doc = pathlib.Path(__file__).parent / "cogent3" / "doc"
# for autodoc / Sphinx-side imports
sys.path.insert(0, str(_cogent3_doc))
# for nbsphinx/jupyter-sphinx kernel subprocesses, which inherit env vars
# but not sys.path mutations from this file
os.environ["PYTHONPATH"] = os.pathsep.join([
    str(_cogent3_doc),
    os.environ.get("PYTHONPATH", ""),
]).rstrip(os.pathsep)


def make_nbsphinx_thumbnails():
    """returns dict of {path: '_images/{path.stem}'"""
    gallery = [
        p for p in pathlib.Path("doc/draw").glob("**/*.rst") if p.stem != "README"
    ]

    return {str(n).split(".")[0]: f"_images/{n.stem}.png" for n in gallery}


rst_prolog = """
.. |scinexus| replace:: `scinexus <https://scinexus.readthedocs.io>`__
.. |define_app| replace:: `define_app <https://scinexus.readthedocs.io/en/latest/explanation/app-lifecycle.html>`__
.. |data_store| replace:: `data store <https://scinexus.readthedocs.io/en/latest/howto/use-data-stores.html>`__
.. |data_member| replace:: `DataMember <https://scinexus.readthedocs.io/en/latest/reference/data-stores.html#scinexus.data_store.DataMember>`__
.. |not_completed| replace:: `NotCompleted <https://scinexus.readthedocs.io/en/latest/howto/handle-failures.html>`__
.. |track_failures| replace:: `track failures <https://scinexus.readthedocs.io/en/latest/howto/handle-failures.html>`__
.. |app_types| replace:: `app types <https://scinexus.readthedocs.io/en/latest/explanation/app-lifecycle.html>`__
.. |citation| replace:: `citation <https://scinexus.readthedocs.io/en/latest/howto/log-and-cite.html>`__
.. |citations| replace:: `citations <https://scinexus.readthedocs.io/en/latest/howto/log-and-cite.html>`__
.. |dstore_cites| replace:: `data store citations <https://scinexus.readthedocs.io/en/latest/howto/log-and-cite.html#extracting-citations-from-a-data-store>`__
"""

# sphinx_navtree
today = datetime.date.today()
year = today.strftime("%Y")
project = "cogent3"
copyright = f"2020-{year}, cogent3 Team"
author = "Gavin Huttley"

# The full version, including alpha/beta/rc tags
# Use calendar versioning
release = today.strftime("%Y.%m.%d")


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "jupyter_sphinx",
    "nbsphinx",
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinxcontrib.bibtex",
    "sphinx_design",
    "sphinxcontrib.video",
]


# Allow autosummary to generate stub files
autosummary_generate = True
add_module_names = False  # don't include module path to module/func names
# Prevent numpydoc from requiring stub files for methods
numpydoc_class_members_toctree = False
html_logo = "_static/c3-logo.png"
html_favicon = "_static/c3-square.svg"
bibtex_bibfiles = ["cogent3.bib"]

templates_path = ["doc/templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document.
master_doc = "index"
show_authors = True
pygments_style = "sphinx"

todo_include_todos = False
todo_emit_warnings = True
htmlhelp_basename = "cogent3doc"


# ignoring the cookbook/union_dict.rst file as it's specifically included
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "cookbook/union_dict",
    "cookbook/loading_tabular",
    "COGENT3_LICENSE",
    "*tmp*",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_extra_path = ["llms.txt"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
sidebar_collapse = False

html_theme_options = {
    "navigation_depth": 6,
    "show_toc_level": 4,
    "show_nav_level": 0,
    "github_url": "https://github.com/cogent3/cogent3",
    # turns off the secondary side-bar
    # it's default value is ["page-toc", "edit-this-page", "sourcelink"]
    # "secondary_sidebar_items": [],
    # "article_header_start": ["header_buttons.html"],
    # "navbar_center": ["navbar-nav", "navbar-icon-links"],
    # "navbar_end": [],
    "header_links_before_dropdown": 5,
    "collapse_navigation": False,
}
# https://github.com/cogent3/cogent3/discussions

nbsphinx_thumbnails = make_nbsphinx_thumbnails()

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ("index", "cogent3.tex", "cogent3 Documentation", "cogent3 Team", "manual")
]
