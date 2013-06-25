Hello everybody.

This is a Sublime Text plugin for WordPress blogs. It will let you create a post and then send it to your wordpress blog.

Usage is really easy and straight forward. There is no need for configuration just a mininal when setting up your blog and username / password. 

*Installation*

Just copy the wordpress.py into your User folder under the Sublime plugin. There are no thrid party compnents that you need. However you need to enable xmlrpc in your blog. If you have Wordpress 3.5 or above it is enabled by default. 

It's reachable under http://yourdomain/yourblog/xmlrpc.php

Then you just edit the username / password in the plugin file and your done!

<code>
wp_url = "http://blogdomain.com/xmlrpc.php"
wp_username = "username"
wp_password = "password"
</code>

The shortcut file for the command can be also found here. It's easy to set up, just add it to your default key configuration file called: Default.sublime_keymap which is also in the User folder.

*Usage*

Usage is even more easier then installation. You just simply open up a new file and start writing your entry in the following format:

```xml
<post>
	<title>This is the Title</title>
	<body>This will be the body.</body>
	<categories>python,problem solving,even more categories</categories>
	<tags>python,sublimetext,socool</tags>
</post>
```

It should immediately publish the post, if you want it to be a draft then the only thing you have to do is edit the status_published to 0. 
Or add it as an <publish>true</publish> xml entry. Whatever you want. :)

*Known problems*

For some wierd reason the xmlrpc throws an exception that start() needs 3 parameters but 5 were given. You can ignore this exception it will work that way. But it's really strange. The submit in xmlrpc does really have 3 params as the last param is an arg which will be used to get out the passed in arguments. With other Python IDEAs like PyCharm this works fine. For some reason though Sublime doesn't seem to like it. 

If you find a solution to this, please feel free to add it to the code. Thanks!

Currently there is no escape in between the lines of body and it's too late now to add it. Until then if you want to add links and such use: < = \&lt; and > = \&gt;.

And currently if you don't have the category that you want to add it won't create it for you. 

I will fix these once I slept a little..

*Last words*

That's all folks.
Please enjoy.
And have a nice day!
Gergely.
