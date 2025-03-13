from setuptools import setup, find_packages

setup(
    name = 'smlogic',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'Collection of tools to aid with making logic creations for the game Scrap Mechanic.',
    long_description = open('README.md').read(),
    install_requires = [],
    url = 'https://github.com/Junkyard-Logic-Studios/Scrap-Mechanic_Logic-Generator',
)
