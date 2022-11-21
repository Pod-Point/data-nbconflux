import versioneer
from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        long_description = f.read()
except:
    long_description = ''
    print('Failed to load README.md as long_description')

setup(
    name='nbconflux',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Converts Jupyter Notebooks to Atlassian Confluence (R) pages using nbconvert',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Valassis Digital',
    url='https://github.com/vericast/nbconflux',
    platforms=['Linux', 'Mac OSX', 'Windows'],
    packages=find_packages(),
    python_requires='>=3.9',
    include_package_data = True,
    license='BSD 3-Clause',
    entry_points = {
        'console_scripts': [
            'nbconflux = nbconflux.cli:main'
        ]
    },
    install_requires=[
        'bleach==5.0.1',
        'nbconvert==7.2.5',
        'requests==2.28.1',
        'traitlets==5.5.0',
        'html5lib==1.1',
    ],
)
