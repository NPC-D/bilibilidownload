# coding=utf-8

from lzma import FORMAT_ALONE
import requests
import re
import json
from moviepy.editor import  VideoFileClip,AudioFileClip


# 安装指导：
# cmd-->:
# pip install requests
# pip install MoviePy
# 注意：
# 由于MoviePy某些功能要用到requests，但是目前直接用pip安装MoviePy时并不会自动帮你安装这个依赖包
# ------------------------------------MoviePy简介👇------------------------------------------
# 1.用python剪辑、组合视频

import time
import threading
def threadDecorator(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

@threadDecorator
def demoFunc(i,url,headers):

    urls = url+'?p='+str(i)

    print(urls)

    response=requests.get(urls,headers).text

    pattern='<script>window\.__playinfo__=(.*?)</script>'
    list=re.findall(pattern,response,re.S)

    list_json=json.loads(list[0])
    title_pattern='<span class="tit">(.*?)</span>'

    # --------------获取文件名字👇--------------
    try:
        title=re.findall(title_pattern,response,re.S)[0]
    except:
        title='B站未知视频'

    print("【"+str(i)+"】"+title+"正在下载")

    volume_url=list_json['data']['dash']['audio'][0]['baseUrl'] # 音频地址

    video_headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
            'cookie': "_uuid=165C46B1-C976-4E75-4FBB-DF7CFCE9B78361416infoc; buvid3=E74152CF-4259-4805-8FB0-3EA62B1A5FE118565infoc; sid=8dy5swfr; buvid_fp=E74152CF-4259-4805-8FB0-3EA62B1A5FE118565infoc; DedeUserID=437098665; DedeUserID__ckMd5=58f089438dd790da; SESSDATA=8509a172%2C1632993914%2Cf1dcc*41; bili_jct=db8c6082bba38c59445d89a6dc2bc8eb; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k)~u~lR)|m0J'uYu~RRk||Y; fingerprint3=9ea3019a6caf79f955972512cf343226; buvid_fp_plain=E74152CF-4259-4805-8FB0-3EA62B1A5FE118565infoc; LIVE_BUVID=AUTO1616186326504349; fingerprint=654b13db806dedf4a8363492a4c50757; fingerprint_s=5f802b1000417d59e0227513b1f22a3e; bp_t_offset_437098665=526477194229905374; bp_video_offset_437098665=531352875458576657; PVID=1; CURRENT_QUALITY=116",
            'referer': 'https://www.bilibili.com/v/dance/?spm_id_from=333.851.b_7072696d6172794368616e6e656c4d656e75.18'
        }

    audio=requests.get(url=volume_url,headers=video_headers).content
    with open('./'+str(i)+'.mp3','wb') as f:
        f.write(audio)

    i += 1
    return # 这里在多线程中十分重要

@threadDecorator
def demoFunc02():
    for i in range(6):
        print(time.time())
        time.sleep(1)

def Batch_download():

    i = 1
    u='https://www.bilibili.com/video/'
    url=u+input('请输入B站视频链接video/：')
    ins = input('需要下载多少呢？')

    headers={
        'Referer': 'https://www.bilibili.com/video/BV1bK4y19743?spm_id_from=333.5.b_64616e63655f6f74616b75.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    while i <= int(ins):
        
        urls = url+'?p='+str(i)

        print(urls)

        response=requests.get(urls,headers).text

        pattern='<script>window\.__playinfo__=(.*?)</script>'
        list=re.findall(pattern,response,re.S)

        list_json=json.loads(list[0])
        title_pattern='<span class="tit">(.*?)</span>'

        # --------------获取文件名字👇--------------
        try:
            title=re.findall(title_pattern,response,re.S)[0]
        except:
            title='B站未知视频'

        print("【"+str(i)+"】"+title+"正在下载")

        volume_url=list_json['data']['dash']['audio'][0]['baseUrl'] # 音频地址

        video_headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
            'cookie': "_uuid=165C46B1-C976-4E75-4FBB-DF7CFCE9B78361416infoc; buvid3=E74152CF-4259-4805-8FB0-3EA62B1A5FE118565infoc; sid=8dy5swfr; buvid_fp=E74152CF-4259-4805-8FB0-3EA62B1A5FE118565infoc; DedeUserID=437098665; DedeUserID__ckMd5=58f089438dd790da; SESSDATA=8509a172%2C1632993914%2Cf1dcc*41; bili_jct=db8c6082bba38c59445d89a6dc2bc8eb; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k)~u~lR)|m0J'uYu~RRk||Y; fingerprint3=9ea3019a6caf79f955972512cf343226; buvid_fp_plain=E74152CF-4259-4805-8FB0-3EA62B1A5FE118565infoc; LIVE_BUVID=AUTO1616186326504349; fingerprint=654b13db806dedf4a8363492a4c50757; fingerprint_s=5f802b1000417d59e0227513b1f22a3e; bp_t_offset_437098665=526477194229905374; bp_video_offset_437098665=531352875458576657; PVID=1; CURRENT_QUALITY=116",
            'referer': 'https://www.bilibili.com/v/dance/?spm_id_from=333.851.b_7072696d6172794368616e6e656c4d656e75.18'
        }

        audio=requests.get(url=volume_url,headers=video_headers).content
        with open('./'+str(i)+'.mp3','wb') as f:
            f.write(audio)

        i += 1

def Multithreaded_batch_download(): # 多线程下载
    i = 1
    u='https://www.bilibili.com/video/'
    url=u+input('请输入B站视频链接video/：')
    ins = input('需要下载多少呢？')

    headers={
        'Referer': 'https://www.bilibili.com/video/BV1bK4y19743?spm_id_from=333.5.b_64616e63655f6f74616b75.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    while i <= int(ins):
        demoFunc(i,url,headers)

Batch_download()


 