***************
Project History
***************

``cogent3`` is a descendant of PyCogent. While there is much in common with PyCogent, the amount of change has been substantial, motivating the new name [*]_.

Given this history, we are grateful to the multitude of individuals who have made contributions over the years. These individuals are explicitly acknowledged in all the files they contributed to and were co-authors on the original PyEvolve :cite:`2004.Butterfield.000` and PyCogent :cite:`2007.Knight.000` publications.

Compared to PyCogent version 1.9, there have been massive changes. These include:

- integration of many of the new developments on algorithms and modelling published by the `Huttley lab <https://biology.anu.edu.au/research/groups/huttley-group-bioinformatics-molecular-evolution-genomes>`_ over the last decade
- an experimental ``cogent3.app`` module that presents a functional programming style interface to ``cogent3``
- modernised our dependencies including using ``plotly`` for visualisation, ``tqdm`` for progress bar display, ``concurrent.futures`` and ``mpi4py.futures`` for parallel process execution, ``tox`` and ``pytest`` for unit testing
- switched to calendar based versioning

The rewrite has been a massive amount of work and unfortunately the changes to the API are only indirectly documented by virtue of having the documentation match the library state. Thus, the best way to get older PyCogent scripts working is to check the Library documentation related to your code. More explicitly, you can also search in the `repository history <https://github.com/cogent3/cogent3>`_.

``cogent3`` no longer includes module ``x``, what do I do?
==========================================================

.. glossary::
    ``cogent.app``
        The ``PyCogent`` module was concerned with wrapping external applications. There are multple 3rd party alternatives to this, for example ``click``, ``burrito``, etc.. The ``cogent3.app`` module is very different being focussed on providing a functional style interface to ``cogent3`` capabilities.

    ``cogent.db.ensembl``
        This has been turned into a standalone project, `EnsemblDb3 <https://github.com/cogent3/ensembldb3>`_.

    ``cogent.db.eutils``
        For querying NCBI via their EUtils interface. A replacement is `biocommons/eutils <https://github.com/biocommons/eutils>`_.

    ``cogent.struct``
        For manipulating 3D structures. We know of no replacements.

    ``cogent.motif``
        A subset of k-mer analyses. No direct replacements.

    ``cogent.seqsim``
        See the sequence simulation capabilities in ``cogent3.evolve`` and ``cogent3.app.evo``.

    ``cogent.maths.unifrac``
        The microbiome related functions are now in `scikit-bio <https://scikit-bio.org>`_.

.. _cogent3: https://github.com/cogent3/cogent3

.. [*] it's Python 3 only amd ``cogent`` was always the import name for PyCogent (dating back to PyEvolve :cite:`2004.Butterfield.000`).

------

.. rubric:: References

.. bibliography:: cogent3.bib
    :filter: docname in docnames
    :style: plain
