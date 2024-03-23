from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ipdetective',
    version='1.0.1',
    description='A Python client for IPDetective API',
    long_description=long_description,
    author='IPDetective',
    author_email='andrew@ipdetective.io',
    project_urls={
        'Homepage': 'https://ipdetective.io',
        'Source': 'https://github.com/AndrewCopeland/ipdetective-client-python'
    },
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
        'Intended Audience :: Developers'
    ],
)