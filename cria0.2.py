import urllib2
import random
from BeautifulSoup import BeautifulSoup
import os

while True:
    # what my code will be about?
    queries = ['sort', 'reverse', 'pussy', 'cat', 'merge', 'plot',
               'complexnetwork', 'complex', 'network', 'hack', 'boobs',
               'sexy', 'asciiart', 'art', 'ascii', 'ga', 'genetic', 'porn', 'p0rn'
               'asciiporn', 'asciip0rn', 'girl', 'cow', 'tits', 'recursion', 'recursive',
               'fractal', 'mandelbrot', 'agent', 'celullar', 'automata', 'automaton',
               'ircbot', 'bot', 'irc', 'simple', 'socket', 'client', 'http', 'server']
    
    programs = ['python', 'ruby', 'node']
    extension = ["py", "rb", "js"]
    # I choose one of those
    q = random.choice(queries)
    p = random.choice(programs)
    e = extension[programs.index(p)]
    
    # request a gist
    req = urllib2.urlopen("http://gist.github.com/search?l={0}&q={1}".format(*(p, q)))
    html = req.read()
    
    # parse a list of gists in html
    soup = BeautifulSoup(html)
    
    # find all gist creators of the page
    creators = soup.findAll('span', attrs={'class': 'creator'})
    
    # get links for all gists of every creator
    hrefs = [cr.findAll('a', href=True)[1]['href'] for cr in creators]

    if len(hrefs) > 0:
        # get the raw data of a gist
        w = random.randint(0,len(hrefs)-1)
        req = urllib2.urlopen("http://gist.github.com/%s/raw" % hrefs[w])
        raw = req.read()
        
        # create a new file remixing the gist
        f = open("new.%s" % e, 'w')
        f.write(raw)
        f.close()
        
        # run the code
        os.system("{0} new.{1}".format(*(p, e)))
