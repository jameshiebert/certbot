from setuptools import setup
from setuptools import find_packages


version = '0.1.0.dev0'

install_requires = [
    'letsencrypt=={0}'.format(version),
    'letsencrypt-apache=={0}'.format(version),
    'letsencrypt-nginx=={0}'.format(version),
    'docker-py',
    'mock<1.1.0',  # py26
    'zope.interface',
]

setup(
    name='letsencrypt-compatibility-test',
    version=version,
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'letsencrypt-compatibility-test = letsencrypt_compatibility_test.test_driver:main',
        ],
    },
)
