# -*- coding: utf-8 -*-
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0.a1 "Kiwi"  #
#  / / / / / __/ /_/ / // /   (!) by Giovanni Squillero and Alberto Tonda   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!" #
#                                                                           #
#############################################################################

# Copyright 2020 Giovanni Squillero and Alberto Tonda
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools
from microgp import __version__ as ugp_version

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microgp",
    version=ugp_version,

    author="Giovanni Squillero",
    author_email="squillero@polito.it",
    license='Apache-2.0',

    description="A multi-purpose extensible self-adaptive evolutionary algorithm",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/squillero/microgp4",
    keywords='optimization evolutionary-algorithm computational-intelligence',

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        'coloredlogs>=9',
        'networkx>=2.4',
    ],
)
