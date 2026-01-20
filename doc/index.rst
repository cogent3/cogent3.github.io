##########################
Making Sense from Sequence
##########################

.. tab-set::

    .. tab-item:: About

        ``cogent3`` is a Python library for the analysis of biological sequence data. We endeavour to provide a first-class experience within Jupyter notebooks, but the algorithms also support parallel execution on compute systems with 1000's of processors.

        Check out the other tabs on this page for installation instructions and highlights of what you can do with ``cogent3``. See the links at the top of the page for an image gallery and detailed user guides.

    .. tab-item:: Installation

        For most uses, we recommend installation with the "extra" dependencies as these add support for visualisation and Jupyter notebooks.

        .. code-block:: shell

            pip install "cogent3[extra]"

        For users on HPC systems, do the vanilla installation.

        .. code-block:: shell

            pip install cogent3

    .. tab-item:: Data wrangling

        ``cogent3`` provides an extensive suite of capabilities for manipulating and analysing sequence data. For instance, the ability to `read standard biological data formats <doc/cookbook/manipulating_biological_data.html>`_, manipulate sequences `by their annotations <doc/examples/seq_features.html>`_, to perform multiple sequence alignment (:ref:`app docs <app-docs>`) using any of our substitution models, `phylogenetic reconstruction <doc/examples/index.html#phylogenetic-reconstruction>`_ and tree manipulation, manipulation of `tabular data <doc/cookbook/tables.html>`_, visualisation of phylogenies (`image gallery`_) and much more.

        .. dropdown:: 🎬 Data wrangling with sequence annotations

            .. video:: https://user-images.githubusercontent.com/3102996/253847297-2611cda8-e078-4b86-a269-43fbf6ced14c.mp4
                :width: 400


    .. tab-item:: Modelling molecular evolution

        Differences in the frequency of nucleotides between species are common. In such cases, non-reversible models of sequence evolution are required for robust estimation of important quantities such as branch lengths, or measuring natural selection :cite:`2015.Kaehler.000, 2017.Kaehler.000` (`see using non-stationary models. <doc/app/index.html#the-model-app>`_). We have done more than just invent these new methods, we have established the most robust algorithms :cite:`2008.Schranz.000` for their implementation and their suitability for real data :cite:`2013.Verbyla.000`.

        .. dropdown:: 🎬 Testing a hypothesis involving a non-stationary nucleotide process

            .. video:: https://user-images.githubusercontent.com/3102996/253849611-6ddd8705-8f16-4b24-b651-68b2123ecdf0.mp4
                :width: 400

    .. tab-item:: Beginner friendly

        You don't have to be an expert in structural programming languages (like Python) to use ``cogent3``! Interactive usage in Jupyter notebooks and a functional programming style interface lowers the barrier to entry. Individuals comfortable with R should find this interface less complex. (See the ``cogent3.app`` documentation.)

        .. dropdown:: 🎬 Using cogent3 apps

            .. video:: https://user-images.githubusercontent.com/3102996/253849168-a821de1a-1aad-4761-970f-e365f6b3b1cd.mp4
                :width: 400


🆕 Features & 📣 Announcements
===============================

.. dropdown:: 🆕 We now support third-party plugins for annotation databases 📚🔌

    If you want to write your own annotation storage backend, `get in touch <https://github.com/cogent3/cogent3/discussions>`_ and we'll give you a hand!

.. dropdown:: 🆕 The ``diverse-seq`` package has been rewritten in rust 🚀!

    The sequence sampling tool `diverse-seq <https://diverse-seq.readthedocs.io>`_, which provides multiple apps for sampling representative sequences, just got faster! The performance critical code has been rewritten in Rust. Give it a try 😀.

.. dropdown:: 🆕 Improved import performance 🎉

    The ``import cogent3`` statement is now much faster! Previously, this statement would trigger imports of many of our dependencies too. Give it a try and report `any issues <https://github.com/cogent3/cogent3/issues>`_ you encounter.

.. dropdown:: 🆕 A new rust-based plugin for k-mer counting 🔌🪝🚀

    We added a new ``count_kmers()`` method to the ``SequenceCollection`` and ``Sequence`` classes. Then, the developers of `Pykmertools <https://github.com/anuradhawick/kmertools>`_ (with a bit of help from us) have released a ``cogent3-pykmertools`` app which makes their rust-based python module for counting k-mers available as ``seqs.count_kmers(k=k, use_hook="cogent3_pykmertools")``. Install it with ``pip install cogent3-pykmertools`` and give it a try. And add a star to the `Pykmertools <https://github.com/anuradhawick/kmertools>`_ repo!

.. dropdown:: 🆕 Third-party tree visualisation demo with iplotx 🎉

    The `iplotx <https://iplotx.readthedocs.io/>`_ team had contributed a demonstration of their tools ability to produce images from `cogent3` tree objects. See :ref:`iplotx-demo`.

.. dropdown:: 🆕 Cogent3 implements plugin hooks 🔌🪝🎉 

    We have implemented the infrastructure to support hook-style plugins. For example, the ``Alignment.quick_tree()`` method checks for an external plugin for calculation. `piqtree <https://pypi.org/project/piqtree>`_ has implemented support for this.

.. dropdown:: 🆕 Cogent3 supports plugins for reading, writing, storing sequence data 🔌🎉 

    Who doesn't love the myriad of file formats for biological sequences!! Or that sequence collections can now have millions of records!? We now support third-party contributions for reading and writing sequences. We also support alternate storage backends for our sequence collection classes. The `cogent3-h5seqs <https://pypi.org/project/cogent3-h5seqs>`_ project uses HDF5 plus compression for efficient storage of large volumes of sequences. See the docs for an example of how to use :ref:`third-party storage <storage-plugin>`.

.. the ordering of the index items below is critical since it defines the web site header!

.. toctree::
    :hidden:
    :maxdepth: 1

    doc/draw/index
    doc/install
    doc/index
    doc/community

.. toctree::
    :hidden:
    :maxdepth: 1

    doc/licenses
    history
    doc/pycogent
    projects
    doc/data_file_links
    genindex


------

.. rubric:: Citations

.. bibliography:: cogent3.bib
    :filter: docname in docnames
    :style: unsrt

.. _`image gallery`: doc/draw/index.html
