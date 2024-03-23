from setuptools import setup, find_packages

setup(
    name='ipdetective',
    version='1.0.0',
    description='A Python client for IPDetective API',
    long_description='''This package provides a Python client for retrieving bot and geolocation information for IP addresses using the IPDetective API. It allows users to query various details such as the country code, country name, ASN (Autonomous System Number), and IP Address classification like VPN, Proxy, Datacenter and Bot''',
    author='IPDetective',
    author_email='andrew@ipdetective.io',
    url='https://github.com/AndrewCopeland/ipdetective-client-python',
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