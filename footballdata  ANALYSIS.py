
# coding: utf-8

# In[2]:


print(4)


# In[ ]:


#our objective is to find best team among 288  teams without any data loss    


# In[3]:



import pandas 
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[4]:


db1=pandas.read_excel("C:\\Users\\manu\\desktop\\Database\\a\\Database.xlsx", sheetname="Team_Attributes")


# In[4]:


db1


# In[5]:


db1.head(5)



# In[6]:


db1.columns


# In[7]:


db1.shape


# In[8]:


db1.tail(5)


# In[9]:


del (db1['id'])


# In[10]:


df=db1.drop('team_fifa_api_id',axis=1)


# In[11]:


df


# In[12]:


team=pandas.read_excel('C:\\Users\\manu\\desktop\\Database\\a\\Database.xlsx',sheetname='Team')


# In[16]:


team


# In[13]:


team1=team[['team_short_name','team_api_id']]


# In[18]:


team1


# In[14]:


df1=pandas.merge(df,team1,on='team_api_id')


# In[15]:


df1


# In[17]:


df1.get_dtype_counts()


# In[16]:


df_string=df1.select_dtypes(include=['object'])


# In[27]:


df_string


# In[21]:


#excluding object data type column 


# In[17]:


df_numerical=df1.select_dtypes(exclude=['object'])


# In[18]:


df_numerical


# In[39]:


df_numerical['team_short_name']=df_string['team_short_name']


# In[20]:


df_numerical.iloc[:,2:-1].shape


# In[24]:


sns.heatmap(df_numerical.iloc[:,2:-1])  

smalldf=df_numerical.iloc[:50,:]

sns.heatmap()   


# In[26]:



sns.barplot(x="defenceAggression", y="team_short_name", data=smalldf)


# In[25]:


sns.swarmplot(x="defenceAggression", y="team_short_name", data=smalldf)


# In[26]:


df_numerical


# In[27]:


df_numerical.shape


# In[27]:


sns.barplot(x='team_api_id',y='buildUpPlaySpeed',data=df_numerical)


# In[28]:


df_num1=df_numerical.groupby(['team_api_id'] , axis =0).mean()


# In[29]:


df_num1


# In[30]:


df_num2=df_num1.reset_index()


# In[31]:


df_num2


# In[32]:


df_numerical[df_numerical.team_api_id==2183]


# In[35]:


df_num2=df_num2.fillna(df_num2.mean())


# In[36]:


df_num2


# In[33]:


#d1=df_num2.applymap(lambda x:x>50)
d1=df_num2.applymap(lambda x:x>50).all(axis=1)


# In[34]:


d1


# In[35]:


d1['teamname']=df_string['team_short_name']


# In[36]:


df_num2['Result']=d1


# In[37]:


df_num2[df_num2['Result'] ==True]

