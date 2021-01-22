import sys
import versioneer
import setuptools

if sys.version_info < (3,6):
    print("agldata requires Python 3.6 or higher please upgrade")
    sys.exit(1)

description = "A python package for data from artificial grammar studies"

long_description = """
A python library for published data from artificial grammar learning or
statistical learning studies. Data can be efficiently accessed in a
structured way, for example to use them for (meta-) analyses.

A first attempt to documentation can be found here: 
https://agldata.readthedocs.io/

You can easily add data sets by entering them in a file in a user-friendly
format (`YAML <https://yaml.org/>`__). See `example here
<https://github.com/gbeckers/agldata/tree/master/agldata/datafiles
/wilsonetal_2013_jneurosci.yaml>`__.

"""

setuptools.setup(
    name='agldata',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['agldata', 'agldata.tests', 'agldata.datafiles'],
    package_data={'agldata': ['datafiles/*.yaml']},
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/gbeckers/agldata',
    license='GPL',
    author='Gabriel Beckers ',
    author_email='g.j.l.beckers@uu.nl',
    description=description,
    requires=['pyyaml'],
    install_requires=['pyyaml']
)
