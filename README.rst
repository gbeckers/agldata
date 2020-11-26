=======
agldata
=======

.. contents::

What is agldata?
----------------
A python library for published data from artificial grammar learning or
statistical learning studies. Data can be efficiently accessed in a
structured way, for example to use them for (meta-) analyses.

You can easily add data sets by entering them in a file in a user-friendly
format (`YAML <https://yaml.org/>`__). See `example here
<https://github.com/gbeckers/agldata/tree/master/agldata/datafiles
/wilsonetal_2013_jneurosci.yaml>`__.

Current version is: 0.1.0

Install
-------
agldata depends on Python 3.6 or higher, and one external library (pyaml). As
long as there is no official release I recommend working in Anaconda.

Create an environment::

    $ conda create -n agltest pip python=3.7 jupyterlab git pyyaml=5.1

Switch to this new environment:

Linux and MacOS::

    $ source activate agltest

Windows::

    $ conda activate agltest

Install the agldata master repo::

    $ pip install git+https://github.com/gbeckers//agldata@master


If you want to remove the conda environment later::

    $ conda env remove -n agltest


Contributing
------------
To add data from studies (using the format described below) or to fix
bugs/add functionality, it is best to use a the Github pull request workflow.
It is described here:
https://github.com/processing/processing/wiki/Contributing-to-Processing-with-Pull-Requests

Design considerations
---------------------
We chose YAML as format for data because it is universal and very easy to
write and edit by hand. JSON would have been simpler for installation
reasons as it is included in the standard library, while YAML depends on an
external library, pyyaml. However, JSON requires more brackets etc, making it
more error prone for use by humans who enter data. We want to minimize such
errors.

Included studies
----------------

- `Abe K, Watanabe D (2011) <https://www.nature.com/articles/nn.2869>`__
  Songbirds possess the spontaneous ability to discriminate syntactic rules.
  Nat Neurosci 14:1067–1074.

- `Attaheri A, Kikuchi Y, Milne AE, Wilson B, Alter K, Petkov CI (2015)
  <https://doi.org/10.1016/j.bandl.2014.11.006>`__
  EEG potentials associated with artificial grammar learning in the primate
  brain. Brain and Language 148:74–80.

- `Chen J, Rossum D van, Cate C ten (2014)
  <https://link.springer.com/article/10.1007/s10071-014-0786-4>`__
  Artificial grammar learning in zebra finches and human adults: XYX versus
  XXY. Anim Cogn 18:151–164.

- `Chen J, ten Cate C (2015)
  <https://doi.org/10.1016/j.beproc.2014.09.004>`__ Zebra finches can use
  positional and transitional cues to distinguish vocal element strings.
  Behavioural Processes 117:29–34.

- `Endress AD, Carden S, Versace E, Hauser MD (2010)
  <https://link.springer.com/article/10.1007/s10071-009-0299-8>`__
  The apes’ edge: positional learning in chimpanzees and humans.
  Anim Cogn 13:483–495.

- `Knowlton BJ, Squire LR (1996)
  <http://dx.doi.org/10.1037/0278-7393.22.1.169>`__
  Artificial Grammar Learning Depends on Implicit Acquisition of Both Abstract
  and Exemplar-Specific Information. Journal of Experimental Psychology
  22:169–181.

- `Saffran J, Hauser M, Seibel R, Kapfhamer J, Tsao F, Cushman F (2008)
  <https://doi.org/10.1016/j.cognition.2007.10.010>`__
  Grammatical pattern learning by human infants and cotton-top tamarin
  monkeys. Cognition 107:479–500.

- `Heijningen CAA van, Chen J, Laatum I van, Hulst B van der, Cate C ten (2012)
  <https://link.springer.com/article/10.1007/s10071-012-0559-x>`__
  Rule learning by zebra finches in an artificial grammar learning task:
  which rule? Anim Cogn 16:165–175.

- `Wilson B, Smith K, Petkov CI (2015)
  <https://doi.org/10.1111/ejn.12834>`__
  Mixed-complexity artificial grammar learning in humans and macaque
  monkeys: evaluating learning strategies. Eur J Neurosci 41:568–578.

- `Wilson B, Slater H, Kikuchi Y, Milne AE, Marslen-Wilson WD, Smith K,
  Petkov CI (2013)
  <https://doi.org/10.1523/JNEUROSCI.2414-13.2013>`__
  Auditory Artificial Grammar Learning in Macaque and Marmoset Monkeys. J
  Neurosci 33:18825–18835.

- `Wilson B, Kikuchi Y, Sun L, Hunter D, Dick F, Smith K, Thiele A,
  Griffiths TD, Marslen-Wilson WD, Petkov CI (2015)
  <https://doi.org/10.1523/JNEUROSCI.2414-13.2013>`__
  Auditory sequence processing reveals evolutionarily conserved regions of
  frontal cortex in macaques and humans. Nat Commun 6:8901.

Data format
-----------

See a `mock example here
<https://github.com/gbeckers/agldata/tree/master/agldata/datafiles/mockexample
.yaml>`__
showing how to define data in a yaml file.


Copyright and License
---------------------
:copyright: Copyright 2019-2020 by Gabriel Beckers, Utrecht University.
:license: 3-Clause Revised BSD License, see LICENSE.txt for details.


Contact
-------
Gabriel Beckers, Utrecht University, https://www.gbeckers.nl
