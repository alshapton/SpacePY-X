from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README-pypi.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '1.0.3'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'requests',
    'future; python_version == "2.7"'
    }
]


setup(name='spacexPython',
    version=version,
    description="Simple Python wrapper for the SpaceX API",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='wrapper api spacex',
    author='Andrew Shapton',
    author_email='alshapton@gmail.com',
    url='https://github.com/alshapton/SpaceX-Python',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['spacex-python=spacexpython']
    }
)
