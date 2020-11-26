import sys, random
from collections import OrderedDict
from .argvalidation import checkpositiveint, checkstring
from .datafiles import get_datadict


__all__ = ['get_stringdata', 'get_data', 'String', 'StringDict', 'StringData',
           'StringLabelTuple']

# FIXME use properties instead of methods whenever possible

class String(str):
    """A sequence of tokens.

    For efficiency reasons this is implemented as a subclass of Python str,
    with added `readingframe` and `tokens` attributes. The reading frame
    determines how many characters make up one token.

    Note that all methods are inherited from str and return str objects, not
    String objects. Most inherited methods do not respect the `readingframe`
    of the string, and operate on python string characters.

    Parameters
    ----------
    value: object
        Object to be interpreted as an agldata String.
    readingframe: positive, nonzero int, default None
        The number of characters that make up one string token. This will
        often be `1`, so that, e.g. the string "abcd" has 4 tokens. However if
        there are more tokens than can be coded in one character position,
        larger readingframes are the solution. E.g., if readingframe is 2,
        then "a1a2" has two tokens, namely "a1" and "a2". If this parameter is
        `None`, the readingframe will be taken from `value` if that has a
        readingframe, and if it doesn't it will default to 1.

    """

    @staticmethod
    def _is_valid(value, readingframe):
        return (len(value) % readingframe) == 0

    def __new__(cls, value, readingframe=None):
        if readingframe is None:
            readingframe = getattr(value, 'readingframe', 1)
        if readingframe != getattr(value, 'readingframe', readingframe):
            raise ValueError(f"`readingframe` parameter ({readingframe}) "
                             f"does not match that of `value` ({value.readingframe})")
        if not cls._is_valid(value, readingframe):
            raise ValueError(f"The length of '{value}' ({len(value)}) is not "
                             f"compatible with a reading frame of {readingframe}")
        return super().__new__(cls, value)

    def __init__(self, value, readingframe=None):
        if readingframe is None:
            readingframe = getattr(value, 'readingframe', 1)
        if readingframe != getattr(value, 'readingframe', readingframe):
            raise ValueError("`readingframe` parameter does not match that of `value`")
        checkpositiveint(readingframe)
        self.__readingframe = readingframe

    @property
    def readingframe(self):
        """The number of characters that make up one string token. Normally 1,
        so that, e.g. the string "abcd" has 4 tokens. However if there exist
        many tokens, these can be coded with multiple ascii symbols. E.g., if
        readingframe is 2, then "a1a2" has two tokens, namely "a1" and "a2"."""
        return self.__readingframe

    @property
    def tokens(self):
        """The set of fundamental units that the string consists of. If the
        `readingframe` is 1, then this would be {'a', 'b', 'c', 'd'} in the case
        of an "abcd" string. If `readingframe` is 2, then this would be
        {'ab', 'cd'}"""
        return set([self[i:i + self.__readingframe]
                    for i in range(0, len(self), self.__readingframe)])


class StringDict(OrderedDict):
    """
    An ordered dictionary of string label to token string mappings.

    This is handy when strings are long and are easiest referred to by a
    label, or when a label is more descriptive:E.g. {'hab1': 'ababcbaba',
    'hab2': 'aacbbb'}. The dictionary can be created in the way they are
    normally created in Python, but you can also just provide a sequence
    or set of strings, in which case the labels of the strings will be the
    same as the strings themselves.

    StringDict() -> new empty dictionary
    StringDict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    StringDict(iterable) -> new dictionary initialized as (key, value)
        pairs, if possible. If the iterable just generates python strings,
        then initialized as (string, string) pairs, so that a string value
        becomes a key to itself.
    StringDict(**kwargs) -> new dictionary initialized with the label= string
        pairs in the keyword argument list.
        For example:  StringDict(A='abcd', B='efgh')

    Additional parameters
    ---------------------
    readingframe: positive, nonzero int, default 1
        The number of characters that make up one string token. This will
        often be `1`, so that, e.g. the string "abcd" has 4 tokens. However if
        there are more tokens than can be coded in ascii symbols,
        the larger readingframes are the solution. E.g., if readingframe is 2,
        then "a1a2" has two tokens, namely "a1" and "a2". The readingframe of
        all strings should be identical.


    """

    def __init__(self, *args, readingframe=None, anchorsymbol=None, **kwargs):
        self.__readingframe = readingframe # to be set later if None, need it now for empty dict
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
            self[key] = String(item, readingframe=readingframe)
            if readingframe is None: # we use the one on the string
                readingframe = self[key].readingframe
        self.__readingframe = readingframe

    @property
    def readingframe(self):
        """The number of characters that make up one string token. Normally 1,
        so that, e.g. the string "abcd" has 4 tokens. However if there exist
        many tokens, these can be coded with multiple ascii symbols. E.g., if
        readingframe is 2, then "a1a2" has two tokens, namely "a1" and "a2"."""
        return self.__readingframe

    @property
    def tokens(self):
        """The set of fundamental units that the strings in the dictionary
        consist of. If the `readingframe` is 1, then this would be
        {'a', 'b', 'c', 'd'} in the case of an "abcd" string. If `readingframe`
        is 2, then this would be {'ab', 'cd'}"""
        t = []
        for key, value in self.items():
            t.extend(value.tokens)
        return set(t)

    def __setitem__(self, key, value):
        value = String(value, readingframe=self.__readingframe)
        self.__readingframe = value.readingframe # in case it was None
        super().__setitem__(key, value)

    def __str__(self):
        maxlabellen = max(map(len, tuple(self.keys())))
        lines = ['Readingframe: {}\n'.format(self.readingframe)]
        lines.append('Strings: \n')
        for l, s in self.items():
            lines.append('    {:<{fill}}: {}\n'.format(l, s,
                                                       fill=maxlabellen + 1))
        return ''.join(lines)


