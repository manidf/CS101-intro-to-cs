# example of a procedure

page = 'this is an html page <a href="http://www.google.com">Click here</a> to view another page'

def get_next_target(page):
    start_link = page.find('<a hef=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote