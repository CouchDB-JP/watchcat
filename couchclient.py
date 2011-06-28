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
        import re
        j = re.match('^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})',
                     re.match('(\d+)-(\d+)-(\d+)-(\d).jpg', self.filename)
                     .group(2))
        self.year = j.group(1)
        self.month = j.group(2)
        self.date = j.group(3)
        self.hour = j.group(4)
        self.minute = j.group(5)
        self.second = j.group(6)

    '''Serialize JSON Document.'''
    def encodeJson(self):
        self.doc = {
            "filename":self.filename,
            "image":self.image_base64,
            "year":self.year,
            "month":self.month,
            "date":self.date,
            "hour":self.hour,
            "minute":self.minute,
            "second":self.second
            }



n = Photos()
print n.listFiles()

