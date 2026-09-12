# Feature Engineering
**EDA**   
**Feature trasnformation**   
**Feature construction**  
**Feature selection**   
**Feature Extraction**



# Feature transformation 
   **Handeling Missing Values**   
       * Dropping  
       * Imputing   
   **Handeling Categorical Values**   
       * Encoding(One hot, label encoding)   
   **Outlier detection**      
   **Feature Scaling**   
       *Standardization (z-score normalizatoin)     
       *Normalization   
# feature of data 
*  accurate 
*  wrong
*  redundant 
*  missing


### feature are tied to a model that is some model perfrom good with some feature and other with other


### main components in ml 
* data : information about something
* model : mathematical realtionship in data
* fature : input to mathematical model 
* preduction : result of model after giving input 


### Feature engineering : Converting raw data into feature 
   * converting raw data into mathematical representation such that it is relvent to task and machine learning model
   * Different model performs better with certain types of features. 
   * So the goal of fe is to develop a feature relvent to ml algorithm
   * not too much not to less but the right balance of feature is good for ml algorithm to perform better.
   
**machine learning models : mathematical formula that maps to a problem statement**   
**feature the input to the mathematical model** 
# Numeric features
* Magnitude
* scale : min and max 
* Distribution of data 

#### smooth functions of input means when input changes the output also changes gradually but not directly
#### In majority of cases input to model is the a vector 


#### Note : 
   * Models which use euclidean distance we have to bring data in a smaller range like rbf, k-means , KNN etc
**scalar : single unit like 3**   
**vector : Ordered list of scalar is called vector**

**vector : [1,2,3,4,5]**
**vectors are input to ml model**
**the aim is to convert raw data into vector**

**Od tensor = scalar**   
**1d tensor = vector**  
**No of elements in vector == dimensions of vector**   
**eg [1,3,4,5] = this is 4d tensor**  
**nd tensors = no of dimension of tensor**   


# binarization : converting values into 1 or zero 
# binning : converting numerical data into cateogrical 
# raw number : same as it was


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import KBinsDiscretizer
df= pd.read_csv("./patient_dataset.csv")

df.head()

titanic_df= pd.read_csv("./titanic.csv")
titanic_df

titanic_df.shape
titanic_df.dropna(inplace = True)


# Feature transformation steps

# 1) Binning
##### here we will bin the data of age into infant, child, adult, aged
#### binning : divides the data into equal groups called bins 
   **UnSupervised binning**  
   * Equal width binning (fixed width binning)
   * quantile binning (variable width binning)
   * k-means binning (forms clusters)
       
   **supervised binning**
   * Decision tree bining
   
#### quantization : it helps to reduce the value by assinging a certain value to one range 
   * suppose the data is between 10-20 then we assign 10 to each value between 10-20 
# binning works here
titanic_df
binner= KBinsDiscretizer(n_bins=4, encode='onehot-dense')
binned = binner.fit_transform(titanic_df[['Age']])
np.array(binned)
# 2)Encoding
### Encoding : converting categorical data into numerical data
   **Ordinal** : data in which order is present  
       *Label: Label encoding*   
   **Nominal** : in which no order is present   
       *OHE: One Hot Encoding*  
# 3)Scaling 
    * It is recomended to do train test splitting before applying feature engineering
    * Process of converting data into normal range by becuse scale of feature is important for many models
* **Nomalization** : 
        ***min-max scaling***   
            * formula : (value - xmin) / (xmax-xmin)    
            * output is always between 0 and 1
        ***mean normalizatoin***          
        ***mean absolute scaling***        
        ***robust scaling***       
        
        
              
* **Standardization(Z-score Normalization)**   
    formula : (value - mean)/ standard deviation      
    mean = 0    
    standard deviation = 1   
    This involves mean centering  
# 4)Handeling Missing values 
### Univariate
    Mean, median, Mode etc 
### Multivariate
    KNN Imputer
    Imputation by chained equation
        1)Iterative imputer
        2)Mice algorithm
# 5)Feature Transformation
   **Changing the distribution of the data**
   **No
   ### 1)Boxcox transformation
   ### 2)Log transformation
   ### 3)Yeo-johnson
   ### 4)Square root transformation
    







# Feature selection steps : 
   ### Wrapper 
     * Forware Selection
     * Backward Selection 
     * Recurssive Feature Elimination
   ### Filter 
     * Pearson's 
     * Kandell tau
     * Spearman's Rho
     * Chi2
     * Muntual Info 
     * F-score 
     * Point-biserial
   ### Embeded 
    * Lasso 
    * Auto encoder with bottleneck 
   ### 1)Forwad selection
   ### 2)Backwards elemination
   ### 3)Bidirectional elemination
   






# Curse of dimentionality 
**Various problem that arises while working with higher dimensional data refers to curse of dimentionality**  
**Neither so much nor so more an optimum no of features are important to give good output**

**So when we have a larage dimentional data there occurs sparsity which reduces the performance**
## So the solution of course of dimentinality is 
   **Dimentionality Reduction Techniques**   
       ***Feature secltion***
           **IN feature selection we select the colunm with more variance in two columns**  
           1.Forware selection  
           2.Backword elimination  
           3.Bidirection Elimination  
       ***Feature Extraction***    
           ***1)PCA  
           2)LDA  
           3)TSNE***  
# PCA (principle Component Analysis)
   **Unsupervised Machine learning algorithm**
   
   1) Convertes the higer dimensions data into lower dimensions data without loosing the esense of the data
   2) If both features have same variance then both of the columns are selected in feature selection
   
   ## Intution 
   **The axises are rotated to form a new principle components**   
   **The axis with heigher variance is accepted as a component**   
   **No of principle componenets is <= n where n is no of initital columns**  
   
   
   **Variance is proporitional to sprad no actually spread**   
   **Variance is important in data to maintain the distance between points**   
   **Distance based algorithm performs well when good variance is present**  
   
   
   ## Working
   **First unit vector is created in a dimension**  
   **Each point it a vector and it is projected in a unit vector**   
   **Now Variance is calculated for every unit vector and one with highest variance becomes principle component** 
   **When a vector is projected on a unit vector it becomes scalar**  
   **u^Tx**  
   **Inshort PCA finds the unit vector which has maximum variance**
# steps : 
    1) Make data a mean centered that is apply stand scalar 
    2) Find a covarinace matrix 
    3) peroform a eigen decompostion 
    4) Find largest eigen vector 
    5) Covarinace matrix = k*K where is k = no of column
    6) No of eignen values == no of columns
    7) Highest eigen value = pc1, sencond eigned value = pc2 and so on
    8) we have to project our points to principle componenets to form  a new dataset 
        Datapoints dotProduct's pca transpose i.e U^T.x
# Step 1 ) Make a data mean centric using standard scalar 
# step 2) Find covariance matrix 
# step 3) Find a eigen vectors and eigen values
# step 4) Data points transposition







# Feature construction 
   **Feature splitting**  
   **Feature Construction**
   **Automatic libraries like**
   * Pycaret
   * Optuna
   * feature-engine
   * Explore-kit   
import pandas as pd

df = pd.read_csv("./patient_dataset.csv")
df.head()
### Creating a feature from existing feature
### Splitting the already existing feature 
#### This is the manual process and it takes time 
###### this also increases the performance

