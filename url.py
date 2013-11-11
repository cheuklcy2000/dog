import urllib2
from BeautifulSoup import BeautifulSoup
# f = urllib2.urlopen('http://www.google.com/')
# print BeautifulSoup(f).prettify()
# import mechanize
# response = mechanize.urlopen("http://www.example.com/")
# print response.read()


import re
import mechanize

# br = mechanize.Browser()
# br.open("http://www.example.com/")
# # follow second link with element text matching regular expression
# response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
# assert br.viewing_html()
# print br.title()
# print response1.geturl()
# print response1.info()  # headers
# print response1.read()  # body


baseurl = "https://www.website.com/login"
br = mechanize.Browser(factory=mechanize.RobustFactory())
br.open(baseurl)
br.select_form(nr=0)
br.form["username"] = self.username
br.form["password"] = self.password
response = br.submit()
print response.geturl()