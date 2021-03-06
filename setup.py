import sys
from setuptools import setup

long_description="""
What is Tox?
==========================

Tox as is a generic virtualenv management and test command line tool you can
use for:

* checking your package installs correctly with different
  Python versions and interpreters

* running your tests in each of the
  environments, configuring your test tool of choice

* acting as a frontend to Continous Integration
  servers, greatly reducing boilerplate and merging
  CI and shell-based testing.

For more information, docs and many examples please checkout the `home page`_:

    http://tox.readthedocs.org

.. _`home page`: http://tox.readthedocs.org
"""


def main():
    install_requires=['virtualenv>=1.6.1']
    setup(
        name='tox',
        description='virtualenv-based automation of test activities',
        long_description=long_description,
        url='http://codespeak.net/tox',
        version='1.0.dev4',
        license='GPLv2 or later',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='holger krekel',
        author_email='holger@merlinux.eu',
        packages=['tox', ],
        entry_points={'console_scripts': 'tox=tox:cmdline'},
        install_requires=install_requires+['argparse', 'py>=1.4.0a2', ],
        zip_safe=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
             'Operating System :: POSIX',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: MacOS :: MacOS X',
             'Topic :: Software Development :: Testing',
             'Topic :: Software Development :: Libraries',
             'Topic :: Utilities',
             'Programming Language :: Python',
             'Programming Language :: Python :: 3'],
    )

if __name__ == '__main__':
    main()