class StringLabelTuple:
    """A tuple of token strings, based on their labels.

    Parameters
    ----------
    stringlabels: sequence
         A sequence of labels (python str objects) that refer to token
         strings. The labels should be keys in the stringdict, if provided.
         If stringdict is not provided, then the labels are assumed to be
         identical to the token strings (i.e. 'aba' stands for the token
         sequence (a,b,a).
    stringdict: StringDict
        An agldata StringDict that has the stringlabels as keys and the
        corresponding token strings as values.
    readingframe: positive, nonzero int, default 1
        The number of characters that make up one string token. This will
        often be `1`, so that, e.g. the string "abcd" has 4 tokens. However if
        there are more tokens than can be coded in ascii symbols,
        the larger readingframes are the solution. E.g., if readingframe is 2,
        then "a1a2" has two tokens, namely "a1" and "a2".

    """

    def __init__(self, stringlabels, stringdict=None, readingframe=None):
        stringlabels = tuple(stringlabels)
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
        self.__readingframe = readingframe

    @property
    def readingframe(self):
        return self.__readingframe

    @property
    def tokens(self):
        """The set of fundamental units that the strings in the tuple
        consist of. If the `readingframe` is 1, then this would be
        {'a', 'b', 'c', 'd'} in the case of an "abcd" string. If `readingframe`
        is 2, then this would be {'ab', 'cd'}"""
        t = []
        for s in self.strings():
            t.extend(s.tokens)
        return set(t)

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


class StringData:
    """String data set

    Parameters
    ----------
    strings: StringDict
        It can be a StringDict or anything that is accepted by the StringDict
        class at instantiation.
    readingframe: positive, nonzero int, default 1
        The number of characters that make up one string token. This will
        often be `1`, so that, e.g. the string "abcd" has 4 tokens. However if
        there are more tokens than can be coded in ascii symbols,
        the larger readingframes are the solution. E.g., if readingframe is 2,
        then "a1a2" has two tokens, namely "a1" and "a2".
    categories: dict, optional
        A dictionary of category label to StringLabelTuple mappings.
    categorycomparisons: sequence
        A sequence of category pairs that are to be compared.
    categorycolors: dict
        A dictionary with category to default color mappings. Handy for
        figures or tables, e.g. to give violating strings a particular color
        that matches the one used in a publication.

    """

    def __init__(self, strings, readingframe=None, categories=None,
                 categorycolors=None, categorycomparisons=None,
                 tokendurations=None, tokenintervalduration=None,
                 anchorsymbol=None):

        if isinstance(strings, StringDict):
            if readingframe is None:
                readingframe = strings.readingframe
            else:
                if not readingframe == strings.readingframe:
                    raise ValueError(f"`readingframe` parameter ({readingframe}) "
                                     f"is not the same as reading frame of "
                                     f"strings ({strings.readingframe})")
        elif readingframe is None:
            readingframe = 1
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

    @property
    def tokens(self):
        """The set of fundamental units that the strings in the data
        consist of. If the `readingframe` is 1, then this would be
        {'a', 'b', 'c', 'd'} in the case of an "abcd" string. If `readingframe`
        is 2, then this would be {'ab', 'cd'}"""
        return self.strings.tokens


def get_data(study, anchorsymbol=None):
    """Returns a dictionary with at least a 'strings' key. In addition it may
    contain a 'readingframe' key, a 'comparisons' key and a 'categories' key,
    and anything you defined in that file.

    """
    return StringData(**get_datadict(study), anchorsymbol=anchorsymbol)

# FIXME raise depreciation warning
get_stringdata = get_data

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
