"""Obviously not finished yet."""
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

print(readme)

setup(
    name='pypokelib',
    version='0.2.0',
    description='A Python library for Pokemon',
    package_dir={'': 'pypokelib'},                            # !
    packages=find_packages(where='pypokelib'),                # !  
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/julius-alexander/pypokelib',                                             # ! 
    author='John Garzon-Ferrer',
    author_email="jgarzonferrer@gmail.com",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Role-Playing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='pokemon',
    python_requires='>=3.11',
)