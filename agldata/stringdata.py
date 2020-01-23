import sys, random
from collections import OrderedDict
from .argvalidation import checkpositiveint, checkstring
from .datafiles import get_datadict


__all__ = ['get_stringdata', 'String']# 'StringData', 'StringLabelTuple',
# 'StringDict']

class String(str):

    def __init__(self, readingframe=1):

        self._readingframe = readingframe

    @property
    def readingframe(self):
        return self._readingframe




class StringData(object):

    def __init__(self, strings, readingframe=1, categories=None,
                 categorycomparisons=None, categorycolors=None,
                 tokendurations=None, tokenintervalduration=None,
                 anchorsymbol=None):

        self.strings = strings = StringDict(strings,
                                            readingframe=readingframe,
                                            anchorsymbol=anchorsymbol)
        self.readingframe = readingframe
        if categories is None:
            categories = {}
        self.categories = {}
        for l, c in categories.items():
            self.categories[l] = StringLabelTuple(c, stringdict=strings)
        if categorycomparisons is None:
            categorycomparisons = (('All', 'All'),)
        self.categorycomparisons = categorycomparisons
        self.tokendurations = tokendurations
        self.tokenintervalduration = tokenintervalduration
        categorycolors = {} if categorycolors is None else categorycolors
        self.stringlabelcolors = {}
        for category, color in categorycolors.items():
            for sl in self.categories[category]:
                self.stringlabelcolors[sl] = color
        for label, string in self.strings.items():
            if label not in self.stringlabelcolors:
                self.stringlabelcolors[label] = 'black'
        if 'All' not in self.categories:
            l = list(self.strings.keys())
            self.categories['All'] = StringLabelTuple(l, stringdict=strings)

    def __getitem__(self, item):
        return self.categories[item]

    def __str__(self):

        lines = [str(self.strings)]
        lines.append('Categories:\n')
        for category, strt in self.categories.items():
            if not category == 'All':
                lines.append('    {}: {}\n'.format(category, strt))
        return ''.join(lines)

    __repr__ = __str__


# make sure the input is a dict
class StringDict(OrderedDict):
    """
    An ordered dictionary of string key to token string value mappings.

    StringDict() -> new empty dictionary
    StringDict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    StringDict(iterable) -> new dictionary initialized as (key, value)
        pairs, if possible. If the iterable just generates python strings,
        then initialized as (string, string) pairs, so that a string value
        becomes a key to itself.
    StringDict(**kwargs) -> new dictionary initialized with the label= string
        pairs in the keyword argument list.
        For example:  TokenStrings(A='abcd', B='efgh')

    Additional parameters
    ---------------------
    readingframe: positive, nonzero int, default 1
        The number of characters that make up one string token. This will
        often be `1`, so that, e.g. the string "abcd" has 4 tokens. However if
        there are more tokens than can be coded in ascii symbols,
        the larger readingframes are the solution. E.g., if readingframe is 2,
        then "a1a2" has two tokens, namely "a1" and "a2".


    """

    def __init__(self, *args, readingframe=1, anchorsymbol=None, **kwargs):
        checkpositiveint(readingframe)
        self._readingframe = readingframe
        try:
            super().__init__(*args, **kwargs)
        except ValueError:
            seq = args[0]
            if isinstance(seq[0], dict):  # a list of 1-item dictionaries
                super().__init__(tuple(d.items())[0] for d in seq)
            else:  # a sequence of string values, no keys
                super().__init__([(s, s) for s in seq])
        # use our string subclass
        for key, item in self.items():
            if anchorsymbol is not None:
                item = f'{anchorsymbol}{item}{anchorsymbol}'
            self[key] = String(item)

    @property
    def readingframe(self):
        return self._readingframe

    def __setitem__(self, key, value):
        checkstring(value, readingframe=self._readingframe)
        super().__setitem__(key, value)

    def __str__(self):
        maxlabellen = max(map(len, tuple(self.keys())))
        lines = ['Readingframe: {}\n'.format(self.readingframe)]
        lines.append('Strings: \n')
        for l, s in self.items():
            lines.append('    {:<{fill}}: {}\n'.format(l, s,
                                                       fill=maxlabellen + 1))
        return ''.join(lines)


class StringLabelTuple(object):
    def __init__(self, strings, stringdict=None, readingframe=None):
        stringlabels = tuple(strings)
        if stringdict is not None:
            if not set(stringlabels).issubset(stringdict):
                raise ValueError('Not all strings are in stringdict')
            if readingframe is not None:
                if readingframe != stringdict.readingframe:
                    raise ValueError(
                        "`readingframe` not compatible with `stringdict`")
            readingframe = stringdict.readingframe
        else:
            if readingframe is None:
                readingframe = 1
        self._stringdict = stringdict
        self._labels = stringlabels
        self._readingframe = readingframe

    @property
    def readingframe(self):
        return self._readingframe

    def __iter__(self):
        if self._stringdict:  # labels are different from strings
            for l in self._labels:
                yield (l, self._stringdict[l])
        else:  # the strings are identical to labels
            for l in self._labels:
                yield (l, l)

    def __getitem__(self, item):
        items = self._labels[item]
        if not isinstance(items, tuple):
            items = (items,)
        return StringLabelTuple(items, stringdict=self._stringdict)

    def __str__(self):
        return str(self._labels)

    def __repr__(self):
        return '<stringlabeltuple: {}>'.format(self._labels)

    def strings(self):
        return tuple((self._stringdict[l] for l in self._labels))

    def labels(self):
        return self._labels

    def items(self):
        return tuple((l, s) for l, s in self)


