from os.path import dirname, join

from setuptools import setup, find_packages



version = '0.7'

setup(
    name = 'cmsplugin-iframe',
    version = version,
    description = "Django CMS Plugin for Iframes",
    long_description = open(join(dirname(__file__), 'README.rst')).read() + "\n" + 
                       open(join(dirname(__file__), 'HISTORY.rst')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"],
    keywords = 'django cms plugin iframe',
    author = 'John Phillips',
    author_email = 'johnphillips@arch.tamu.edu',
    url = 'https://github.com/johnphillips1992/cmsplugin-iframe',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'django-cms>=2.1.0',],
)
