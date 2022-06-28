#!/usr/bin/env python
# coding: utf-8

import pandas as pd

dataFrom_IPs = pd.read_csv(r'C:\Users\Findmore\Desktop\Ips.csv', sep=';')
listA = []
listB = []
Equals = []
Diff = []

list_Host = dataFrom_IPs['Host'].tolist()
list_Ips = dataFrom_IPs['Ips']

listEquals = []
listDiff = []
temp_list = []
listB = []
# listB=list_Ips[0]
#listB = listB.split(",")

for i, iteminHost in enumerate(list_Host):

    for index, listinIps in enumerate(list_Ips):
        tempA=[]
        listinEqual=[]
        listinDiff=[]


        # print('')
        # print(listB)
        if iteminHost in listinIps:

            listinEqual=dataFrom_IPs.at[index, 'Equals']
            listinDiff=dataFrom_IPs.at[index, 'Diff']
            if isinstance(listinEqual,list):
                print("ok")
            else:
                listinEqual=listinEqual.split(",")

            if isinstance(listinDiff,list):
                print("ok")
            else:
                listinDiff=listinDiff.split(",")
            
            
            #adicionar o que é igual
            listinEqual.append(iteminHost)

            #remover caso esteja na lista de Diff
            if iteminHost in listinDiff:
                listinDiff.remove(iteminHost)  


            #listinEqual.remove()

            dataFrom_IPs.at[index, 'Diff'] = listinDiff
            dataFrom_IPs.at[index, 'Equals'] = listinEqual

            # dataFrom_IPs.at[index, 'Equals'] = iteminHost
            # tempA = listB
            # tempA = tempA.replace(iteminHost, '')
            # tempA= tempA.split(",")
            # tempA.remove(iteminHost)
            # dataFrom_IPs.at[index, 'Diff'] = str(tempA)

print(dataFrom_IPs.head(4))