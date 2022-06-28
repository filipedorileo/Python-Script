#!/usr/bin/env python
# coding: utf-8

import pandas as pd

dataFrom_IPs = pd.read_csv(r'C:\Users\Findmore\Desktop\Ips.csv', sep=';')
listA = []
listB = []
Equals = []
Diff = []


dataFrom_IPs


list_Host = dataFrom_IPs['Host'].tolist()

list_Host

list_Ips = dataFrom_IPs['Ips']


listEquals = []
listDiff = []
temp_list = []
listB = []


list_Host  # Lista de todos os objetos da Coluna 'host'
list_Ips  # Lista de todos os objetos da Coluna 'Ips'

# listB=list_Ips[0]
#listB = listB.split(",")




for i, iteminHost in enumerate(list_Host):
    print('-----------------------------------------------------')
    print('Host:'+iteminHost)
    for index, row in enumerate(list_Ips):

        listB = list_Ips[index]
        print('')
        print(listB)
        if iteminHost in listB:

            dataFrom_IPs.at[index, 'Equals'] = iteminHost

        else:
            tempA = listB
            tempA = tempA.replace(iteminHost, '')
            print('#######')
            print('tempA:  '+tempA)
            print('#######')

            dataFrom_IPs.at[index, 'Diff'] = tempA


dataFrom_IPs.head(18)

dataFrom_IPs.at[2, 'Diff']
