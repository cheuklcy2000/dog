# import mechanize
# import urllib
# br = mechanize.Browser()
# url = "www.google.com"
# response = br.open(url)
# print response.read()  

import re
import mechanize

br = mechanize.Browser()
# br.open("http://www.example.com/")
br.open("http://www.hotmail.com/")
# follow second link with element text matching regular expression
# response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
# assert br.viewing_html()
print br.title()