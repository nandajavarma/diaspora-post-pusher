#!/usr/bin/python
from os import listdir
from os.path import isfile, join
import re
from datetime import datetime
from diaspora_pusher import DiasporaPusher

class PushMyPost(DiasporaPusher):
    def __init__(self):
        self.main()

    def main(self):
        mypath = '_posts/'
        files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
        new_post_date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        pattern = '([0-9]*-[0-9]*-[0-9]*)-(.*)\.md'
        for each in files:
            g = re.match(pattern, each)
            if g:
                date = g.group(1)
                date = datetime.strptime(date,'%Y-%m-%d')
                if date > new_post_date:
                    new_post_date = date
                    post = g.group(2)
            else:
                return
        url = "http://gemiam.in/" + post
        DiasporaPusher(url, "https://joindiaspora.com", "nandaja", "password")


PushMyPost()
