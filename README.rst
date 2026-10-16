cogent3.github.io
#################

This repo contains the top-level documentation for cogent3.org

The ``cogent3`` source (whose ``doc/`` tree we wrap) is included as a git
submodule at ``doc/cogent3``, tracking the ``develop`` branch.

First-time checkout
===================

When cloning, pull the submodule in the same step:

.. code-block:: shell

    git clone --recurse-submodules git@github.com:cogent3/cogent3.github.io.git

If you already cloned without ``--recurse-submodules``:

.. code-block:: shell

    git submodule update --init --recursive

Building the docs
=================

Everything goes through ``build.sh`` at the repo root:

.. code-block:: shell

    ./build.sh                             # full build from the pinned submodule
    C3_REPO=/path/to/cogent3 ./build.sh    # build from your own cogent3 checkout
    ./build.sh --skip-compose              # reuse the already-copied doc/doc/ tree
    ./build.sh --skip-quartodoc            # skip regenerating the API reference

The finished site lands in ``docs/``. Don't commit it, because CI rebuilds
and publishes it.

If you're only changing a page this repo owns, such as ``doc/index.qmd``,
render that one page instead. It's much faster:

.. code-block:: shell

    quarto render doc/index.qmd    # writes doc/_site/index.html
    quarto preview doc             # live reload while you edit

Use ``C3_REPO`` to preview cogent3 doc changes that aren't in the submodule
pin yet.

If you add a new page to the cogent3 docs, you must also add it to the
sidebar in ``doc/_quarto.yml``. Otherwise the build stops with an error.

Updating the submodule to the latest ``develop``
================================================

``git submodule update --init --recursive`` only checks out the commit
pinned by this repo — it does *not* fetch newer commits from the
submodule's remote. To advance to the tip of ``cogent3@develop``:

.. code-block:: shell

    git submodule update --remote doc/cogent3

Then record the new pin in this repo:

.. code-block:: shell

    git add doc/cogent3
    git commit -m "DEV: bump cogent3 submodule"

Working inside the submodule
============================

If you need to make commits against ``cogent3`` itself, ``cd doc/cogent3``
and work there as you would in any clone — it has its own ``origin``
pointing at ``cogent3/cogent3``. After pushing changes upstream, run
``git submodule update --remote doc/cogent3`` from the superproject to
move this repo's pin forward.
