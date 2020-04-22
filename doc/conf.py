import sphinx_bootstrap_theme

project = "cogent3"
copyright = "2020, Gavin Huttley"
author = "Gavin Huttley"

# The full version, including alpha/beta/rc tags
release = "2020.4"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]


html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()


html_theme_options = {
    "navbar_title": "cogent3",
    "navbar_site_name": "Site",
    "navbar_links": [
        ("Install", "install"),
        ("Docs", "https://cogent3.readthedocs.io", True),
        ("Code", "https://github.com/cogent3/cogent3", True),
        ("Projects Using", "projects"),
        (
            "Code of Conduct",
            "https://github.com/cogent3/c3dev/wiki/Code-of-Conduct",
            True,
        ),
    ],
    "navbar_class": "navbar navbar-inverse",
    "navbar_fixed_top": "true",
    "source_link_position": "skipped",
    "bootswatch_theme": "cerulean",
    "bootstrap_version": "3",
}


todo_include_todos = True
todo_emit_warnings = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# sidebar_collapse = False
