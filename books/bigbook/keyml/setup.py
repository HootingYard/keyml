from setuptools import setup

setup(
    name='keyml',
    version='1.0.0',
    description='Tests that XHTML files are in the "KeyML" subset.',
    author='',
    author_email='',
    url='https://github.com/hootingyard/',
    entry_points={
        'console_scripts': [
            'keyml=keyml:main',
        ],
    },
    install_requires=[
        'pillow',
        'lxml',
    ],
    long_description=open('keyml.md').read(),
    long_description_format='markdown',
)
