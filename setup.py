from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


install_requires = [{
    'beautifulsoup4',
    'cachepy',
    'requests',
    'tinydb'
    }
]


setup(name='SpacePY-X',
      version="v1.1.2a1",
      description="Simple Python wrapper for the SpaceX API",
      long_description=README,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      keywords='wrapper api spacex python',
      author='Andrew Shapton',
      author_email='alshapton@gmail.com',
      url='https://github.com/alshapton/SpacePY-X',
      license='MIT',
      packages=find_packages('src'),

      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
        'console_scripts':
            ['spacex-python=spacexpython']
                }
      )
