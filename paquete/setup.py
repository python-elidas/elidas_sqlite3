from setuptools import setup

long = (
    open('README.md').read()
    + '\n' +
    open('LICENSE').read()
    + '\n'
)

setup(
    name='simply_sqlite',
    version='0.1.12',
    description='A simplified version of SQLite3',
    long_description=long,
    long_description_content_type='text/markdown',
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
        'Programming Language :: Python :: 3',
        # SSistema Operativo
        'Operating System :: OS Independent',
    ],
    keywords='SQLite Database',
    author='Oscar Gutierrez',
    author_email='pyro.elidas@gmail.com',
    license='GNU GPLv3',
    packages=['simply_sqlite']
)
