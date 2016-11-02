# Cookiecutter Data Science Template

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._
 
Based on http://drivendata.github.io/cookiecutter-data-science/  
Adapted for minimalist purposes.  
Optimized for Python projects, can also be used with R.

### Requirements 
To use the cookiecutter template, you will need the following packages installed:
* Python 2.7 or 3.5
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:
 
``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

NB. We will try to make the `cookiecutter` package installed by default.


## How to start a new project
First `cd` to your desired projects dir. We recommend using a dir called `projects` where you store all your repos.
``` bash
mkdir ~/projects
cd ~/projects
```
Install the cookiecutter data science template, be referring to the Gitlab repo:
``` bash
cookiecutter https://github.com/BigDataRepublic/cookiecutter-data-science.git --checkout minimal
```
You will be prompted to fill in some info, such as the project name, repository name, description, etc.
  
Next, create a new empty repo named accordingly and follow these steps to link the new project dir:  

``` bash
cd {repo-name}
git init
git remote add origin git@{repo-host}:{username-or-organization}/{repo-name}.git
git add -A
git commit -m 'initial commit'
git push -u origin master
```

You're good to go!


