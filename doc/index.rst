##########################
Making Sense from Sequence
##########################

``cogent3`` is a mature python library for analysis of biological sequence data. We endeavour to provide a first-class experience within Jupyter notebooks, but the algorithms also support parallel execution on compute systems with 1000's of processors. It be used for...

.. tab-set::

    .. tab-item:: Data wrangling

        ``cogent3`` provides an extensive suite of capabilities for manipulating and analysing sequence data. For instance, the ability to `read standard biological data formats <doc/cookbook/manipulating_biological_data.html>`_, manipulate sequences `by their annotations <doc/examples/seq_features.html>`_, to perform multiple sequence alignment (`app docs`_) using any of our substitution models, `phylogenetic reconstruction <doc/examples/index.html#phylogenetic-reconstruction>`_ and tree manipulation, manipulation of `tabular data <doc/cookbook/tables.html>`_, visualisation of phylogenies (`image gallery`_) and much more.

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


📣 New Features & Announcements
===============================

.. dropdown:: 🆕 A new tutorial on using non-stationary amino acid models 🧐

    A new contribution from Peter Goodman and Andrew Wheeler demonstrates how to specify a non-stationary amino acid substitution model. Check it out :ref:`here <nonstationary-model-aa-inference>`. Thanks Peter and Andrew!

.. dropdown:: 🆕 Faster sequence coevolution measures 🚀

    We have completely rewritten all the Mutual Information based coevolution statistic calculators. Single CPU performance is orders of magnitude faster than the old implementation and we now also support parallel execution. The existing ``<alignment>.coevolution()`` method uses these so you don't need to do anything different to use the new algorithms.

.. dropdown:: 🆕 Supporting third-party apps as plugins 🔌

    Cogent3 now provides support for plugins! Third-party developers can deploy their code as cogent3 apps with just a few lines. See the app `demo project <https://github.com/cogent3/app_template>`_ for an example of how easy it is to share your cogent3 apps.

    Please post any questions you have about writing apps or sharing them on `cogent3 discussions <https://github.com/cogent3/cogent3/discussions>`_.

.. dropdown:: 🆕 The developers of Cogent3 and IQ-TREE2 announce piqtree2 🎉

    Speaking of plugins, our first major third-party plugin is `piqtree2 <https://pypi.org/project/piqtree2>`_. Try it out and `give us feedback <https://github.com/iqtree/piqtree2/discussions>`_.

.. dropdown:: 🆕 New core data types improve efficiency and flexibility

    The cogent3 development team 👾 are hard at work modernising cogent3 core objects 💪🛠.

    In this release, the ``Sequence``, ``SequenceCollection``, ``MolType``, ``GeneticCode``, and alphabet classes have all been rewritten from scratch to simplify the code while improving its flexibility and performance. (We're working on alignments for the next release.)

    The "new-style" objects enhance performance by supporting the access of the underlying data in various formats (i.e. ``numpy`` arrays, bytes or strings). You can create "new-style" objects by setting the ``new_type=True`` argument in top-level functions (``make_seq``, ``load_seq``, ``make_unaligned_seqs``, ``get_moltype``, ``get_code``). These are not yet the default and are not fully integrated into the existing code. They can also differ in their API relative to the classes they replace. 

    We encourage experimentation in cases where integration with old objects is NOT required and `look forward to any feedback <https://github.com/cogent3/cogent3/discussions>`_!


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

.. _`app docs`: doc/app/index.html
.. _`image gallery`: doc/draw/index.html
