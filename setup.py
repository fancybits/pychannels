from setuptools import setup
from os.path import join, dirname
from pathlib import Path

def read(fname):
    """Read content of a file and return as a string."""
    return Path(join(dirname(__file__), fname)).read_text()

setup(
    name='pychannels',
    version="1.2.2",
    packages=['pychannels',],
    license='The MIT License',
    description='API client for the Channels app - https://getchannels.com',
    long_description_content_type='text/markdown',
    long_description=read('README.md'),
    author='Fancy Bits, LLC',
    author_email='jon@getchannels.com',
    url='https://github.com/fancybits/pychannels',
    keywords=['api', 'client', 'channels', 'automation'],
    install_requires=['requests>=2.0'],
    zip_safe=True
)
