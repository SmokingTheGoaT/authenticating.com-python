from setuptools import find_packages, setup


setup(
    name = 'authenticating.com',
    packages = find_packages(include=['authenticating.com']),
    version = '0.1.0',
    description = 'authenticating.com-python',
    author = 'SmokingGoaT',
    license = 'MIT',
    install_requires = [],
    setup_requires = ['pytest-runner'],
    tests_requires = ['pytests'],
    test_suite = 'tests'
)