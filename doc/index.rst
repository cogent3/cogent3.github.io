##########################
Making Sense from Sequence
##########################

``cogent3`` is a mature python library for analysis of biological sequence data. We endeavour to provide a first-class experience within Jupyter notebooks, but the algorithms also support parallel execution on compute systems with 1000's of processors. It be used for...

.. tabbed:: Data wrangling

    ``cogent3`` provides an extensive suite of capabilities for manipulating and analysing sequence data. For instance, the ability to `read standard biological data formats <doc/cookbook/manipulating_biological_data.html>`_, manipulate sequences `by their annotations <doc/examples/seq_features.html>`_, to perform multiple sequence alignment (`app docs`_) using any of our substitution models, `phylogenetic reconstruction <doc/examples/index.html#phylogenetic-reconstruction>`_ and tree manipulation, manipulation of `tabular data <doc/cookbook/tables.html>`_, visualisation of phylogenies (`image gallery`_) and much more.


    .. dropdown:: 🎬 Data wrangling with sequence annotations

        .. video:: https://user-images.githubusercontent.com/3102996/253847297-2611cda8-e078-4b86-a269-43fbf6ced14c.mp4
            :width: 400


.. tabbed:: Modelling molecular evolution

    Differences in the frequency of nucleotides between species is common. In such cases, non-reversible models of sequence evolution are required for robust estimation of important quantities such as branch lengths, or measuring natural selection :cite:`2015.Kaehler.000, 2017.Kaehler.000` (`see using non-stationary models. <doc/app/index.html#the-model-app>`_). We have done more than just invent these new methods, we have established the most robust algorithms :cite:`2008.Schranz.000` for their implementation and their suitability for real data :cite:`2013.Verbyla.000`.

    .. dropdown:: 🎬 Testing a hypothesis involving a non-stationary nucleotide process

        .. video:: https://user-images.githubusercontent.com/3102996/253849611-6ddd8705-8f16-4b24-b651-68b2123ecdf0.mp4
            :width: 400

.. tabbed:: Beginner friendly

    You don't have to be an expert in structural programming languages (like Python) to use ``cogent3``! Interactive usage in Jupyter notebooks and a functional programming style interface lowers the barrier to entry. Individuals comfortable with R should find this interface less complex. (See the ``cogent3.app`` documentation.)

    .. dropdown:: 🎬 Using cogent3 apps

        .. video:: https://user-images.githubusercontent.com/3102996/253849168-a821de1a-1aad-4761-970f-e365f6b3b1cd.mp4
            :width: 400


.. the ordering of the index items below is critical since it defines the web site header!

.. toctree::
    :hidden:
    :maxdepth: 1

    doc/draw/index
    doc/install
    doc/index
    doc/general

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
