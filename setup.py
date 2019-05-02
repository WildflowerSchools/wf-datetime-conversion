from setuptools import setup, find_packages

setup(
    name='datetime_conversion',
    packages=find_packages(),
    version='0.0.1',
    include_package_data=True,
    description='Provides various functions for converting between datetime formats',
    long_description=open('README.md').read(),
    url='https://github.com/WildflowerSchools/datetime_conversion',
    author='Ted Quinn',
    author_email='ted.quinn@wildflowerschools.org',
    install_requires=[
        'pandas==0.24.2',
        'numpy==1.16.2'
    ],
    keywords=['datetime'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
