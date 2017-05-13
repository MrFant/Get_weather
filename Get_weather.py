#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
from city import city
import Email_script
import time
#

__author__="fant"

#
def Get_weather():
    cityname = '北京'
    citycode = city.get(cityname)
    content=' '
    while(True):
        if citycode:
            try:
                url = ('http://www.weather.com.cn/data/cityinfo/%s.html'
                       % citycode)
                content2 = urllib2.urlopen(url).read()
                if content != content2:
                    content = content2
                    data = json.loads(content)
                    result = data['weatherinfo']
                    str_temp = ('%s\n%s ~ %s') % (
                        result['weather'],
                        result['temp1'],
                        result['temp2']
                    )
                    print str_temp
                    #Email_script.Post_Email(str_temp)
                else:
                    pass
                    #time.sleep(3*3600)

            except:
                print '查询失败'
        else:
            print '没有找到该城市'
    
if __name__=='__main__':
    Get_weather()
