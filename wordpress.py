import sublime
import sublime_plugin
import datetime
import xmlrpclib
import sys
import re

class WordpostCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):

        wp_url = "http://blogdomain.com/xmlrpc.php"
        wp_username = "username"
        wp_password = "password"
        wp_blogid = ""

        status_published = 1

        server = xmlrpclib.ServerProxy(wp_url)
        allText = self.view.substr(sublime.Region(0, self.view.size()))
        title = re.search('%s(.*)%s' % ('<title>', '</title>'), allText).group(1)
        content = re.search('%s(.*)%s' % ('<body>', '</body>'), allText).group(1)
        date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2013-06-24 21:35", "%Y-%m-%d %H:%M"))
        categories = re.search('%s(.*)%s' % ('<categories>', '</categories>'), allText).group(1).split(',')
        tags = re.search('%s(.*)%s' % ('<tags>', '</tags>'), allText).group(1).split(',')
        data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

        try:
            server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
        except Exception as ins:
            sublime.status_message("There was an error sending the post. If this is the start() thing ignore it: %s " % ins)

