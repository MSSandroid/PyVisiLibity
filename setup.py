#!/usr/bin/env python
# PyVisiLibity: a Python binding of VisiLibity1
# Copyright (C) 2018 Yu Cao < University of Southampton> Yu.Cao at soton.ac.uk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, Extension
from setuptools.command.build import build


class CustomBuild(build):
    sub_commands = [
        ('build_ext', lambda self: True),
        ('build_py', lambda self: True),
        ('build_clib', lambda self: True),
        ('build_scripts', lambda self: True),
    ]
    
module = Extension('_visilibity', swig_opts=['-c++'],
                   sources=['visilibity.i', 'visilibity.cpp'],
                   include_dirs=['.'])  # Assuming 'visilibity.hpp' is in the current directory


setup (name = 'VisiLibity',
       version = '1.0.10',
       cmdclass = {'build': CustomBuild},
       author = 'Yu Cao',
       author_email = 'yu.cao@soton.ac.uk',
       license = 'LGPL',
       url = 'https://github.com/tsaoyu/PyVisiLibity',
       description = 'Python bindings of VisiLibity1',
       py_modules = ['visilibity'],
       ext_modules = [module])
