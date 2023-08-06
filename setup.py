from setuptools import setup, find_packages

#https://stackoverflow.com/a/60211007/656449
setup(
    name='ml_utils',
    version='1.0',
    packages=find_packages(),
    package_dir = { '' : 'src' }
)
