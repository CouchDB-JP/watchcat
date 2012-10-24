# -*- coding: utf-8 -*-
"""
    Copyright (C) 2012 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import magic


def error(msg):
    """Print error message and exit.

    Argument:

        msg: error message
    """
    print("ERROR: %s" % msg)
    #exit(1)


def get_mimetype(filename):
    """Get mimetype of file

    Argument:

        filename: target filename path
    """
    m = magic.open(magic.MAGIC_MIME)
    m.load()
    mimetype = m.file(filename).split('; ')[0]
    return mimetype
