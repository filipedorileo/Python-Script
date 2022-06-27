#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataFrom_IPs  = pd.read_csv(r'C:\Users\xxx\Desktop\Ips.csv',sep=';')
listA = []
listB=[]
Equals=[]
Diff=[]


# In[3]:


dataFrom_IPs


# In[4]:


list_Host  = dataFrom_IPs['host'].tolist()

list_Host


# In[5]:


list_Ips  = dataFrom_IPs['Ips']                  


# In[6]:


listEquals=[]
listDiff=[]
temp_list=[]
listB=[]


# In[7]:


list_Host #Lista de todos os objetos da Coluna 'host'
list_Ips #Lista de todos os objetos da Coluna 'Ips'

#listB=list_Ips[0]
#listB = listB.split(",")


# In[ ]:


#"10.222.199.39" in listB


# In[15]:



#listB.append("10.130.191.77")
for i,iteminHost in enumerate(list_Host):
        print(i)
        print(iteminHost)
        # index_Host=list_Host.index(iteminHost)
        for index, row in dataFrom_IPs.iterrows():
            #print(index)
            listB=list_Ips[index]
            #listB = listB.split(",")
            print(type(listB))
            if iteminHost in listB:
            #print(listB)
           #listEquals.append(iteminHost)
                dataFrom_IPs.at[index, 'Equals']= iteminHost        
                #listB.remove(iteminHost)
            else:
               # res= [''.join(ele)for ele in listB]
               # print(res)
                dataFrom_IPs.at[index, 'Diff']=listB 
                #','.join(listB)
           


# In[16]:


#listEquals  
dataFrom_IPs.head(18)


# In[ ]:


#list_Host


# In[ ]:





# In[ ]:




