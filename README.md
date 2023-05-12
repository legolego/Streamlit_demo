# Example connecting to Streamlit cloud from Deepnote through Github


## Description

This will use a single, shared ```requirements.txt``` file. It will be shared between Deepnote, through the init file, and Streamlit, 
which requires ```requirements.txt``` to load libraries it needs.
This repo was made to show was how to reference a file in both Deepnote ans Streamlit, as well as a convenient file structure to use in Deepnote.

### Deepnote file structure

![Deepnote file structure](./streamlit/assets/Deepnote_file_struct.png "Deepnote file structure")


For referencing files, this line of code was key:

```
Path(__file__).parents[1]
```

It lives online here: https://deepnote-to-stlit-comm-cloud.streamlitapp.com/
## Getting Started

### Dependencies

* Deepnote project
* Streamlit account
* Github account

### Installing

* Just clone this or copy/paste :)
* This text can be pasted into a new Deepnote file with **.ipynb** extension:
```{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "import os"
   ]
  }
 ],
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {}
}
```
Once created, click to a different file, then back to this one, and it should(as of 10/18/2022) be recognized as a jupyter notebook.
More information from Deepnote is here: https://deepnote.com/docs/notebooks

### Executing program

* https://deepnote-to-stlit-comm-cloud.streamlitapp.com/
* in your directory analogous to and located at the same level as ```/For_github``` run the following commands from the terminal:
```
git init
git add *
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_ACCOUNT/YOUR_GITHUB_PROJECT_NAME.git
```

### Running a single requirement.txt file

You can make a decision to use a single `requirements.txt` file, or two, depending on how resource intensive your your code is. Streamlit's cloud
isn't as powerful as Deepnote's, so you need to be careful how much processing vs displaying results you want to do. For a light project like this one,
sharing a `requirements.txt` file can be more convenient. You can point to the one inside the `streamlit` directory with a modification to
Deepnote's `init.py` file, found under the Settings gear in the Environment section on the right. There are three references to the file in the script.

```
%%bash
# If your project has a 'requirements.txt' file, we'll install it here apart from blacklisted packages that interfere with Deepnote (see above).
if test -f /work/Streamlit_demo/For_github/streamlit/requirements.txt
  then
    sed -i '/jedi/d;/jupyter/d;' /work/Streamlit_demo/For_github/streamlit/requirements.txt
    
    #This line was added to get rid of the warning about pip
    pip install --upgrade pip
    
    pip install -r /work/Streamlit_demo/For_github/streamlit/requirements.txt
  else echo "There's no requirements.txt, so nothing to install. This is the case with most projects."
fi
```


## Authors

Oleg


## Acknowledgments

* [simple-readme](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
