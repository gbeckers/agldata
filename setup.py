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
    packages=['agldata', 'agldata.tests', 'agldata.datafiles'],
    package_data={'agldata': ['datafiles/*.yaml']},
    url='',
    license='GPL',
    author='Gabriel Beckers ',
    author_email='g.j.l.beckers@uu.nl',
    description=description, requires=['pyyaml']
)
