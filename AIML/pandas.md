# Pandas
**Pandas is python library used for data manipulation and analysis it's alternate are SAS, STATA, Excel, SQL**

**TUTORIAL**  
*DataFram is a two dimensional datastrucutre that can store int, character, floating point , categorial and more*   
*Every column is series*  
*Cleaning data is called data munging or data wrangling*
*we can use python dictionaries and python list to create pandas dataframe*
*df.iloc - works with index*  
*df.loc - works with lables*    
*Index is column that is used to access the row items*  
*The items present in index is used to access the list*  
*Index is something that is used to access the row items*  



# this way we can create dataframe here distinoary key becomes column
```py
import pandas as pd
anddf = pd.DataFrame({
                "name":["anuj","akshand","rahul","vivek"],
                "age":[22,21,21,22]
})
series = pd.Series([22,23,24],name='age')
# series doesnot have the name of the colum
df.describe() #is used to print the statistics
df['age'].max() # gives max in age
df['age'].min() # gives you min

df.loc[['age','roll']] #gives dataframe
df.iloc[:1,:1]]
anddf.loc[[1,2],['age','name']] # use to work with label based index also known as column based index.
anddf.fillna(df['age'].mean()) # filling the none value with mean

```

### Handeling missing values 
| function | use | code |
|-|-|-|
|pd.read_csv("complatepathoffile.csv") | load csv file | pd.read_csv('filename.csv') |
|df.to_excel('filename.xlsx') | dump some data to file | df.to_excel('filename.xlxs') |
|df.dropna()| drop rows with null value | df.dropna() |
|df.is_null() | find out if value is null | df.is_null()|
|df.is_unique() | find out unique values | df.is_unique() |
|df['column'].value_count() | to get unique values & their counts | df['sex'].value_count() |
|df.fillna(df['age'].mean()) | fill null values with mean | df.fillna(value) |
|df.iloc[:,:,:] | used for slicing and indexing | df.iloc[:1,:3] | 
|df.loc[index_value] | used to access columns using row | df.loc[[1,2,3],['age','sex','name']]|













