import mmap
import contextlib

from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from xml.dom import minidom

def MyFun():
    EvtxPath = "D:Application.evtx"

    with open(EvtxPath,'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)) as buf:
            fh = FileHeader(buf,0)
            for xml, record in evtx_file_xml_view(fh):
                #只输出事件ID为4624的内容
                InterestEvent(xml,4624)


# 过滤掉不需要的事件，输出感兴趣的事件
def InterestEvent(xml,EventID):
    xmldoc = minidom.parseString(xml)
    # 获取EventID节点的事件ID
    booknode=root.getElementsByTagName('event') 
    for booklist in booknode: 
        bookdict={} 
        bookdict['id']=booklist.getAttribute('id') 
        bookdict['head']=booklist.getElementsByTagName('head')[0].childNodes[0].nodeValue.strip() 
        bookdict['name']=booklist.getElementsByTagName('name')[0].childNodes[0].nodeValue.strip() 
        bookdict['number']=booklist.getElementsByTagName('number')[0].childNodes[0].nodeValue.strip() 
        bookdict['page']=booklist.getElementsByTagName('page')[0].childNodes[0].nodeValue.strip() 
    if EventID == eventID:
        pass
if __name__ == '__main__':

    print("aaa")