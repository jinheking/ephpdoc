#-*- coding:utf-8 -*-
#File:cli.py
import os,sys
import ephpdoclib
from optparse import OptionParser, OptionGroup, SUPPRESS_HELP
import ephpdoclib.folder
class cli:
  '''
  本类用于cli操作
  <a target=‘'_blank' href='http://davidx.me/2010/12/10/use-optionparser-to-parse-arguments/'>参考的文章</a>
  '''
  OPTION_DEFAULTS = dict(
      action="html", show_frames=True,
      show_private=True, show_imports=False, inheritance="listed")
  
  def __init__(self):
    usage = '%prog [ACTION] [options] NAMES...'
    version = _("Ephpdoc, version %s") % ephpdoclib.__version__
    #print version
    optparser = OptionParser(usage=usage, add_help_option=False)
    action_group = OptionGroup(optparser, 'Actions')
    optparser.add_option_group(action_group)
    action_group.add_option("--html",
        action="store", dest="foldername",default="htmldoc",
        help=_("Write HTML output."))
    action_group.add_option("-v","--version",
        action="store_const", dest="action", const="version",
        help=_("Show ephpdoc's version number and exit."))
    
    action_group.add_option("-h", "--help",
        action="store_const", dest="action", const="help",
        help=_("Show this message and exit. "))
    
    output_group = OptionGroup(optparser, 'Output Options')
    optparser.add_option_group(output_group)
    output_group.add_option("--name", "-n",
        dest="prj_name", metavar="NAME",
        help="The documented project's name (for the navigation bar).")
    

    
    optparser.set_defaults(**self.OPTION_DEFAULTS)
    options, names = optparser.parse_args()
    self.opt=options
    if options.action == 'version':
      print version
      sys.exit(0)
    
    if options.action == 'help':
      names = set([n.lower() for n in names])
      optparser.print_help()
      sys.exit(0)

    if options.action == 'html':
      path=os.getcwd()
      path+=os.sep
      path+=options.foldername
      #print options
      ephpdoclib.folder().createHtmlFrameWork(path)
      

      
      
