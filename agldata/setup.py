from distutils.core import setup
import versioneer

description = "A python package for data from artificial grammar studies"

setup(
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
