#-*- coding:utf-8 -*-
#File:ephpdocfile.py
import glob,os,sys
import shutil
import codecs
import re
class ephpdocfile:
    '''
    本Class的作用是文件的操作,包括读写
    '''
    def replaceMenu(self,reg,sourceStr,newStr):
        '''
        本函数的作用是替换toc.html里面的<ul id="menu">……</ul>
        @date 2011-06-29添加
        @param reg string 正则表达式
        @param sourceStr string 原字符串
        @param newStr string 要添加的字符串
        @return result string 替换好的字符串
        @see <a href="http://developer.51cto.com/art/201003/188824.htm">参考</a>
        '''
        mi= re.compile(reg)
        m=mi.finditer(sourceStr)
        for my in m:
            content=r'<ul id="menu">'+my.group('body')+newStr+r'</ul>'
            result, number = re.subn(reg, content, sourceStr) 
            return result
    
    def nl2br(self,string, is_xhtml= True ):
        """
        替换nl
        """
        if is_xhtml:
            return string.replace('\n','<br />\n')
        else :
            return string.replace('\n','<br>\n')
    
    def openFile(self,filename,foldname):
        '''
        文件打开
        @param filename string 文件名
        @param foldname string 生成的帮助文档的目录地址
        @return handle 文件句柄
        @see <a target="_blank" href="http://www.cnblogs.com/lovebread/archive/2009/12/24/1631108.html">参考</a>
        @see <a target="_blank" href="http://blog.csdn.net/zheng_j_c/archive/2010/08/11/5804798.aspx">参考</a>
        现在有一个问题，就是一个文件目前只能够有一个Class,有多的Class还不能够有多余一个的Class
        '''
        file_target = open(foldname+"/toc.html",'w+')
        file_target.write( codecs.BOM_UTF8) 
        file_object = codecs.open(filename,"r","utf-8")
        strcontent = file_object.read()
        #content = str.replace("\n"," ")
        content = strcontent
#        print content
#        m= re.findall(r'class\s+(.*?)\s+extends',strcontent, re.S | re.I)
        m= re.findall(r'\<\?php',strcontent, re.S | re.I)
 
        #print m
        for my in m:
            #print my.strip()
            strcontent=strcontent[strcontent.find(my.strip(),0)+len(my.strip()):]
            tmp= re.findall(r'/\*\*.*?\*/\s+class',strcontent, re.S | re.I) 
            for t in tmp:
                file_target.writelines(self.nl2br(t.encode("utf-8")[:-5])+"<br />\r\n")
                #print type(t)
            file_target.writelines(r'<ul id="menu">')
            m_fun= re.findall(r'\r\s+([a-z]{1,})\s+function\s+(.*?)\s*\(.*?\)',strcontent, re.S | re.I)
            dict_fun={}
            for mm in m_fun:
                dict_fun[mm[1].strip()]=mm[0].strip()
#                file_target.writelines(r'<li>'+mm[1].strip()+r'</li>')
                #print mm.strip()
#            print dict_fun
            m_fun= re.findall(r'function\s+(.*?)\s*\(.*?\)',strcontent, re.S | re.I)
            for mm in m_fun:
                key=mm.strip()
#                print key
                if key in dict_fun:
                    pass
                else:
                    dict_fun[key]='protected'
#                    file_target.writelines(r'<li>'+mm.strip()+r'</li>')
#            dict_fun=sorted(dict_fun.iteritems(), key=lambda asd:asd[1], reverse = False )
            list_fun=[]
            for fun in dict_fun:
                list_fun.append(fun)
            list_fun.sort()
            for l in list_fun:
                file_target.writelines(r'<li><a href="#'+l+'">'+l+r'</a></li>')
            file_target.writelines(r'</ul>')
        file_target.close();

