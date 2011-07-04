#!/usr/bin/python

class Photos:
    '''getting bulk_docs of Listing photo images taken with motion.'''
    def getBulkDocsOfPhotos(self):
        import glob, os.path

        self.docs = []
        for self.filename in glob.glob("*-??????????????-??-?.jpg"):
            if os.path.isfile(self.filename):
                self.image_base64 = self.encodeBase64(self.filename)
                self.getDate()
                self.generateThumbnail()
                self.thumbnail_base64 = self.encodeBase64(self.thumbnail_name)
                #self.thumbnail_base64 = self.encodeBase64_hoge(self.hoge)
                self.generateDict()
                self.docs.append(self.doc)
        self.serializedJson()


    def serializedJson(self):
        import json
        self.bulk_docs = json.JSONEncoder().encode({
                "all_or_nothing":"true",
                "docs":self.docs
                })

    '''Encoding photo image file to base64 ascii strings.'''
    def encodeBase64(self, image):
        import base64
        return base64.encodestring(open(image,"rb").read())

    def encodeBase64_hoge(self, image):
        import base64
        return base64.encodestring(image)


    '''Generating thumbnail.'''
    def generateThumbnail(self):
        import Image, os
        '''
        self.thumbnail = Image.open(self.filename,mode='r')
        self.hoge = str(self.thumbnail.thumbnail([60,60]))
        '''
        image = Image.open(self.filename,mode='r')
        image.thumbnail([60,60])
        self.thumbnail_name = os.path.splitext(self.filename)[0] + "_s.jpg"
        image.save(self.thumbnail_name)


    '''Getting date info from filename.'''
    def getDate(self):
        import re,os,time

        '''get epoctime of file mtime, and convert struct_time of localtime.'''
        t = time.localtime(os.path.getmtime(self.filename))
        self.year = t.tm_year
        self.mon = t.tm_mon
        self.mday = t.tm_mday
        self.hour = t.tm_hour
        self.min = t.tm_min
        self.sec = t.tm_sec


    '''generate dict as document.'''
    def generateDict(self):
        self.doc = {
            "year":self.year,
            "mon":self.mon,
            "mday":self.mday,
            "hour":self.hour,
            "min":self.min,
            "sec":self.sec,
            "_attachments":{
                self.filename:
                    {
                    "content_type":"image/jpeg",
                    "data":self.image_base64
                    },
                self.thumbnail_name:
                    {
                    "content_type":"image/jpeg",
                    "data":self.thumbnail_base64
                    }
                }
            }


    '''serializing JSON'''
    


n = Photos()
n.getBulkDocsOfPhotos()
print n.bulk_docs
