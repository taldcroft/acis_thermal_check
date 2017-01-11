#!/usr/bin/env python
from setuptools import setup
import glob
from acis_thermal_check import __version__

templates = glob.glob("templates/*")

setup(name='acis_thermal_check',
      packages=["acis_thermal_check"],
      version=__version__,
      description='ACIS Thermal Model Library',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/acis_thermal_check',
      download_url='https://github.com/acisops/acis_thermal_check/tarball/1.2.0',
      data_files=[('templates', templates)],
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      ],
      )
