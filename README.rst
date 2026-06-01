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
