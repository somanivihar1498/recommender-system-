
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# In[8]:


column_names=['user_id','item_id','ratings','timestamp']
df=pd.read_csv('u.data',sep='\t',names=column_names)
# In[11]:


df.head(10)


# In[13]:


movie_titles=pd.read_csv('Movie_Id_Titles')


# In[14]:


movie_titles.head(10)


# In[15]:


df=pd.merge(df,movie_titles,on='item_id')


# In[18]:


df[df['ratings']>4].head()


# In[19]:


df.groupby('title')['ratings'].count().sort_values(ascending=False).head()


# In[21]:


ratings=pd.DataFrame(df.groupby('title')['ratings'].mean())


# In[22]:


ratings.head()


# In[23]:


ratings['num of ratings']=pd.DataFrame(df.groupby('title')['ratings'].count())


# In[27]:


ratings.sort_values('num of ratings',ascending=False).head()


# In[28]:


movie_mat=df.pivot_table(index='user_id',values='ratings',columns='title')


# In[29]:


movie_mat.head(10)


# In[32]:


starwars_user_ratings = movie_mat['Star Wars (1977)']
liarliar_user_ratings = movie_mat['Liar Liar (1997)']
starwars_user_ratings.head()


# In[33]:


similar_to_starwars = movie_mat.corrwith(starwars_user_ratings)
similar_to_liarliar = movie_mat.corrwith(liarliar_user_ratings)
similar_to_starwars.head()


# In[34]:


corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# In[35]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[36]:


corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()


# In[37]:


corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[38]:


corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()

