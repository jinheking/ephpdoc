# -*- coding: utf-8 -*-
import glob,os,sys
import re


if '__main__' == __name__:
  s=r'<ul id="menu"><li>1</li></ul>'
  reg=r'<ul id="menu">(?P<body>.*?)</ul>'
  mi= re.compile(reg)
  m=mi.finditer(s)
  for my in m:
    content=r'<ul id="menu">'+my.group('body')+r'<li>美丽人生</li>'+r'</ul>'
    result, number = re.subn(reg, content, s) 
    print unicode(result,"utf-8").encode("GBK")

