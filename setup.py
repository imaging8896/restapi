from setuptools import setup, find_packages

setup(
    name='restapi',
    version='0.6',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    provides=['hamcrest'],
    install_requires=['setuptools', 'requests']
)