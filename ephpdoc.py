# -*- coding: utf-8 -*-
import glob,os,sys
import gettext
import ephpdoclib

'''
 Copyright (C) 2011 Eagle
 Author: Edward Loper <jinheking@gmail.com>
 URL: <http://www.caoqi.com>

 $Id: ephpdoc.py 2011-01-19 17:55 Eagle $
''' 
  #getCurrentPathFilenameList('','')
if '__main__' == __name__:
  try:
    cruentpath=ephpdoclib.folder().getCurrentPath() 
    gettext.install('lang', cruentpath+'\locale', unicode=False)
    gettext.translation('lang', cruentpath+'\language', languages=['zh-CN']).install(True)
    print _('Current Version is')+'0.0.1!'
    print _('Ephpdoc is tool for php that is the function of the PHP inside comments compiled into an HTML document.') 

    '''
    fo=ephpdoclib.folder()
    for item in  fo.dir_list_allfolder(os.getcwd()):
      print item
    '''
    cli=ephpdoclib.cli()
    #print cli.opt.foldername
    ephpdocfile=ephpdoclib.ephpdocfile()
    ephpdocfile.openFile(".\Action\MgModel.class.php",cli.opt.foldername)
    #for item in fo.dir_list_folder(os.getcwd(),r'LC_MESSAGES'):
    #  print item
  except IndexError,Error:
    print Error
    pass
  


