# Fish Species Classification

The goal of this notebook is the application of classification techniques to classify different type fishes around in the market for sale.

A multi-class classification problem to detect the type of fish in the given dataset.[Fish_Dataset.csv]

You can check out the working code of this application hosted on the below url on Heroku:
https://fish-species-ml.herokuapp.com/

## Installation

**Installing Python**

Make sure that you have [Python3 installed](https://realpython.com/installing-python/) on your machine.

Depending on your installation you might have access to Python3 interpreter either by
running `python` or `python3`. The same goes for pip package manager - it may be accessible either
by running `pip` or `pip3`.

You may check your Python version by running:

```bash
python --version
```

Note that in this repository whenever you see `python` it will be assumed that it is Python **3**.

**Installing dependencies**

Install all dependencies that are required for the project by running:

```bash
pip install -r requirements.txt
```
Also you might want to install jupyter to access the notebook in the repository.

## Dataset

The dataset is included in the repository with file names *Fish_Dataset.csv*
You can also visit the [dataset](https://www.kaggle.com/aungpyaeap/fish-market)

Missing attribute values: none

Class distribution: 357 benign, 212 malignant
## Attributes in the dataset

    6 features are used, examples:

      - Weight
      - Length1
      - Length2
      - Length3
      - Height
      - Width 

    Datasets are linearly separable using all 6 input features
    Total Number of Instances: 159
    Target class: Species 
    Unique Labels: 7
    

## Usage

You would need to clone the repo to access all the contents
```
git clone https://github.com/MohseenShaikh/Fish-Species-Classification

```

Install all the dependencies using the environment manager or using the `pip install requirements.txt` command

Access the Fish Species Classification.ipynb.ipynb notebook which contains the source code for feature selection and modelling

## Implementation

The dataset was divided into training and testing data with the test size of 20%

We have used Logistic Regression and Neural Network to classify and predict which class species label from given test data

After training the data we have calculted the accuracy for each model and saved the latest model for future use as a `pickel` file named `model.pkl`


# Credits

  - Mohseen Shaikh
  - Noopa Jagadeesh 
  
# License 

  This is released under the MIT License. http://www.opensource.org/licenses/mit-license

# Contribution

Feel free to raise any issue at this repository or please raise pull request to incorporate changes
