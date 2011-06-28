#!/usr/bin/python

class Photos:
    '''Listing photo images taken with motion.'''
    def listFiles(self):
        import glob, os.path
        for f in glob.glob("*-??????????????-??-?.jpg"):
            if os.path.isfile(f):
                print f
                self.encodeBase64(f)
                self.encodeJson()
                print self.doc
                

    '''Encoding photo image file to base64 ascii strings.'''
    def encodeBase64(self, filepath):
        import base64
        self.image_base64 = base64.encodestring(open(filepath,"rb").read())

    '''Serialize JSON Document.'''
    def encodeJson(self):
        self.doc = {"image":self.image_base64}



n = Photos()
print n.listFiles()

