#!/usr/local/bin/python

import html5lib
import urllib2
import lxml
from lxml.html import tostring
from lxml import etree

parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("lxml"))
f = urllib2.urlopen("http://ex.ua/view/14475479").read()
doc = html5lib.parse(f,treebuilder="lxml" , namespaceHTMLElements=False)
root = doc.getroot()

fnd_p = etree.XPath("/html/body/table/tbody/tr/td/table[@class='list']/tbody/tr/td/a[@rel='nofollow']", namespaces = {"html": "http://www.w3.org/1999/xhtml"})
print "[playlist]"
item = 1;
for a in fnd_p(root):
    print("File"+str(item)+"=http://ex.ua"+a.get('href'));
    print("Title"+str(item)+"="+a.get("title"))
    item=item+1;
