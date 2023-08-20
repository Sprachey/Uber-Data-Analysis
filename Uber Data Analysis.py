# %% [markdown]
# ### Importing Libraries

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# %% [markdown]
# ### Reading Data
# 

# %%
data=pd.read_csv("uber data\UberDataset.csv")

# %%
data.head()

# %%
data.shape

# %%
data.columns

# %%
data.describe()

# %%
data.info()

# %%
data.info()

# %% [markdown]
# ### Check for null values

# %%
data.isna().values.any()

# %%
data.isna().sum()

# %% [markdown]
# ### Removing null values

# %%
columns_to_drop=data.columns.drop('PURPOSE')
data.dropna(subset=columns_to_drop,inplace=True)


# %% [markdown]
# ### Replacing Wrong Values

# %%
data['START'] = data['START'].replace("Kar?chi", "Karachi")
data['STOP'] = data['STOP'].replace("Kar?chi", "Karachi")

# %% [markdown]
# ### Converting dates to datetime datatype

# %%
data["START_DATE"]=pd.to_datetime(data["START_DATE"])
data["END_DATE"]=pd.to_datetime(data["END_DATE"])

# %% [markdown]
# ### Analysis

# %%
print("Maximum Miles for a ride:",data["MILES"].max(),"miles")
print("Minimum Miles for a ride:",data["MILES"].min(),"miles")
print(f"Average Miles for a ride: {data['MILES'].mean():.3} miles")

# %%
print("Top Start Station:",data["START"].mode()[0])
print("Top Stop Station:",data["STOP"].mode()[0])

# %%
data["START"].value_counts()[:10]

# %%
columns_to_check = ['CATEGORY' , 'PURPOSE']

for column in columns_to_check:
    distinct_values = data[column].unique()
    print(f"Distinct values in '{column}':")
    print(distinct_values)
    print()

# %% [markdown]
# ### Trips by Category

# %%
cat=data["CATEGORY"].value_counts()
fig=px.pie(labels=cat.index,values=cat.values,title="Category",names=cat.index,color_discrete_sequence=px.colors.sequential.Sunsetdark)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# %%
plt.figure(figsize=(8, 6))
sns.barplot(x=cat.index, y=cat.values)
plt.xlabel("Category")
plt.ylabel("Trips")
plt.title("Bar Plot of Trips by Category")
plt.show()

# %% [markdown]
# ### Trips by Purpose

# %%
pur=data["PURPOSE"].value_counts()
fig=px.pie(labels=pur.index,values=pur.values,title="Purpose",names=pur.index,color_discrete_sequence=px.colors.sequential.Aggrnyl)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# %%
plt.figure(figsize=(8, 6))
sns.barplot(x=pur.index, y=pur.values)
plt.xlabel("Purpose")
plt.ylabel("Trips")
plt.xticks(rotation=45)
plt.title("Bar Plot of Trips by Purpose")
plt.show()

# %% [markdown]
# ### Average Miles by Purpose
# 

# %%
miles_pur=data.groupby("PURPOSE",as_index=False)["MILES"].mean()
plt.figure(figsize=(8, 6))
sns.barplot(x="PURPOSE", y="MILES", data=miles_pur)
plt.title("Average Miles by Purpose", fontsize=14)
plt.xlabel("Purpose", fontsize=14)
plt.ylabel("Average Miles", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### Average Miles by Category

# %%
miles_cat=data.groupby("CATEGORY",as_index=False)["MILES"].mean()
plt.figure(figsize=(8,6))
sns.barplot(x=miles_cat["CATEGORY"],y=miles_cat["MILES"])
plt.title("Average Miles by Category",fontsize=14)
plt.xlabel("Category",fontsize=14)
plt.ylabel("Averae Miles",fontsize=14)
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### Station Performance

# %%
top_start_stations=data["START"].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=top_start_stations.index[:10], y=top_start_stations.values[:10])
plt.title("Top 10 Start Stations", fontsize=14)
plt.xlabel("Stations", fontsize=14)
plt.ylabel("Counts", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# %%
top_stop_stations=data["STOP"].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=top_stop_stations.index[:10], y=top_stop_stations.values[:10])
plt.title("Top 10 Stop Stations", fontsize=14)
plt.xlabel("Stations", fontsize=14)
plt.ylabel("Counts", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# %%
top_start_stations=data["START"].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=top_start_stations.index[-10:], y=top_start_stations.values[-10:])
plt.title("Least 10 Start Stations", fontsize=14)
plt.xlabel("Stations", fontsize=14)
plt.ylabel("Counts", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# %%
top_stop_stations=data["STOP"].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=top_stop_stations.index[-10:], y=top_stop_stations.values[-10:])
plt.title("Least 10 Stop Stations", fontsize=14)
plt.xlabel("Stations", fontsize=14)
plt.ylabel("Counts", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# ### Ride Duration

# %%
data['ride_duration'] = data['END_DATE'] - data['START_DATE']
min_duration = data['ride_duration'].min()
max_duration = data['ride_duration'].max()
average_duration = data['ride_duration'].mean()

print("Minimum ride duration:", min_duration)
print("Maximum ride duration:", max_duration)
print("Average ride duration:", average_duration)

# %%
sns.histplot(data['ride_duration'].dt.total_seconds() / 60, bins=30) 
plt.xlabel('Ride Duration (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Uber Ride Durations')



