***************
Project History
***************

``cogent3`` is a descendant of PyCogent_. While there is much in common with PyCogent, the amount of change has been substantial, motivating a new name ``cogent3``. This name has been chosen because ``cogent`` was always the import name (dating back to PyEvolve :cite:`2004.Butterfield.000`) and it's Python 3 only.

Given this history, we are grateful to the multitude of individuals who have made contributions over the years. These individuals are explicitly acknowledged in all the files they contributed to and were co-authors on the original PyEvolve :cite:`2004.Butterfield.000` and PyCogent :cite:`2007.Knight.000` publications.

Compared to PyCogent version 1.9, there has been a massive amount of changes. These include integration of many of the new developments on algorithms and modelling published by the `Huttley lab <https://biology.anu.edu.au/research/groups/huttley-group-bioinformatics-molecular-evolution-genomes>`_ over the last decade. We have also modernised our dependencies. For example, we now use ``plotly`` for visualisation, ``tqdm`` for progress bar display, ``concurrent.futures`` and ``mpi4py.futures`` for parallel process execution, ``tox`` and ``pytest`` for unit testing.

------

.. rubric:: References

.. bibliography:: cogent3.bib
    :filter: docname in docnames
    :style: plain
