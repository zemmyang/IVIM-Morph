from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ivim-morph",
    version="0.0.1",
    install_requires=requirements,
    packages=find_packages(
        where='src',
    ),
    long_description=open('README.md').read(),
    url="https://github.com/TechnionComputationalMRILab/IVIM-Morph",
    package_dir={
        '': 'src',
    },
    include_package_data=True,
)
