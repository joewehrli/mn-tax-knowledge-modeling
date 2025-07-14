# use: pip install -e .

from setuptools import setup, find_packages

setup(
    name='mn-tax-knowledge-modeling',
    version='0.5',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
