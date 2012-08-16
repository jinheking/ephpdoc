#-*- coding:utf-8 -*-
#File:folder.py
import glob,os,sys
import shutil
class folder:
  '''
本Class的作用是包括目录、文件的搜索操作
  '''
  def dir_list_folder(self,head_dir, dir_name):
    """
  列出传入路径下的所有目录名
  @param head_dir string 检索的目录名
  @param dir_name string 要检索的目录名
  @return outlist list 所有的目录列表
    """
    outputList = []
    for root, dirs, files in os.walk(head_dir):
      for d in dirs:
        if d.upper() == dir_name.upper():
          outputList.append(os.path.join(root, d))
    return outputList
  def dir_list_allfolder(self,head_dir):
    '''
  列指定目录下的所有目录名
  @param head_dir string 检索的目录名
  @return out list 所有的目录列表
    '''
    out=[]
    for i in os.walk(head_dir+os.sep):
      out.append(i[0])
    return out
  
  def getCurrentPath(self):
    '''
    本函数是返回当前执行目录的全目录名
    @return pathname string 返回当前执行目录的全目录名
    '''
    return os.getcwd()+os.sep+os.path.dirname(sys.argv[0])

  def getCurrentPathFilenameList(self,folder,ext):
    '''
  取得当前目录的文件列表
  @param folder string 指定目录名
  @param ext string 指定扩展名
  @return files list 当前目录下的指定扩展名文件名列表
  <a target="_blank" href="http://bytes.com/topic/python/answers/832443-python-code-search-folder-not-file-inside-another-folder">参考</a>
  '''
    files = os.listdir(folder) # 指定目录中的所有文件
    files = glob.glob('*.'+ext)
    return files


  def createHtmlFrameWork(self,foldername):
    '''
    创建HTML的基本框架,把Templetes\default里面的所有东西复制到指定的foldername目录下。
    @param foldername string 指定目录名
    <a target="_blank" href="http://blog.sina.com.cn/s/blog_64d75a250100i1yb.html">参考</a>
    '''
    if os.path.isdir(foldername):
      print _("%s already exits!") %(foldername)
      sys.exit()
      #self.CleanDir(foldername)
      #os.removedirs(foldername)
      #shutil.rmtree(foldername)
      #sys.exit()
    else :
      sourceFolderName=self.getCurrentPath()
      sourceFolderName+=os.sep
      sourceFolderName+="Templets"
      sourceFolderName+=os.sep
      sourceFolderName+="default"
      shutil.copytree(sourceFolderName,foldername)
     

  def CleanDir(self,Dir):
    if os.path.isdir(Dir):
      paths = os.listdir(Dir)
      for path in paths:
        filePath = os.path.join(Dir,path)
        if os.path.isfile(filePath):
          try:
            os.remove(filePath)
          except os.error:
            autoRun.exception( "remove %s error." %filePath )#引入logging
        elif os.path.isdir(filePath):
          if filePath[-4:].lower() == ".svn".lower():
            continue
          shutil.rmtree(filePath,True)
    return True 
  