def get_stringdata(study, anchorsymbol=None):
    """Returns a dictionary with at least a 'strings' key. In addition it may
    contain a 'readingframe' key, a 'comparisons' key and a 'categories' key,
    and anything you defined in that file.

    """
    return StringData(**get_datadict(study), anchorsymbol=anchorsymbol)


def _get_random(randomseed=None):
    if randomseed is None:
        randomseed = random.randrange(sys.maxsize)
    return random.Random(randomseed)

def shuffled(seq, randomseed=None):
    seqc = [s for s in seq] # make copy
    _get_random(randomseed=randomseed).shuffle(seqc)
    return seqc



def stimuli_wilsonetal_2013_jneurosci(randomseed=None, anchorsymbol=None):

    """Returns a string sequence to model the stimulus sequences in the
    study: "Wilson B, Slater H, Kikuchi Y, Milne AE, Marslen-Wilson WD,
    Smith K, Petkov CI (2013) Auditory Artificial Grammar Learning in Macaque
    and Marmoset Monkeys. J Neurosci 33:18825–18835."

    The sequence is what a single individual monkey received.

    Parameters
    ----------
    randomseed

    Returns
    -------
    dict
      A dictionary with info on stimulus sequence.

    """

    # Macaques:
    # *Habituation* was done as follows: 9 strings per minute, inter-string
    # interval was 4 s. For the duration of 2 hours in the afternoon the day
    # before testing, and 10 min. immediately before testing (see 'Habituation
    # phase' on page 18828). Hence each subject heard 9 * 60 * 2 = 1080 (afternoon
    # day before) and then 10 * 9 = 90 (just before test) habituation strings.
    # In total: 1170. There are 9 habituation strings, so each one was played 130
    # times.
    #
    # *Testing* was done as follows: randomly selected test string of the eight
    # (correct or violation; see below Fam, Novel and Viol strings) strings was
    # individually presented (4 times each, for a total of 32 testing trials; at
    # an average rate of 1/min; interstring intervals ranged between 45 and
    # 75 s).
    #
    # Marmosets:
    # "Four marmosets were available for study, thus, to obtain sufficient data
    # for analysis they were each tested four times. Each testing run was
    # separated by at least 1 week and followed an identical procedure to the
    # macaque experiment, including a habituation and testing phase."

    sd = get_stringdata('wilsonetal_2013_jneurosci', anchorsymbol=anchorsymbol)
    habstrings = list(sd.categories['Hab'].strings())
    habstim = shuffled(habstrings * 130, randomseed=randomseed)
    hablabel = ['Hab'] * len(habstim)
    teststim = []
    testlabel = []
    for testcategory in ('Fam', 'Novel', 'ViolbA', 'ViolnbA'):
        strings = sd.categories[testcategory].strings()
        teststim.extend(strings * 4)
        testlabel.extend([testcategory] * len(strings) * 4)
    # shuffle the sequence
    testlabel, teststim = zip(*shuffled(zip(testlabel, teststim),
                                          randomseed=randomseed))
    return {'category': hablabel + list(testlabel),
            'string': habstim + list(teststim)}


#FIXME numbers in exposure and test are not clear from paper
def stimuli_attaheri_etal_2015_brainlanguage(randomseed=None):

    # stimulus delivery, from the paper:
    # "During the first phase of the experiment the animals
    # were exposed for 30 min with the exemplary consistent AG
    # sequences (Suppl. Fig. S2A). The exposure phase was followed by
    # a ~30 min testing phase (240 completed test sequence trials)
    # where randomly selected consistent and violation testing
    # sequences were individually presented (Suppl. Figs. S1–2)."

    # unfortunately the paper is not clear on the exact number of exposure
    # stimuli. according to suppl info they were randomized.
    # it is probably reasonable to assume there are 240 exposure stimuli (
    # 8 strings), so every string 30 times.
    #


    sd = get_stringdata('attaheri_etal_2015_brainlanguage')
    expstrings = list(sd.categories['Exposure'].strings())
    expstim = shuffled(expstrings * 30, randomseed=randomseed)

    constrings = list(sd.categories['Consistent'].strings())
    violstrings = list(sd.categories['Violating'].strings())
    teststrings = constrings + violstrings
    teststim = shuffled(teststrings * 15, randomseed=randomseed)
    return expstim, teststim

# old code from here; should we be able to save stringdata?

# def save_stringdata(string_data, filename):
#     """
#     Saves a stringData class as a yaml file.
#
#     """
#     # d = StringData(**string_data)
#     string_list = []
#     for string in string_data.strings:
#         string_list.append({string: string})
#
#     stringcategories_list = {}
#     string_types = {'Training': ['Train'], 'Testing': []}
#     for category, items in string_data.stringcategories.items():
#         if category is 'All':
#             pass
#         else:
#             string_types['Testing'].append(category)
#             stringcategories_list[category] = items
#
#     yaml_dict = {'readingframe': string_data.readingframe,
#                  'strings': string_list,
#                  'stringcategories': stringcategories_list,
#                  'string_types': string_types}
#
#     if '.yaml' not in filename:
#         filename += '.yaml'
#     with open(filename, 'w') as yaml_file:
#         yaml.dump(yaml_dict, yaml_file, default_flow_style=None)

