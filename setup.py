from setuptools import setup, find_packages

setup(
    name='blogdown',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'blogdown=src.blogdown:main'
        ]
    }
)