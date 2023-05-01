from setuptools import find_packages, setup

setup(
    name='pyspark-examples',
    url='',
    description='Pyspark Application examples.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[
        'Cerberus'
    ],
    extra_requires={
        'test': [
            'pylint',
            'pytest'
        ]
    },
    entry_points={
        'console_scripts': [
        ]
    }
)
