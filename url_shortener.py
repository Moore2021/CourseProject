# pylint: disable=no-member
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys
import re 
def Find(string): 
    # findall() has been used  
    # with valid conditions for urls in string 
    x = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),] | (?:%[0-9a-fA-F][0-9a-fA-F]))+", string) 
    return x   
def make_tiny(url):
    # Get An Alias to use
    alias = input("Alias please: ")
    # Set up links to get shortened link
    # Through API
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({
                       'source': 'create',
                       'url': url,
                       'alias': alias
                   }))
    # Though regular site
    offical_page = ('https://tinyurl.com/create.php?' +
                        urlencode({
                            'source': 'indexpage',
                            'url': url,
                            'alias': alias
                        }))
    
    # Print source of links
    print("Extra Information:\nHere is the api page of where the link comes from: {0}".format(request_url))
    with contextlib.closing(urlopen(request_url)) as response:
        print('Here is the offical page of where the link comes from: {0}\n\n'.format(offical_page)) 
        response.read().decode('utf-8')

    # Get response body of offical page
    response = urlopen(offical_page).read().decode()
    # Pull all urls aside
    urlsFound = Find(response)
    # Delete all static urls
    del urlsFound[:15]
    del urlsFound[-3]
    del urlsFound[6]
    del urlsFound[6]
    del urlsFound[3]
    del urlsFound[3]
    
    if "<b style=\"color: red;\">" in response:
        print("That alias is not availiable so a random one has been created for you.")
    return urlsFound[0]

def main():
    if not len(sys.argv) > 1:
        urls = ['https://www.google.com']
    else:
        urls = sys.argv[1:]
    print("\n==========Your links are being processed below==========\n")
    for tinyurl in map(make_tiny, urls):
        print("Here is your shortened link: " + tinyurl)
        print("\n==================================================\n")

if __name__ == '__main__':
    main()
