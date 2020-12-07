#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import geopandas as gpd


# In[13]:


a_co001 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co001')
a_co618 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co618')
a_co641 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co641')
a_co642 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co642')
a_co643 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co643')
a_co644 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co644')
a_co645 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co645')
a_co651 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co651')
a_co653 = gpd.read_file("lab1.gpkg", layer='soilmu_a_co653')


# In[15]:


co001 = gpd.read_file("lab1.gpkg", layer='muaggatt_co001')
co618 = gpd.read_file("lab1.gpkg", layer='muaggatt_co618')
co641 = gpd.read_file("lab1.gpkg", layer='muaggatt_co641')
co642 = gpd.read_file("lab1.gpkg", layer='muaggatt_co642')
co643 = gpd.read_file("lab1.gpkg", layer='muaggatt_co643')
co644 = gpd.read_file("lab1.gpkg", layer='muaggatt_co644')
co645 = gpd.read_file("lab1.gpkg", layer='muaggatt_co645')
co651 = gpd.read_file("lab1.gpkg", layer='muaggatt_co651')
co653 = gpd.read_file("lab1.gpkg", layer='muaggatt_co653')


# In[16]:


a_co001 = a_co001.merge(co001, left_on='MUSYM', right_on='musym')
a_co618 = a_co618.merge(co618, left_on='MUSYM', right_on='musym')
a_co641 = a_co641.merge(co641, left_on='MUSYM', right_on='musym')
a_co642 = a_co642.merge(co642, left_on='MUSYM', right_on='musym')
a_co643 = a_co643.merge(co643, left_on='MUSYM', right_on='musym')
a_co644 = a_co644.merge(co644, left_on='MUSYM', right_on='musym')
a_co645 = a_co645.merge(co645, left_on='MUSYM', right_on='musym')
a_co651 = a_co651.merge(co651, left_on='MUSYM', right_on='musym')
a_co653 = a_co653.merge(co653, left_on='MUSYM', right_on='musym')


# In[17]:


layerlist = [a_co001, a_co618, a_co641, a_co642, a_co643, a_co644, a_co645, a_co651, a_co653]


# In[22]:


a_co001["mapunit"] = "co001"
a_co618["mapunit"] = "co618"
a_co641["mapunit"] = "co641"
a_co642["mapunit"] = "co642"
a_co643["mapunit"] = "co643"
a_co644["mapunit"] = "co644"
a_co645["mapunit"] = "co645"
a_co651["mapunit"] = "co651"
a_co653["mapunit"] = "co653"


# In[28]:


watershed = gpd.read_file("lab1.gpkg", layer='wbdhu8_lab1', crs = )


# In[25]:


layermerge = []
layermerge = pd.concat(layerlist)


# In[31]:


print(layermerge.columns)


# In[32]:


print(watershed.columns)


# In[34]:


layermerge.rename(columns={'geometry_x': 'geometry'})


# In[38]:


intersect_final = gpd.sjoin(layermerge, watershed, how='left',op="intersects")


# In[39]:


layermerge.drop(columns='geometry_y')


# In[40]:


intersect_final = gpd.sjoin(layermerge, watershed, how='left',op="intersects")


# In[ ]:




