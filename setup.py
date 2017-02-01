# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='remind',
    version='0.1.0',
    description='A terminal based TODO task manager and reminder',
    long_description=readme,
    author='Nitin Choudhary',
    author_email='nitin.iitkgp23@gmail.com',
    url='https://github.com/nitinkgp23/remind',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
