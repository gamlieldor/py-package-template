from setuptools import setup, find_packages

setup(
    name='py-package',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.rst').read(),
    install_requires=[],
    url='https://github.com/gamlieldor/py-package',
    author='Dor Gamliel',
    author_email='gamlieldor@gmail.com'
)