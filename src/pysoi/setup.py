from setuptools import setup
setup(
    name='pysoi',
    version='1.0',
    author='Cédric Donner',
    description='Tool to facilitate debugging SOI tasks in gitpod',
    long_description='Tool to facilitate debugging SOI tasks in gitpod',
    url='',
    keywords='competitive programming',
    python_requires='>=3.7, <4',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
    ],
    package_data={
        
    },
    entry_points={
    }
)