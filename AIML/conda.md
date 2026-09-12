# Conda
##### Conda is a package management tool generally used with python and r language 
* Anaconda (anaconda-navigator) : Contains 300+ packages and also a gui to work with.
* Miniconda : Contains only conda , python and other depnedencies that are needed for them.

`conda comes installed with both miniconda and anaconda`

|Working with conda CLI| cmd |
|---|---
`create new env` | `conda create -n envname` |
`activate new env` | `conda activate env_name`|
`get env info` | `conda env list`, `conda info --envs`,`conda info -e`
`get version` | `conda --version`
`search package` | `conda search scipy`
`install package` | `conda install numpy`
`build package` | `conda build package`

![conda0](./conda1.png)
![conda1](./conda2.png)
![conda2](./conda3.png)
![conda3](./conda4.png)
![conda4](./conda5.png)
![conda5](./conda6.png)


### Installation of miniconda
* You can install the .sh file 
* verify the sha key
* install the miniconda using bash filename.sh
* read instruction and follow the commands
* add conda to path ~/.bashrc okay 
* after this you are done
* run source ~/.bashrc -- to reaload terminal

### install jupyter
* conda install jupyter
* conda init
* source ~/.bashrc 
* conda create -n newenv
* conda activate 
* conda activate env 
* jupyter notebook