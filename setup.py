# coding: utf-8
from setuptools import setup

setup(
    name='facebook-client',
    version='0.0.1',
    description='Python lib to communicate with facebook graph api',
    author='Bernardo Fontes',
    author_email='bernardoxhc@gmail.com',
    packages=['facebook_client'],
    install_requires=['requests>=2.6.0'],
    zip_safe=True,
    platforms='any',
)
