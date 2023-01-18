# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:37:19 2022

@author: Divya
"""
# libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
import missingno as msno


df = pd.read_csv(r"C:\Pandas project\bestsellers with categories.csv")

df.head()

df.info()

df.isnull().sum()


#plt.figure(figsize=(7,5))
n = msno.bar(df,color = "crimson",figsize=(12,6),fontsize=10) # there is no null value


# Name of the Authors with highest number of published Books
plt.style.use("ggplot")
plt.rcParams["figure.figsize" ]= (12,7)
#color = plt.cm.hsv(np.linspace(0,1,15))
df["Author"].value_counts().sort_values(ascending=False).head(15).plot.bar()#color=color
plt.title("Top 15 Authors with highest number of Books Published (2009-2019)",fontsize=20)
plt.xlabel("Authors",fontsize=15)
plt.ylabel("No. of Books",fontsize=15)
plt.show()


# Count of published Genre
plt.style.use("ggplot")
plt.rcParams["figure.figsize" ]= (9,6)
#color = ["purple","yellowgreen"]#plt.cm.BuPu(np.linspace(0,1,15))
df["Genre"].value_counts().sort_values(ascending=False).head(15).plot.bar()#color=color
plt.title("No. of published Genre(2009-2019)",fontsize=20)
plt.xlabel("Genre",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.show()

df["Genre"].value_counts()


# Books with Highest number of Reviews
df[["Name","Reviews","User Rating"]].nlargest(5,"Reviews")


# Top 20 Books with Highest number of Reviews
plt.rcParams["figure.figsize"] = (16,5)
#color = plt.cm.BuPu(np.linspace(0,1,20))
df[["Name","Reviews"]].nlargest(20,"Reviews").plot.bar(x="Name",y="Reviews",width=0.4,)#'vertical', 'horizontal',color=color
plt.title("Top 20 Books with highest number of Reviews",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("No.of Reviews",fontsize=15)
plt.show()


# Best selling Fiction books according to Reviews
plt.rcParams["figure.figsize"] = (16,5)
#color = plt.cm.BuPu(np.linspace(0,1,20))
df[df["Genre"] == "Fiction"].nlargest(10,"Reviews").plot.bar(x="Name",y="Reviews",width=0.4,)#'vertical', 'horizontal',color=color
plt.title("Top 10 bestselling Fiction books according to Reviews(2009-2019)",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("No.of Reviews",fontsize=15)
plt.show()
# So Top reviewed Fiction book is 'Where the Crawdads Sing' with 87841 reviews


# Best selling Non Fiction books according to Reviews
plt.rcParams["figure.figsize"] = (16,5)
#color = plt.cm.BuPu(np.linspace(0,1,20))
df[df["Genre"] == "Non Fiction"].nlargest(10,"Reviews").plot.bar(x="Name",y="Reviews",width=0.4,)#'vertical', 'horizontal',color=color
plt.title("Top 10 bestselling Non Fiction books according to Reviews(2009-2019)",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("No.of Reviews",fontsize=15)
plt.show()
# So Top reviewed Non Fiction book is 'Becoming' with 61133 reviews


# Most expensive Fiction books
expensive = df[df["Genre"] == "Fiction"].nlargest(10,"Price")
p = expensive["Price"]
plt.rcParams["figure.figsize"] = (16,5)
#color = plt.cm.BuPu(np.linspace(0,1,20))
df[df["Genre"] == "Fiction"].nlargest(10,"Price").plot.bar(x="Name",y="Price",width=0.4,)#'vertical', 'horizontal',color=color
for i,price in enumerate(p):
    plt.text(i,price,str(price),fontsize=12)
plt.title("Top 10 Most expensive Fiction books(2009-2019)",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("Price",fontsize=15)
plt.show()
# So The Twilight Saga is the most expensive Fiction Book


# Most expensive Non Fiction Books
expensive = df[df["Genre"] == "Non Fiction"].nlargest(10,"Price")
p = expensive["Price"]
plt.rcParams["figure.figsize"] = (16,5)
#color = plt.cm.BuPu(np.linspace(0,1,20))
df[df["Genre"] == "Non Fiction"].nlargest(10,"Price").plot.bar(x="Name",y="Price",width=0.4,)#'vertical', 'horizontal',color=color
for i,price in enumerate(p):
    plt.text(i,price,str(price),fontsize=12)
plt.title("Top 10 Most expensive Non Fiction books(2009-2019)",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("Price",fontsize=15)
plt.show()
# So Diagnostic and Statistical Manual of Mental Disorders,5th edition is the most expensive Non Fiction Book


# Top 20 Books according to price
plt.rcParams["figure.figsize" ]= (16,5)
#color = plt.cm.PuRd(np.linspace(0,1,20))
df[["Name","Price"]].nlargest(20,"Price").plot.bar(x="Name",y="Price")#'vertical', 'horizontal',,color=color
plt.title("Top 20 Books with highest Price",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("Price",fontsize=15)
plt.show()


# Percentage of Genres Among Best Selling Books
plt.rcParams["figure.figsize"]= (10,8)
plt.style.use("classic")
color = ["Gold","yellowgreen"]
labels = ["Non Fiction","Fiction"]
df["Genre"].value_counts().plot.pie(y = "Genre",startangle = 70,explode = (0,0.05),shadow=True,colors = color,autopct="%0.1f%%")
plt.title("Percentage of Genres Among Best Selling Books ",fontsize=20)
plt.legend(labels,loc="best")
plt.axis("off")
plt.show()


# Mean User Rating according to Genre
mean_rate = df.groupby(["Genre"],as_index=False)["User Rating"].mean()#,as_index=False
#df.groupby(['Genre'])['Weighted Rating'].mean()
mean_rate

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize =(9, 6))   
# Horizontal Bar Plot 
#color = ["yellowgreen","purple"]
ax.bar(mean_rate["Genre"],mean_rate["User Rating"])#,color = color 

# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_x()+0.4,i.get_height()+0.2,   
             str(round((i.get_height()), 3)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
plt.title("Average User Rating according to Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.show()
# On average Fiction gets higher rating than Non Fiction


# Trend
# Trend (Fiction)
year = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
num_fic= []
for i in year:
    fic = df[(df["Year"] == i) & (df["Genre"] == "Fiction")]
    num_fic.append(len(fic))
df_fict = pd.DataFrame({"Year": year,"numberofFiction": num_fic})
df_fict.head()

# Trend (Non Fiction)
year = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
num_nonfic= []
for i in year:
    nonfic = df[(df["Year"] == i) & (df["Genre"] == "Non Fiction")]
    num_nonfic.append(len(nonfic))
df_nonfict = pd.DataFrame({"Year": year,"numberofNonFiction": num_nonfic})
df_nonfict.head()

df_nonfict["numberofFiction"] = df_fict["numberofFiction"]
df_nonfict.head()

df_genre = df_nonfict.copy()
df_genre.head()

# Non fiction
plt.style.use("ggplot")
plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
plt.bar(x = df_genre["Year"],height=df_genre["numberofNonFiction"],)
plt.plot(df_genre["Year"],df_genre["numberofNonFiction"],"bo-")
#plt.plot(df_genre["Year"],df_genre["numberofFiction"],"ro-")
plt.title("Trend of having NonFiction on BestSeller Books List(2009-2019)")
plt.xlabel("Year")
plt.ylabel("No. of NonFiction published")

# Fiction
plt.subplot(1,2,2)
plt.bar(x = df_genre["Year"],height=df_genre["numberofFiction"],)
plt.plot(df_genre["Year"],df_genre["numberofFiction"],"bo-")
plt.title("Trend of Having Fiction on BestSeller Books List(2009-2019)")
plt.xlabel("Year")
plt.ylabel("No. of Fiction published")
plt.show()

plt.style.use("ggplot")
plt.figure(figsize=(16,5))
#plt.subplot(1,1,1)
width = 0.4
plt.bar(x = df_genre["Year"]-width,height=df_genre["numberofNonFiction"],label = "Non Fiction")
plt.bar(x = df_genre["Year"]+width,height=df_genre["numberofFiction"],label = "Fiction")

#plt.plot(df_genre["Year"],df_genre["numberofNonFiction"],"bo-")
#plt.plot(df_genre["Year"],df_genre["numberofFiction"],"go-")
#plt.xlabel("Year")
#plt.ylabel("No. of Books Published")
#plt.legend()
#plt.show()


# Reviews according to Year & Genre
genre_reviews = df.groupby(["Genre","Year"],as_index=False)["Genre","Reviews"].mean()#,as_index=False
genre_reviews.head()

plt.figure(figsize=(12,6))
plt.style.use("ggplot")
sns.barplot(x ="Year",y="Reviews",hue = "Genre",data = genre_reviews)
plt.title("No. of Reviews according to Year & Genre") #,Fontsize=20
plt.show()
# Fiction Books always gets highest reviews except year 2018


# Average User Rating according to Year & Genre
genre_ratings = df.groupby(["Genre","Year"],as_index=False)["Genre","User Rating"].mean()#,as_index=False
genre_ratings.head()

plt.figure(figsize=(12,6))
plt.style.use("ggplot")
sns.barplot(x ="Year",y="User Rating",hue = "Genre",data = genre_ratings)
plt.title("Average rating according to Year & Genre") #,Fontsize=20
plt.show()

# Year 2019 Analysis
df_19 = df[df["Year"] == 2019]
df_19.head()

# Top 20 Books with highest number of Ratings in 2019
plt.rcParams["figure.figsize" ]= (12,7)
#color = plt.cm.PuRd(np.linspace(0,1,20))
df_19[["Name","User Rating"]].nlargest(20,"User Rating").plot.bar(x="Name",y="User Rating")#'vertical', 'horizontal',,color=color
plt.title("Top 20 Books with highest Ratings(2019)",fontsize=20)
plt.xlabel("Name of the Books",fontsize=15)
plt.ylabel("User Rating",fontsize=15)
plt.show()

# Authors who published more than 1 books in 2019
#plt.style.use("classic")
plt.rcParams["figure.figsize" ]= (8,6)
#color = ["yellowgreen","purple"]#plt.cm.BuPu(np.linspace(0,1,7))
df_19["Author"].value_counts().sort_values(ascending=False).head(2).plot.bar()#color=color
plt.title("Authors who published  more than 1 books in 2019")
plt.xlabel("Authors")
plt.ylabel("No. of Books Published")
plt.xticks(rotation=0)
plt.show()
# Dav Pilkey published highest number of Books which is 3 in 2019

# Name of the Books which Dav Pilkey Published in 2019
df_19[df_19["Author"] == "Dav Pilkey"]

# Number of each Genre published in 2019
plt.rcParams["figure.figsize" ]= (8,6)
#color = ["yellowgreen","purple"] #plt.cm.hsv(np.linspace(0,1,15))
df_19["Genre"].value_counts().plot.bar()#sort_values(ascending=False).head(15).,color=color
plt.title("No. of each Genre published in 2019")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation =0)
plt.show()

# Books with highest reviews in 2019
plt.rcParams["figure.figsize"] = (16,8)
#color = plt.cm.PuRd(np.linspace(0,1,10))
df_19[["Name","Reviews"]].nlargest(10,"Reviews").plot.bar(x="Name",y="Reviews")#,color=color
plt.title("Top 10 Books with highest number of Reviews(2019)")
plt.xlabel("Name of the Books")
plt.ylabel("No.of Reviews")
plt.xticks()
plt.show()


#-------------1st Method--------------#
x=df.loc[(df.author=="Stephenie Meyer")&(df.genre=="Fiction")]
m=df.loc[((df.ratings>=4.5)|(df.ranks<=3))&(df.year==2021)]
a=df.loc[(df.year==2018)&(df.genre=="Non Fiction")]

#--------------QUERY-------------#
y=df.query("(author=='Stephenie Meyer')&(genre=='Fiction')")

t=df.query("(title=='The Legend of Zelda: Hyrule Historia')")

i=df.query("(year==2013)&(genre=='Fiction')")
i.count()


df.drop('Unnamed: 0',inplace=True,axis=1)
df.info()

b=df.query("(ranks==1)")

c=df.query("(author=='Joanna Gaines')&(year==2018)")

e=df.query("(year==2021)&(genre=='Non Fiction')&(ratings>=4.5)")
e.count()
e.price.max()
e.price.min()
e.author.unique()
a=e.query("(price==2.88)&(ratings==4.8)")
h=df.query("(author=='Scholastic Teacher Resources')")


j=df.author.unique()
df.price.min()
a1=df.query("(year>=2009)&(ratings>=4.5)&(price<=3)")
a2=a1.query("(ratings==4.9)")
a3=df.query("(author=='Dav Pilkey')")
a3.count()
a4=a3.query("(ranks<=10)")


x=df.query("(ratings==4.9)")
x.count()
x1=x.query("(ranks<=5)&(genre=='Fiction')")


df.price.max()
g=df.query("(price==144&(year==2015))")

df.reviews.max()
f=df.query("(reviews==344811.0)&(year==2018)")



#--------------3rd Method-------------#
p=df.eval("(author == 'Stephenie Meyer')&(genre == 'Fiction')")
#--------------4th Method-------------#
df.loc[(df["author"]=='Stephenie Meyer')&(df["genre"]=='Fiction'),"Fiction"] = "F"
df

df.columns
df.shape
df.price.mean()
df.price.mode()
df.price.median()

p=df.duplicated()

df.rename(columns={"price":"amount","no_of_reviews":"reviews"},inplace=True)
df
i=df.set_index("title",inplace=True)
# df.drop_duplicates()
df.drop([1,2],inplace=True)
# df.dropna(how='all')

