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
                    title = meta["content"].strip()
                if name == "description":
                    description = meta["content"].strip()
                if name == "keywords":
                    tags = meta["content"].strip()
        return title + description + tags



    def post_entry(self):
        print('Posting entry to D*')
        client = diaspy.connection.Connection(self.pod_url, self.username, self.password)
        post = self.get_post_title()
        client.post('status_messages', post)



