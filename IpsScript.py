#!/usr/bin/env python
# coding: utf-8



import pandas as pd





dataFrom_IPs  = pd.read_csv(r'C:\Users\xxx\Desktop\Ips.csv',sep=';')
listA = []
listB=[]
Equals=[]
Diff=[]





dataFrom_IPs




list_Host  = dataFrom_IPs['host'].tolist()

list_Host





list_Ips  = dataFrom_IPs['Ips']                  




listEquals=[]
listDiff=[]
temp_list=[]
listB=[]





list_Host #Lista de todos os objetos da Coluna 'host'
list_Ips #Lista de todos os objetos da Coluna 'Ips'


for i,iteminHost in enumerate(list_Host):
        print('-----------------------------------------------------')
        print('Host:'+iteminHost)
        for index, row in enumerate(list_Ips):
            
            listB=list_Ips[index]
            print('')   
            print(listB)
            if iteminHost in listB:
                
                tempA = listB
                
                
                
                dataFrom_IPs.at[index, 'Equals']= iteminHost
                
          
                  
            else:
                tempA.replace(iteminHost,'')
                dataFrom_IPs.at[index, 'Diff']=tempA    



#listEquals  
dataFrom_IPs.head(18)



