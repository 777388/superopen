import sys
import os
class requested:
    def __init__(self, url, source):
        self.url = url
        self.source = source

    def sources(self):
        if (self.source == "wget"):
            os.popen(self.source +" "+ self.url).read()
        elif (self.source == "yt"):
            os.popen(self.source+"fzf " + self.url).read()
        else:
            os.popen(self.source +" "+ self.url).read()

class Insist(requested):
    def __init__(self, url, source):
        super(Insist, self).__init__(url, source)

openup = Insist(sys.argv[1], sys.argv[2])

openup.sources()
            