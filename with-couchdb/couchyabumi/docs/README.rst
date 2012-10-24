====================================================
 watchcat couchyabumi is photo uploader to CouchDB.
====================================================

This tool is posting photos taken by motion(*) to CouchDB.
"watchcat" is the name that is I monitor for a cat as my pet, "yabumi" is method sending a letter to with a bow and arrow, the spell is "矢文" in Japanese.


Requirements
------------

* Python 2.6 and over
* python-magic 5.04 and over
* python-couchdb 0.8 and over

Setup
-----

Install Debian packages that couchyabumi dpends on
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

couchyabumi depends on python-magic and python-couchdb. Install these packages::

  $ sudo apt-get instal python-magic python-couchdb

couchyabmi uploads photos that are taken by motion. So you should install motion and prepare web camera.::

  $ sudo apt-get install motion

Install couchyabumi
^^^^^^^^^^^^^^^^^^^

Install that choosing with one of three ways.

from source
"""""""""""
::

   $ git clone https://github.com/CouchDB-JP/watchcat.git
   $ cd with-couchdb/couchyabumi
   $ sudo python setup.py install

PyPI
""""
::

   $ pip install couchyabumi

Debian package
""""""""""""""

Not ye official package, then download python-couchyabumi-x.x_all.deb from https://www.palmtb.net/deb/c/ and install with dpkg command.::

  $ wget https://www.palmtb.net/deb/c/python-couchyabumi_x.x-x_all.deb
  $ sudo dpkg -i python-couchyabumi_x.x-x_all.deb

Set up couchyabumi
^^^^^^^^^^^^^^^^^^

The configuration file of couchyabumi is ~/.couchyabumirc by default.
The format is follows.::

  {
      "motion": {
          "photodir": "/var/cache/motion"
      },
      "couchdb": {
          "host": "couchdb.example.org",
	  "port": 5984,
	  "db": "watchcat",
	  "username": "uploader",
	  "password": "password"
      }
  }

Change permission of this file that readable and writable by owner only.::

  $ chmod 600 ~/.couchyabumirc

Run couchyabumi
^^^^^^^^^^^^^^^

Register crontab entry.::

   $ crontab -e
   --
   3-59/15 * * * * /usr/bin/couchyabumi

See also
--------

* `motion` http://motion.sf.net
* `CouchDB` http://couchdb.apache.org/

