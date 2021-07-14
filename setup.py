from setuptools import setup

long = (
    open('README.md').read()
    + '\n' +
    open('LICENSE').read()
    + '\n'
)

setup(
    name='sqlite_easy',
    version='0.1.1',
    description='A simplified version of SQLite3',
    long_description=long,
    classifiers=[
        # Estabilidad del proyecto:
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Publico Objetivo:
        'Intended Audience :: Developers',
        # Etiqueta:
        'Topic :: Database',
        # Licencia:
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        # Version de Python
        'Progamming Language :: Python :: 3',
        # SSistema Operativo
        'Operating System :: OS Independent',
    ],
    keywords='SQLite Database',
    author='Oscar Gutierrez',
    author_email='pyro.elidas@gmail.com',
    license='GNU GPLv3',
    packages=['sqlite_easy']
)
