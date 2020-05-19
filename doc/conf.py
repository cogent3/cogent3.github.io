import os
import pathlib
import shutil
import sys
from glob import glob

# sphinx_navtree
# html_theme = "sphinx_rtd_theme"
import sphinx_bootstrap_theme

project = "cogent3"
copyright = "2020, cogent3 Team"
author = "Gavin Huttley"

# The full version, including alpha/beta/rc tags
release = "2020.4"


# -- General configuration ---------------------------------------------------

# set the plotly renderer
os.environ["PLOTLY_RENDERER"] = "sphinx_gallery"

sys.path.append("../src")

# Allow autosummary to generate stub files
autosummary_generate = True

# Prevent numpydoc from requiring stub files for methods
numpydoc_class_members_toctree = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "numpydoc",
    "sphinx.ext.todo",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxcontrib.bibtex",
]


html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    "navbar_site_name": "Site",
    "navbar_links": [
        ("Install", "doc/install", False),
        ("Docs", "doc/index", False),
        ("Gallery", "doc/draw/index.html", True),
    ],
    "navbar_class": "navbar navbar",
    "navbar_fixed_top": "true",
    "source_link_position": "skipped",
    "bootswatch_theme": "Cerulean",
    "bootstrap_version": "3",
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
    "dev/draw_examples/README.rst",
    "dev/draw_examples/aln/README.rst",
    "dev/draw_examples/tree/README.rst",
]

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

show_authors = True

pygments_style = "sphinx"

todo_include_todos = True
todo_emit_warnings = True

sidebar_collapse = False

html_static_path = ["_static"]

htmlhelp_basename = "cogent3doc"

# -- Options for Sphinx Gallery

nbsphinx_requirejs_path = "require.js"


def plotly_sg_scraper(block, block_vars, gallery_conf, *args, **kwargs):
    examples_dirs = gallery_conf["examples_dirs"]
    if isinstance(examples_dirs, (list, tuple)):
        examples_dirs = examples_dirs[0]
    pngs = sorted(glob(os.path.join(examples_dirs, "**", "*.png"), recursive=True))
    htmls = sorted(glob(os.path.join(examples_dirs, "**", "*.html"), recursive=True))
    image_path_iterator = block_vars["image_path_iterator"]
    image_names = list()
    seen = set()
    for html, png in zip(htmls, pngs):
        if png not in seen:
            seen |= {png}
            this_image_path_png = next(image_path_iterator)
            this_image_path_html = os.path.splitext(this_image_path_png)[0] + ".html"
            image_names.append(this_image_path_html)
            shutil.move(png, this_image_path_png)
            shutil.move(html, this_image_path_html)

    # Use the `figure_rst` helper function to generate rST for image files
    from plotly.io._sg_scraper import figure_rst

    return figure_rst(image_names, gallery_conf["src_dir"])


def plotly_sg_scraper_nb(*args, **kwargs):
    try:
        result = plotly_sg_scraper(*args, **kwargs)
    except Exception:
        result = ""
    return result


c3_doc_dir = pathlib.Path("doc")
if c3_doc_dir.exists():
    from sphinx_gallery.sorting import ExplicitOrder, FileNameSortKey

    templates_path = ["doc/templates"]
    image_scrapers = (plotly_sg_scraper_nb,)
    extensions.append("sphinx_gallery.gen_gallery")
    example_dirs = ["doc/draw_examples"]
    gallery_dirs = ["doc/draw"]

    sphinx_gallery_conf = {
        "examples_dirs": example_dirs,
        "subsection_order": ExplicitOrder(
            ["doc/draw_examples/aln", "doc/draw_examples/tree"]
        ),
        "abort_on_example_error": True,
        "within_subsection_order": FileNameSortKey,
        "gallery_dirs": gallery_dirs,
        "image_scrapers": image_scrapers,
        "download_all_examples": False,
    }

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ("index", "cogent3.tex", "cogent3 Documentation", "cogent3 Team", "manual")
]

html_show_sourcelink = False
