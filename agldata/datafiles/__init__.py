import yaml
from pathlib import Path

__all__ = ['get_datadict', 'availablestudies']

datadir = Path(__file__).parent
datafiles = [datafile for datafile in datadir.glob('*.yaml')
             if datafile.stem != 'mockexample']
availablestudies = sorted([datafile.stem for datafile in datafiles])

def get_datadict(study):
    """Returns a dictionary with data from a study thats us included in the
    package. The dictionary should at least contain a 'strings' key. In
    addition it may contain a 'readingframe' key, a 'comparisons' key and a
    'categories' key, and other key-item pairs that are defined in the file.

    Parameters
    ----------
    study: str
        The label of the study. To get a list of the labels of available
        studies, check the `availablestudies' list (see example below).

    Returns
    -------
    dict
        A dictionary containing the study's data.

    Example
    -------
    >>> import agldata as ad
    >>> ad.availablestudies
    ['abe_and_watanabe_2011_natneurosci',
     'abewatanabe_natneurosci_2011',
     'attaheri_etal_2015_brainlanguage',
     'attaherietal_brainlanguage_2015',
     'chenetal_animcogn_2015',
     'chentencate_behproc_2015',
     'endressetal_2010',
     'knowltonsquire_jexppsy_1996',
     'saffranetal_cog_2008',
     'saffranetal_cog_2008_exp5',
     'vanheijningenetal_animcogn_2013',
     'wilsonetal_ejn_2015',
     'wilsonetal_2013_jneurosci',
     'wilsonetal_natcomm_2015']
    >>> d = ad.get_data('wilsonetal_2013_jneurosci')
    >>> d['strings']
    [{'Hab_1': 'acf'},
     {'Hab_2': 'acfc'},
     {'Hab_3': 'acgf'},
     {'Hab_4': 'acgfc'},
     {'Hab_5': 'acgfcg'},
     {'Hab_6': 'adcf'},
     {'Hab_7': 'adcfc'},
     {'Hab_8': 'adcfcg'},
     {'Hab_9': 'adcgf'},
     {'Fam_1': 'acgfc'},
     {'Fam_2': 'adcfcg'},
     {'Novel_1': 'acfcg'},
     {'Novel_2': 'adcgfc'},
     {'Viol_bA_1': 'afgcd'},
     {'Viol_bA_2': 'afcdgc'},
     {'Viol_nbA_1': 'fadgc'},
     {'Viol_nbA_2': 'dcafgc'}]

    """
    filename = datadir / f'{study}.yaml'
    with open(filename, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)