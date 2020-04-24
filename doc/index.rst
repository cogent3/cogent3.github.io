
``cogent3`` is a mature python library for analysis of biological sequence data. We endeavour to provide a first-class experience within Jupyter notebooks, but the algorithms also support parallel execution on compute systems with 1000's of processors.

``cogent3`` is released under the BSD-3 license, links to documentation and code are above. If you would like to contribute (and we hope you do!), we have created a companion `c3dev <https://github.com/cogent3/c3dev>`_ repo which provides details on how to contribute and some useful tools for doing so.

**Who is it for? Anyone who wants to analyse sequence divergence using robust statistical models.**

``cogent3`` is unique in providing numerous non-stationary Markov models :cite:`2015.Kaehler.000` for modelling sequence evolution, including novel codon models :cite:`2017.Kaehler.000`. ``cogent3`` also includes an extensive collection of time-reversible models (again including novel codon models  :cite:`2010.Yap.000`). We have done more than just invent these new methods, we have established the most robust algorithms :cite:`2008.Schranz.000` for their implementation and their suitability for real data :cite:`2013.Verbyla.000`. Additionally, there are novel signal processing methods focussed on statistical estimation of integer period signals :cite:`2011.Epps.000,2012.Bellani.000`.

.. todo:: LINK TO DOCS

**Anyone who wants to undertake exploratory genomic data analysis**

Beyond our novel methods, ``cogent3`` provides an extensive suite of capabilities for manipulating and analysing sequence data. For instance, the ability to read standard biological data formats, manipulate sequences by their annotations, to perform multiple sequence alignment using any of our substitution models, phylogenetic reconstruction and tree manipulation, manipulation of tabular data, visualisation of phylogenies and much more.


.. todo:: LINK TO DOCS

**Anyone looking for a functional programming style approach to genomic data analysis**

Our ``cogent3.app`` module provides a very different approach to using the library capabilities. Notably, a functional programming style interface lowers the barrier to entry for using ``cogent3``\ 's advanced capabilities. It also supports building pipelines suitable for large-scale analysis. Individuals comfortable with R should find this interface pretty easy to use.

.. todo:: LINK TO DOCS

.. toctree::
    :hidden:
    :maxdepth: 1

    Documentation Release <https://github.com/cogent3/>
    Documentation Development <https://github.com/cogent3/cetest>
    history


------

.. rubric:: References

.. bibliography:: cogent3.bib
    :filter: docname in docnames
    :style: unsrt