#!/usr/bin/python
#
# Copyright 2017 KiKe. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

    license='Apache License 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',

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