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
import os.path
import re
import base64
import Image
import utils


def encode_base64(image_file):
    """Encoding photo image file to base64 ascii strings.

    Argument:

        image_file: image file path
    """
    image_bin = open(image_file, "rb").read()
    image_name = os.path.basename(image_file)
    image_base64 = base64.encodestring(image_bin)
    mimetype = utils.get_mimetype(image_file)
    return (image_name, image_base64, mimetype)


def generate_thumbnail(image_file):
    """Generating thumbnail.

    Argument:

        image_file: image file path
    """
    thumbnail_file = os.path.splitext(image_file)[0] + "_s.jpg"

    try:
        img = Image.open(image_file, mode='r')
        img.thumbnail([60, 60])
        img.save(thumbnail_file)
        return thumbnail_file

    except IOError as e:
        utils.error(e)


def get_date(filename):
    """Getting date info from filename.

    Argument:

        filename: image file name (not path)
    """
    pat_filename = re.compile('(\d+)-(\d+)-(\d+)-(\d).jpg')
    pat_datetime = re.compile('^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})')

    try:
        datetime_str = pat_filename.match(filename).group(2)
        t = pat_datetime.match(datetime_str)

        year = t.group(1)
        mon = t.group(2)
        mday = t.group(3)
        hour = t.group(4)
        minute = t.group(5)
        sec = t.group(6)
        return (year, mon, mday, hour, minute, sec)

    except AttributeError as e:
        utils.error(e)


def generate_dict(image, thumbnail, timeinfo):
    """Generate dict as document.

    Arguments:

        image: image tuple (filename, base64 encoded, mimetype)
        thumnail: thumbnail tuple (filename, base64 encoded, mimetype)
        timeinfo: datetime tuple (year, mon, mday, hour, min, sec)
    """
    doc_dict = {
        "year": timeinfo[0],
        "mon": timeinfo[1],
        "mday": timeinfo[2],
        "hour": timeinfo[3],
        "min": timeinfo[4],
        "sec":  timeinfo[5],
        "photo": image[0],
        "thumbnail": thumbnail[0],
        "_attachments": {
            image[0]:
                {
                "content_type": image[2],
                "data": image[1]
                },
            thumbnail[0]:
                {
                "content_type": thumbnail[2],
                "data": thumbnail[1]
                }
            }
        }
    return doc_dict
