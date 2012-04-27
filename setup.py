from setuptools import setup, find_packages

setup(
    name='cmsplugin-tumblr',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/sclaughl/cmsplugin-tumblr',
    author='Stuart Laughlin',
    author_email='stuart@bistrotech.net',
    description='A django-cms plugin that displays the last number of posts of a tumblr user',
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
