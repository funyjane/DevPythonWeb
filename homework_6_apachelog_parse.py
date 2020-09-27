#1. Сколько было всего запросов
#2. Сколько уникальных ip адресов обратилось
#3. Какие браузеры обращались. Для простоты берем запись почти в конце строки (Firefox/34.0)
#4. Сколько запросов от каждого такого браузера ''' 

import re
from collections import Counter

ip_set = set()
ip_list = []
browsers = {'Firefox':0,
'Chrome': 0,
'Edge': 0,
'Explorer': 0,
'Opera': 0,
'Safari': 0}


#1. Сколько было всего запросов
def reader(file_name):

   with open (file_name) as file: 
      
      regxp_ips = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
      
      for line in file:
         ips = re.search(regxp_ips, line)
         ip_list.append(ips.group(0))
   print('Сколько было всего запросов: ' + str(len(ip_list)))

#2. Сколько уникальных ip адресов обратилось
def reader_1(file_name):

   with open (file_name) as file: 
      
      regxp_ips = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
      
      for line in file:
         ips = re.search(regxp_ips, line)
         ip_set.add(ips.group(0))
   print('Сколько уникальных ip адресов обратилось: ' + str(len(ip_set)))

#Какие браузеры обращались. Для простоты берем запись почти в конце строки (Firefox/34.0)
def browser_reader(file_name):

   with open (file_name) as file: 
      
      for line in file:
         user_request = line[-40:]
         for browser in browsers.keys():
            #4. Сколько запросов от каждого такого браузера ''' 
                if browser in user_request:
                    browsers[browser] += 1
      print('Количество запросов от браузеров:')
      for keys, values in browsers.items():
            print(keys, '-', values)
   

if __name__ == "__main__":
   browser_reader('access.log')