from setuptools import setup, find_packages

setup(
    name='wikiparser',
    version='1.0.1',
    description='Wikipedia parser',
    long_description='Simple and best tool to parse wikipedia',
    url='https://github.com/KiranNiranjan/wiki-parser-py',

    # Author details
    author='Kiran Niranjan (KiKe)',
    author_email='kiranleo1992@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='wiki parser html to json wikipedia',

    packages=['wikiparser'],

    install_requires=['bs4', 'requests'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'wikiparser = wikiparser.wikiparser:wiki_parser',
        ],
    },
)