# Machine Learning 

**Application of computer Artifical Intelligence which tries to mimmic the human intelligence and the precit the outcome using past data i.e. derive inference using past data**

### Types : 
* `Supervised`
  * Regression
      * Simple Linear Regression 
      * Multiple Linear Regression
      * Polynomial Linear Regression (Works fine even on non linear data)
      * Decision Trees
      * SVM Support vector machines
      * Random Forest (ensemble Learning Bagging)
      * Gradient Boosting (Ensemble Learning Boosting)
      * L1(lasso Regression) Normalization technique
      * L2(Ridge Regression) Normalization technique
      * Elasticnet Regression Normalization Technique
  * Classification :
      * Logistic Regression
      * Softmax Logistic Regression Or Multinomail Logistic Regressoin 
      * Decision Tress
      * SVM
      * Random Forest (Bagging)
      * Gradient Boosting (Ensemble Learning Boosting)
      * Naive Bayes Classifier
      * LDA (Linear discriminant Analysis)
      * KNN (K-nearest Neighbour)
   
* `Unsupervised`
  * Clustring
      * K-means clustring
      * DBSCAN
      * XGBOOST 
  * Association
  * Dimentionality Reduction
      * PCA (principal Component Analysis)
      * TSNE (T - Distributed Stochastic Neighbour Embedding) 
   
* `Semi-Supervised`
* `Reinforcement learning`
    * Q-learning


### Ensemble Learning 
* Combining Multiple models to predict the result to enhance the performance of the machine learning model*   
#### Types :  
* `Voting` : Heterogeneous ensemble techqnique where different models are trained on same dataset and the result which is predicted by most model is the output.  
 
* `Bagging` (Bootstrapped aggrigation) : Different instance of same model is tranined with different subset of data. In case of regression means of output from different model is output and in case of classification the mode of the result i.e. result from maximum models is output.   
  * Subset is taken using two techniques :
    * with replacement ( Duplicate rows are possible)
    * without Replacement ( Duplicate rows are not possible)

* `Boosting` : Ensemble learning model where weight is assigned to different models it is sequential in nature. Same data is given to different instance of same model. The output of one model instance if input to another model instance with flaw which is corrected by the other model.




### Types of functions in machine learning 
| Function | Type | use | 
|-|-|-|
| Adam | optimization | minimize loss function | 
| adagrad | optimization | same is above | 
| nestrov | same as above | same as above | 
| Gradient Descent | same | same | 
| Stochastic GD | same | same | 
| Batch GD | same | Same | 
| Mini Batch GD | Same | same | 
| RMSprop | Same | same | 
| SGD with momentum | Same | same | 
| Step | Activation Function | To convert output into desired format | 
| Sigmoid | same | same | 
| Relu | same | same | 
| Leaky Relu | same | same | 
| Tanh | same | same | 
| Linear (No activation | same | same | 
| Softmax(version of sigmoid) | same | same | 
| MSE | Loss function | Used to measure loss in regression  | 
| MAE | same | same | 
| RMSE | same | same | 
| Huber loss | same | same | 
| Log loss | same | used to measure loss in classification  | 
| Cross entropy | same | same | 
| Binary cross entropy | same | two class classification | 
| Categorical Cross entropy | same | multi class classification 
| Hinge loss | same | Used in SVM | 

### Gradient Descent : 
* Gradient Descent is an optimization technique that is used to optimize the loss function. There are mainly three type of gradient descent*
   * Batch Gradient Descent
   * Stochastic Gradient Descent
   * Mini Batch Gradient Descent
   * `Formula weight_new= weight_old - Learning_rate * Slope of loss function with respect to given weight`





