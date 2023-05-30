from setuptools import setup
setup(
    name='pysoi'
    version='1.0',
    author='Cédric Donner',
    description='Tool to facilitate debugging SOI tasks in gitpod',
    long_description='Tool to facilitate debugging SOI tasks in gitpod,
    url='',
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0,,
        'jupyter'
    ],
    package_data={
        'sample': ['sample_data.csv'],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)