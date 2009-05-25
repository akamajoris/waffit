#!/usr/bin/env python
from evillib import *
import logging, sys

if len(sys.argv) == 1:
    print "pass a domainname"
    sys.exit(1)
logging.basicConfig(level=logging.DEBUG)
w = waftoolsengine(target=sys.argv[1], path="/")    
w.log = logging.getLogger('test')
w.querycrawler(path='/')