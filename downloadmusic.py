# -*- coding:utf-8 -*-  
  
import urllib  
import os
import json  
import sys  
import time  
reload(sys)  
sys.setdefaultencoding('gb18030')  
  
def getURL_of_music(json_url):  
    url = json_url  
    response = urllib.urlopen(url)  
    content = response.read().decode('utf-8')  
    print content
    js = json.loads(content)  
    k = u"audio"  
    print js['result']['songs'][0]
    music_url = js['result']['songs'][0][k]  
    return music_url  
  
  
def download_music(save_path,songName,url_org):  
    url = getURL_of_music(url_org)  
    if not os.path.isdir(save_path):  
        os.mkdir(save_path)  
    save_music_name = save_path.decode('utf-8')+"/"+songName.decode('utf-8')+u".mp3"  
    if not os.path.exists(save_music_name):   
        #print save_music_name  
        urllib.urlretrieve(url,save_music_name)  
    return save_music_name  
  
  
def play_music(music_path):  
    file_mp3 = music_path  
    mp3 = mp3play.load(file_mp3)  
    mp3.play()  
    time.sleep(mp3.seconds())  
    mp3.stop()  
      
      
  
if __name__ == "__main__":  
          
    music_name=raw_input("Please input music name of what you want to listen:")
    music_name_url=urllib.quote(music_name)
    print music_name
    limit = "2"  
    type ="1"  
    url='http://s.music.163.com/search/get/'  
    url = url+"?type="+type+"&limit="+limit+"&s="+music_name_url
    save_music = download_music('/Users/sungang/downloadmusic', music_name, url)
    flag = raw_input("Would you like to listen %s right now ?: (Y/N)"%music_name.decode('utf-8'))  
    if flag=='Y':  
        play_music(save_music)  
    else:  
        print "Are you kiding me?" 
