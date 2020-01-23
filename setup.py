from distutils.core import setup
import versioneer

description = "A python package for data from artificial grammar studies"

setup(
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
