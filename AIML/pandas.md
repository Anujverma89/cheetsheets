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
