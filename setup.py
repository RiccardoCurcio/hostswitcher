import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR, 'hostswitcher')

version = None
exec(open('hostswitcher/version.py').read())

requirements = [
    'termcolor',
    'colorama'
]

setup(
    name="hostswitcher",
    version=version,
    author = "Riccardo Curcio, Angelo Landino, Giuseppe Iannelli",
    author_email = "curcioriccardo@gmail.com,angelolandino@hotmail.it,me@giuseppeiannelli.it",
    description="Multiplatform hosts file manager",
    url='https://github.com/riccardocurcio/hostswitcher',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3',
    py_modules=['hostswitcher'],
    entry_points={
        'console_scripts': [
            'hostswitcher=hostswitcher:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)


## TO PUSH ON PYPI
# python3 setup.py build sdist upload --sign
# python3 setup.py bdist_wheel --python-tag 3 upload --sign
# python3 setup.py build bdist_egg upload --sign