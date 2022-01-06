import datetime
import os
import pathlib
import shutil
import sys
from glob import glob


def make_nbsphinx_thumbnails():
    """returns dict of {path: '_images/{path.stem}'"""
    gallery = [
        p for p in pathlib.Path("doc/draw").glob("**/*.rst") if p.stem != "README"
    ]

    return {str(n).split(".")[0]: f"_images/{n.stem}.png" for n in gallery}


# sphinx_navtree
today = datetime.date.today()
year = today.strftime("%Y")
project = "cogent3"
copyright = f"2020-{year}, cogent3 Team"
author = "Gavin Huttley"

# The full version, including alpha/beta/rc tags
# Use clanedar versioning
release = today.strftime("%Y.%m.%d")


# -- General configuration ---------------------------------------------------
sys.path.append("../src")

# Allow autosummary to generate stub files
autosummary_generate = True
add_module_names = False  # don't include module path to module/func names

# Prevent numpydoc from requiring stub files for methods
numpydoc_class_members_toctree = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "jupyter_sphinx",
    "numpydoc",
    "sphinx.ext.todo",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxcontrib.bibtex",
    "sphinx_gallery.load_style",
    "sphinx_panels",
]

bibtex_bibfiles = ["cogent3.bib"]

html_theme = "sphinx_docs_theme"
html_theme_path = [
    "_theme",
]
html_theme_options = {
    "navbar_links": [
        ("Install", "doc/install.html"),
        ("Gallery", "doc/draw/index.html"),
        ("Docs", "doc/index.html"),
        ("Forum", "https://github.com/cogent3/cogent3/discussions"),
        ("GitHub", "https://github.com/cogent3/cogent3"),
        (
            "Site",
            [
                ("Posting Bugs", "general.html"),
                ("Citation", "general.html"),
                ("Support", "general.html"),
                ("History", "history.html"),
                ("Projects", "projects.html"),
                ("License", "doc/licenses.html"),
            ],
        ),
    ],
    "years": copyright,
    "navigation_depth": 6,
}

# todo_include_todos=True # to expose the TODOs, uncomment this line

# The suffix of source filenames.
source_suffix = ".rst", ".ipynb"

# ignore the cookbook/union_dict.rst file as it's specifically included
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "cookbook/union_dict.rst",
]

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

show_authors = True

pygments_style = "sphinx"

todo_include_todos = False
todo_emit_warnings = True

sidebar_collapse = False

html_static_path = ["_static"]

htmlhelp_basename = "cogent3doc"

# -- Options for Gallery

nbsphinx_requirejs_path = "require.js"
nbsphinx_thumbnails = make_nbsphinx_thumbnails()


templates_path = ["doc/templates"]

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ("index", "cogent3.tex", "cogent3 Documentation", "cogent3 Team", "manual")
]

html_show_sourcelink = False


def setup(app):
    app.add_js_file("plotly-latest.min.js")
