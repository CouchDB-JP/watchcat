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
import glob
import os.path
import json
import encoder


def get_bulk_docs_photos(photo_dir):
    """Getting bulk_docs of Listing photo images taken with motion.

    Argument:

        photo_dir: directory path of photo images taken with motion
    """
    if photo_dir.rfind('/') != len(photo_dir) + 1:
        photo_dir += '/'
    photo_files = photo_dir + "[0-9]*-[0-9]*-[0-9]*-[0-9].jpg"

    docs = []
    for image_file in glob.glob(photo_files):
        if os.path.isfile(image_file):

            # generating thumbnail from original photo.
            thumbnail_file = encoder.generate_thumbnail(image_file)

            # encoding original photo file in base64.
            image = encoder.encode_base64(image_file)

            # encoding thumbnail photo file in base64.
            thumbnail = encoder.encode_base64(thumbnail_file)

            # getting photo timestamp.
            datetime_info = encoder.get_date(image[0])

            # generating dictionary object.
            doc = encoder.generate_dict(image, thumbnail, datetime_info)

            # append doc of photo to dictionary object as all_doc.
            docs.append(doc)

            # remove jpg files.
            #os.remove(image_file)
            #os.remove(thumbnail_file)

    if docs:
        # generate json as bulk_docs for CouchDB.
        return serialize_json(docs)


def serialize_json(docs):
    """Serializing JSON for bulk_docs.

    Argument:

        docs: documents dictionary for Bulk docs
    """
    bulk_docs = json.JSONEncoder().encode({
            "all_or_nothing": "true",
            "docs": docs
            })
    return bulk_docs
