#1. Сколько было всего запросов
#2. Сколько уникальных ip адресов обратилось
#3. Какие браузеры обращались. Для простоты берем запись почти в конце строки (Firefox/34.0)
#4. Сколько запросов от каждого такого браузера ''' 

import re
from collections import Counter

ip_set = set()
ip_list = []

def reader(file_name):

   with open (file_name) as file: 
      
      regxp_ips = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
      
      for line in file:
         ips = re.search(regxp_ips, line)
         ip_list.append(ips.group(0))
   print('Сколько было всего запросов: ' + str(len(ip_list)))

def reader_1(file_name):

   with open (file_name) as file: 
      
      regxp_ips = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
      
      for line in file:
         ips = re.search(regxp_ips, line)
         ip_set.add(ips.group(0))
   print('Сколько уникальных ip адресов обратилось: ' + str(len(ip_set)))


def reader_1(file_name):

   with open (file_name) as file: 
      
      regxp_ips = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
      
      for line in file:
         ips = re.search(regxp_ips, line)
         ip_set.add(ips.group(0))
   print('Сколько уникальных ip адресов обратилось: ' + str(len(ip_set)))

if __name__ == "__main__":
   reader('access.log')