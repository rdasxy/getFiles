from pyparsing import makeHTMLTags
import urllib.request
import os.path

'''
Use html tags to find all filenames of some type referenced in a web page, then filter the results
and download the files to a specified directory.  For example, we can find all the img files, and then
grab only the png's, or only the png's and jpg's.
'''

# read data from web page
url = r'http://www.stroustrup.com/Programming/Graphics/'
target = 'C:/users/saul/desktop'
html = urllib.request.urlopen(url).read()

# define expression for <a> tag
aTag, aEndTag = makeHTMLTags("a")

# search for matching tags, extract attributes by key value

hrefs= (h['href'] for h in aTag.searchString(html))
files = (h for h in hrefs if h.endswith('.h') or h.endswith('.cpp'))
for file in files:
    urllib.request.urlretrieve(os.path.join(url,file), os.path.join(target, file))

    
    
    