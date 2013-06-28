import sublime
import sublime_plugin
import datetime
import xmlrpclib
import sys
import re
from xml.dom.minidom import parse, parseString

class WordpostCommand(sublime_plugin.TextCommand):
    
    def getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)

    def run(self, edit):

        wp_url = "http://yourblog.com/xmlrpc.php"
        wp_username = "username"
        wp_password = "password"
        wp_blogid = ""

        status_published = 1

        server = xmlrpclib.ServerProxy(wp_url)
        allTextDOM = parseString(self.view.substr(sublime.Region(0, self.view.size())))
        title = self.getText(allTextDOM.getElementsByTagName('title')[0].childNodes)
        content = self.getText(allTextDOM.getElementsByTagName('body')[0].childNodes)
        date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2013-06-24 21:35", "%Y-%m-%d %H:%M"))
        categories = self.getText(allTextDOM.getElementsByTagName('categories')[0].childNodes).split(',')
        tags = self.getText(allTextDOM.getElementsByTagName('tags')[0].childNodes).split(',')
        data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

        try:
            server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
        except Exception as ins:
            sublime.status_message("There was an error sending the post. If this is the start() thing ignore it: %s " % ins)

