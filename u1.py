# import re
# import mechanize

# br = mechanize.Browser()
# # br.open("http://www.example.com/")
# br.open("http://www.google.com/")
# # follow second link with element text matching regular expression
# # response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
# # assert br.viewing_html()
# print br.title()


# import mechanize
# response = mechanize.urlopen("http://wwww.google.com/")
# print response.read()

# import urllib2

# response = urllib2.urlopen('http://python.org/')

# html = response.read()

# print html 


from mechanize import Browser
browser = Browser()
response = browser.open('http://hotmail.com')
print response.code
print response.geturl()