Contributing
------------

To add data from studies or to fix bugs/add functionality, it is best to
use the Github pull request workflow. It is described here:
https://github.com/processing/processing/wiki/Contributing-to-Processing-with-Pull-Requests

To add studies, you create a text file in YAML format following the a `mock example here
<https://github.com/gbeckers/agldata/tree/master/agldata/datafiles/mockexample
.yaml>`__ and place it in the 'datafiles' directory.

Make sure you tell your text editor to use UTF-8 text encoding for your file, if it is not
using that already as default.

Use filenames in the following format, all lowercase (see for examples the `datafiles` directory):

authors_year_journal_suffix.yaml

Mention in the comments section at the beginning of the file:

1) who entered the data and when
2) what the source of that data was
3) who independently reviewed the entered data (if anyone)
4) any updates / fixes


