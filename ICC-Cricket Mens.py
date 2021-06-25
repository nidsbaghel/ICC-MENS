#!/usr/bin/env python
# coding: utf-8

# In[22]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[23]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[24]:


page=["https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting",
    "https://www.icc-cricket.com/rankings/mens/player-rankings/test/bowling",
    "https://www.icc-cricket.com/rankings/mens/rankings-predictor/odi"]


# In[1]:


final_result_file_name="All Ranking List.csv"
final_result_file_name=["player name","team name","Rating","career Best Rating"]


# In[2]:


pd.DataFrame(column=final_coulmn_names).to_csv(final_result_file_name,sep="\t",index=False,encoding="utf-8")


# In[12]:


for page in pages:
    request_object=requests.get(url,headers=headers)
soup_object=BeautifulSoup(html_content,"lxml")
for element in soup_object.select('[class+"ranking-pos up"],[class="ranking-pos down"]'):
        element.replace_with(BeautifulSoup("<"+elemnt.name+">"/+element.name+">","html.parser"))
rankling_type=soup_object.select_one("ranking_block_title_container>h4").text
result_file_name=ranking_type+".csv"
    
column_name=["player Name","Team Name","Rating","Career Best Rating"]
    
    


# In[5]:


pd.DataFrame({})

for element in soup_object.select('table[class="table ranking-table"]tr')
 if (element.find("th")):
        continue
        data_dict=dict()
        data_dict["crawl URl"]=url
        data_dict["Ranking Type"]=ranking_type
        if(element.select_one('[class*="position"]')):
            data_dict["podition"]=element.select_one('[class*="postion"]').text


# In[32]:


for player_name in element.select('a[href*="/player-ranking"]'):
    if(player_name.text.strip()):
        data_dict["player Name"]=Player_name.text
        
if(element.select_one('[class^="flag-15"]')):
    data_dict["Team Name"]=element.select_one('["class^=flag-15"]')["class"][-1]
if(element.select_one('[class$="rating"]')):
   data_dict["Rating"]=element.select_one('[class$="rating"]').text
   
if(element.select_one('td.uhide_phabet')):
   
 data_dict["career Best Rating"]=element.select_one('td.u-hide-phabet').text
   
for key in data_dict.key():
   data_dict[key]=re.sub(r"\s+"," ",data_dict[key])
   data_dict[key]=data_dict[key].strip()

pd.DataFrame([data_dict], columns=column_names).to_csv(result_file_name).to_csv(result_file_name,sep="\t", index=False,header=False,encoding="utf-8",mode="a")


# In[ ]:




