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
