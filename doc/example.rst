Example usage
=============

.. code:: python

    >>> import agldata
    >>> agldata.availablestudies
    ['abe_and_watanabe_2011_natneurosci',
     'attaheri_etal_2015_brainlanguage',
     'chenetal_2015_animcogn',
     'chentencate_2015_behproc',
     'endressetal_2010_animcogn',
     'knowltonsquire_1996_jexppsy',
     'saffranetal_2008_cog',
     'saffranetal_2008_cog_exp5',
     'vanheijningenetal_2013_animcogn',
     'wilsonetal_2013_jneurosci',
     'wilsonetal_2015_ejn',
     'wilsonetal_2015_natcomm']
    >>> s = agldata.get_stringdata('wilsonetal_2013_jneurosci')
    >>> print(s)
    Readingframe: 1
    Strings:
        Hab_1      : acf
        Hab_2      : acfc
        Hab_3      : acgf
        Hab_4      : acgfc
        Hab_5      : acgfcg
        Hab_6      : adcf
        Hab_7      : adcfc
        Hab_8      : adcfcg
        Hab_9      : adcgf
        Fam_1      : acgfc
        Fam_2      : adcfcg
        Novel_1    : acfcg
        Novel_2    : adcgfc
        Viol_bA_1  : afgcd
        Viol_bA_2  : afcdgc
        Viol_nbA_1 : fadgc
        Viol_nbA_2 : dcafgc
    Categories:
        Hab: ('Hab_1', 'Hab_2', 'Hab_3', 'Hab_4', 'Hab_5', 'Hab_6', 'Hab_7', 'Hab_8', 'Hab_9')
        Test: ('Fam_1', 'Fam_2', 'Novel_1', 'Novel_2', 'Viol_bA_1', 'Viol_bA_2', 'Viol_nbA_1', 'Viol_nbA_2')
        Fam: ('Fam_1', 'Fam_2')
        Novel: ('Novel_1', 'Novel_2')
        ViolbA: ('Viol_bA_1', 'Viol_bA_2')
        ViolnbA: ('Viol_nbA_1', 'Viol_nbA_2')
    >>>hab = s['Hab']
    >>>hab
    <stringlabeltuple: ('Hab_1', 'Hab_2', 'Hab_3', 'Hab_4', 'Hab_5', 'Hab_6', 'Hab_7', 'Hab_8', 'Hab_9')>