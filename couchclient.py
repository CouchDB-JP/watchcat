#!/usr/bin/python

class Photos:
    '''Listing photo images taken with motion.'''
    def listFiles(self):
        import glob, os.path
        for self.filename in glob.glob("*-??????????????-??-?.jpg"):
            if os.path.isfile(self.filename):
                self.encodeBase64(self.filename)
                self.getDate()
                self.encodeJson()
                print self.doc
                

    '''Encoding photo image file to base64 ascii strings.'''
    def encodeBase64(self, filepath):
        import base64
        self.image_base64 = base64.encodestring(open(filepath,"rb").read())

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

    '''Serialize JSON Document.'''
    def encodeJson(self):
        self.doc = {
            "filename":self.filename,
            "image":self.image_base64,
            "year":self.year,
            "mon":self.mon,
            "mday":self.mday,
            "hour":self.hour,
            "min":self.min,
            "sec":self.sec
            }

        '''serializing JSON'''
        


n = Photos()
print n.listFiles()

