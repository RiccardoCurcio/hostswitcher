import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR, 'hostswitcher')

version = None
exec(open('hostswitcher/version.py').read())

requirements = [
    'termcolor'
]

setup(
    name="hostswitcher",
    version=version,
    author = "Riccardo Curcio, Angelo Landino, Giuseppe Iannelli",
    author_email = "curcioriccardo@gmail.com,angelolandino@hotmail.it,me@giuseppeiannelli.it",
    description="Multiplatform hosts file manager",
    url='https://github.com/giuseppeiannelli/hostswitcher',
    packages=find_packages(),
    install_requires=requirements,
    py_modules=['hostswitcher'],
    entry_points={
        'console_scripts': [
            'hostswitcher=hostswitcher:main',
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
