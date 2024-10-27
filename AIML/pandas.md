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
| function and attributes | use | code |
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
| df.head() | print first 5 rows | df.head(no_of_row_to_print) |
| df.tail() | print last 5 rows | df.tail(no_of_rows_to_print) |
| df['newcolumn'] = new value | to add new column to dataset | df['newcolumn'] = np.arange(10) |
| df.describe() | print statistical values about dataset | df[columnname].describe() |
| df.info() | get information about dataset like datatype and null and not null | df.info() |
| df.index | to get index info like min max | df.index |
| df.index.value | to get all the indexes present in df | df.index.value |
| df.to_numpy() | to convert data set into numpy array | df.to_numpy() |
| df.DataFrame(data, index, columns) | to create pandas dataframe | pd.DataFrame(list or dict, columns= [], index = something) |
| df.keys | gives name of all the columns along with data | df.keys|
| df.insert(position_to_insert, 'column_name', vlaue=[1,2,4,5,]) | insert column into dataset at specified location | anddf.insert(1,"new",[45,34,56,77]) |
| df.corr() | to find the corelation among numerical features of dataset  only applied on numerical features not on textual| df.corr() |
















