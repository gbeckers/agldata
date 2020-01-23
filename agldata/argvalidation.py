def checkpositiveint(i):
    if not (isinstance(i, int) and (i > 0)):
        raise ValueError("i ({}) should be an int > 0".format(i))

def isvalidstring(s, readingframe=1):
    if isinstance(s, str) \
        and (len(s) >= readingframe) \
        and (len(s) % readingframe == 0):
        return True
    else:
        return False

def checkstring(s, readingframe=1):
    if not (isinstance(s, str) and len(s) >= readingframe):
        raise TypeError("`s` should be a string with at least one "
                        "token (s: {})".format(s))
    if readingframe > 1:
        if not len(s) % readingframe == 0:
            raise ValueError('string "{}" not compatible with '
                             'readingframe of {}'.format(s, readingframe))

