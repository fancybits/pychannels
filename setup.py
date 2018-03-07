from distutils.core import setup

setup(
    name='pychannels',
    version="0.2.6",
    packages=['pychannels',],
    license='The MIT License',
    description = 'API client for the Channels app - https://getchannels.com',
    author = 'Fancy Bits, LLC',
    author_email = 'jon@getchannels.com',
    url = 'https://github.com/fancybits/pychannels',
    keywords = ['api', 'client', 'channels', 'automation'],
    install_requires=['requests>=2.0'],
    zip_safe=True
)
