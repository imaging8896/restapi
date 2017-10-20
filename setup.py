from setuptools import setup, find_packages

setup(
    name='restapi',
    version='2.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    provides=['restapi'],
    install_requires=['setuptools', 'requests']
)