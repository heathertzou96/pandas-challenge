#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[317]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[200]:


unique_players = purchase_data["SN"].unique()
total_players = len((unique_players))
total_players
#easier way: total_players = len(purchase_data["SN"].value_counts())

total_players_df = pd.DataFrame({"Total Players": [total_players]})
total_players_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[203]:


unique_items = len(purchase_data["Item ID"].value_counts())
unique_items

total_price = purchase_data["Price"].sum()
avg_price = total_price / len(purchase_data)
avg_price

total_revenue = avg_price * len(purchase_data)
total_revenue

total_purchase_summary = pd.DataFrame(
    {"Number of Unique Items" : [unique_items],
     "Average Price" : [avg_price],
     "Number of Purchases" : len(purchase_data),
     "Total Revenue" : [total_revenue]
    }
)

total_purchase_summary["Average Price"] = total_purchase_summary["Average Price"].map("${:.2f}".format)
total_purchase_summary["Total Revenue"] = total_purchase_summary["Total Revenue"].map("${:.2f}".format)

total_purchase_summary.head()


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[202]:


grouped_gender = purchase_data.groupby(["Gender"])

gender_count = grouped_gender["SN"].nunique() #count distinct observations over requested axis and return Series with number of distinct observations
gender_count

male_count = gender_count[1] #getting element at the specified index in series
female_count = gender_count[0]
other_count = gender_count[2]

male_percentage = (male_count / total_players) * 100
female_percentage = (female_count / total_players) * 100
other_percentage = (other_count / total_players) * 100

gender_summary = pd.DataFrame(
    {"": ["Male", "Female", "Other / Non-Disclosed"],
     "Total Count": [male_count, female_count, other_count],
     "Percentage of Players": [male_percentage, female_percentage, other_percentage]
    }
)

gender_summary["Percentage of Players"] = gender_summary["Percentage of Players"].map("{:.2f}%".format)

gender_summary = gender_summary.set_index("")

gender_summary


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[264]:


#grouped_gender = purchase_data.groupby(["Gender"])

purchase_count = grouped_gender["Item ID"].count()
purchase_count

#purchase_price = grouped_gender["Price"].value_counts()
#purchase_price
total_purchase_price = grouped_gender["Price"].sum()
total_purchase_price
avg_purchase_price = total_purchase_price / purchase_count
avg_purchase_price

total_purchase_value = purchase_count * avg_purchase_price
total_purchase_value

avg_total_purchase = total_purchase_value / gender_count
avg_total_purchase

gender_purchase_summary = pd.DataFrame(
    {"Purchase Count": purchase_count,
     "Average Purchase Price": avg_purchase_price,
     "Total Purchase Value": total_purchase_value,
     "Avg Total Purchase per Person": avg_total_purchase
    }
)

gender_purchase_summary["Average Purchase Price"] = gender_purchase_summary["Average Purchase Price"].map("${:.2f}".format)
gender_purchase_summary["Total Purchase Value"] = gender_purchase_summary["Total Purchase Value"].map("${:.2f}".format)
gender_purchase_summary["Avg Total Purchase per Person"] = gender_purchase_summary["Avg Total Purchase per Person"].map("${:.2f}".format)

gender_purchase_summary


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[259]:


bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 100]
bins_label = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins, labels = bins_label)

grouped_age = purchase_data.groupby(["Age Group"])

age_group_count = grouped_age["SN"].nunique()
age_group_count

age_group_percentage = (age_group_count / total_players) * 100
age_group_percentage

age_summary = pd.DataFrame(
    {"Total Count": age_group_count,
     "Percentage of Players": age_group_percentage,
    }
)

age_summary["Percentage of Players"] = age_summary["Percentage of Players"].map("{:.2f}%".format)

age_summary


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[301]:


#grouped_age = purchase_data.groupby(["Age Group"])
grouped_age.count().head()

age_purchase = grouped_age["Purchase ID"].count()
age_purchase

avg_age_purchase = grouped_age["Price"].mean()
avg_age_purchase

total_age_purchase = age_purchase * avg_age_purchase
total_age_purchase

age_count = grouped_age["SN"].nunique() 
avg_total_age_purchase = total_age_purchase / age_count
avg_total_age_purchase

age_purchase_summary = pd.DataFrame(
    {"Purchase Count": age_purchase,
     "Average Purchase Price": avg_age_purchase,
     "Total Purchase Value" : total_age_purchase,
     "Avg Total Purchase per Person": avg_total_age_purchase
    }
)

age_purchase_summary["Average Purchase Price"] = age_purchase_summary["Average Purchase Price"].map("${:.2f}".format)
age_purchase_summary["Total Purchase Value"] = age_purchase_summary["Total Purchase Value"].map("${:.2f}".format)
age_purchase_summary["Avg Total Purchase per Person"] = age_purchase_summary["Avg Total Purchase per Person"].map("${:.2f}".format)                                                                                                        

age_purchase_summary


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[344]:


grouped_SN = purchase_data.groupby(["SN"])

spender_purchase = grouped_SN["Purchase ID"].nunique()
spender_purchase

avg_spender_purchase = grouped_SN["Price"].mean()
avg_spender_purchase

total_spender_purchase = spender_purchase * avg_spender_purchase
total_spender_purchase

spender_summary = pd.DataFrame(
    {"Purchase Count": spender_purchase,
     "Average Purchase Price": avg_spender_purchase,
     "Total Purchase Value" : total_spender_purchase,
    }
)

spender_summary

topspender_summary = spender_summary.sort_values("Total Purchase Value", ascending = False)

topspender_summary["Average Purchase Price"] = topspender_summary["Average Purchase Price"].map("${:.2f}".format)
topspender_summary["Total Purchase Value"] = topspender_summary["Total Purchase Value"].map("${:.2f}".format)
topspender_summary.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[357]:


grouped_item = purchase_data.groupby(["Item ID", "Item Name"])
grouped_item.count().head()

popular_purchase = grouped_item["Purchase ID"].count()
popular_purchase 

popular_price = grouped_item["Price"].mean()
popular_price

total_popular_purchase = popular_purchase * popular_price

popular_summary = pd.DataFrame(
    {"Purchase Count": popular_purchase,
     "Item Price": popular_price,
     "Total Purchase Value": total_popular_purchase
    }
)

mostpopular_summary = popular_summary.sort_values("Purchase Count", ascending = False)

mostpopular_summary["Item Price"] = mostpopular_summary["Item Price"].map("${:.2f}".format)
mostpopular_summary["Total Purchase Value"] = mostpopular_summary["Total Purchase Value"].map("${:.2f}".format)

mostpopular_summary.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[362]:


mostprofitable_summary = popular_summary.sort_values("Total Purchase Value", ascending = False)

mostprofitable_summary["Item Price"] = mostprofitable_summary["Item Price"].map("${:.2f}".format)
mostprofitable_summary["Total Purchase Value"] = mostprofitable_summary["Total Purchase Value"].map("${:.2f}".format)

mostprofitable_summary.head()


# In[ ]:




