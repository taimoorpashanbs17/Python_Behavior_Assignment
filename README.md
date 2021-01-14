# Python_Behavior_Assignment
This is Testing Sample App for working on Python 

To Run this Project within you system, following requirements are needed:

1. Windows or Linux Operating Systems
2. Python3.x installed (3.8 recommended)
3. Git Installed
4. Chrome version 87

## Installation 

### 1.  Install virtual Environment

Create Virtual Environment on same folder where project has been cloned.

#### Windows:

Open Command Line or Powershell(Recommend):

`py -m pip install --user virtualenv`

#### Linux:

Open Terminal and Type:

`python3 -m pip install --user virtualenv`

### 2.  Create virtual Environment
Let's just say that environment name is 'env'

Windows:

`py -m venv env`

Linux:

`python3 -m venv env`


### 3. Activate Virtual Environment
Windows:

`.\env\Scripts\activate`

Linux:

`source env/bin/activate`

### 4.  Install all requirements

Install all dependencies using following command:

`pip install -r requirements.txt`

Now all dependencies will be stored within virtual environment


## 3. Run Test Cases

Now it depends on what is the scenario, running whole suite or individual scenarios

### Running Whole Suite

`behave features/`