

#you-get https://www.bilibili.com/video/BV1ix411h7xm?p=2
#for i in $(seq 1 41); do you-get https://www.bilibili.com/video/BV1ix411h7xm?p=$i; done
import you_get
import os
import time

stime = time.time()

urlList = []
def getMp4(path,urlList):
    cmd_list = []
    for url in urlList:
        #cmds = 'you-get -o %s --format=dash-flv480 %s'%(path,url)
        cmds = 'you-get -o %s  %s'%(path,url)
        #cmds = 'you-get -o %s --format=dash-flv %s'%(path,url)
        #cmds = 'you-get   %s'%(url)
        cmd_list.append(cmds)
    for count,each in enumerate(cmd_list):
        startTime = time.time()
        print("当前正在下载第%s个视频，一共有%s个视频需要下载..."%(count+1,len(cmd_list)))
        print(each)
        os.system(each)
        endtime = time.time()
        useTime = (endtime-startTime)
        print ("您所下载的视频一共使用%s秒"%useTime)
def make_page(url):
    for p in range(1,2):
        
        urlList.append(url)
if __name__ == '__main__':
    url=input()
    make_page(url)
    path = "e:\\xxdd"
    getMp4(path,urlList)
    etime = time.time()
    utime = (etime-stime)/60
    print ("您所下载的全部视频一共使用%s分钟"%utime)

