#!/usr/bin/python


import diaspy
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re


class DiasporaPusher(object):

    def __init__(self, post_url, pod_url, username, password):
        self.post_url = post_url
        self.pod_url = pod_url
        self.username = username
        self.password = password
        self.post_entry()


    def get_post_title(self):
        b = Browser()
        url = b.open(self.post_url)
        soup = BeautifulSoup(url)
        title, description, tags = '', '', ''
        for meta in soup.findAll("meta"):
            name = meta.get("name")
            if name:
                if "title" in name:
                    title = '<a href="%s">' % self.post_url + meta["content"].strip() + '</a>'
                if name == "description":
                    description = " - " + meta["content"].strip() + "\n"
                if name == "keywords":
                    tags = "tags: " + meta["content"].strip()
        return title + description + tags



    def post_entry(self):
        print('Posting entry to D*')
        c = diaspy.connection.Connection(self.pod_url, self.username, self.password)
        c.login()
        stream = diaspy.streams.Stream(c)
        post = self.get_post_title()
        stream.post(post)



