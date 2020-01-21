#!/usr/bin/env python3
import cgi
import cgitb

from templates import login_page, secret_page, after_login_incorrect
#import secret
import os
from http.cookies import SimpleCookie


print("Content-type: text/html\n")
print()

#print(os.environ)
print(os.environ.get('HTTP_USER_AGENT'))
#print(os.environ["HTTP_USER_AGENT"])

#print(login_page())
#s = cgi.FieldStorage()
#username = s.getfirst("username")
#password = s.getfirst("password")
