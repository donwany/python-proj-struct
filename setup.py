from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name='FilesForPythonProject',
    version='0.1.0',
    description='Sample package for FilesForPythonProject',
    long_description=readme,
    author='Theophilus S.',
    author_email='theodondre@gmail.com',
    url='https://github.com/donwany/samplemod',
    license=license,
    install_requires=install_requires,
    packages=find_packages(exclude=('tests', 'docs'))
)
