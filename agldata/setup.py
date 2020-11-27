import sys
import versioneer
import setuptools

if sys.version_info < (3,6):
    print("agldata requires Python 3.6 or higher please upgrade")
    sys.exit(1)

description = "A python package for data from artificial grammar studies"

setuptools.setup(
    name='agldata',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['agldata', 'agldata.tests', 'datafiles'],
    package_data={'datafiles': ['datafiles/*.yaml']},
    url='',
    license='BSD',
    author='Gabriel Beckers ',
    author_email='g.j.l.beckers@uu.nl',
    description=description, requires=['pyyaml']
)
