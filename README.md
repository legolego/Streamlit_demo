# Example connecting to Streamlit cloud from Deepnote through Github


## Description

This will use a single, shared requirements.txt file. It will be shared between Deepnote, through the init file, and Streamlit, which requires it to load libraries it needs.
One problem this was made to show was how to reference a file in both Deepnote ans Streamlit, this line of code was key

```
Path(__file__).parents[1]
```

It lives online here: https://legolego-streamlit-demo-streamlitdemo-un56xj.streamlitapp.com/
## Getting Started

### Dependencies

* Deepnote project
* Streamlit account
* Github account

### Installing

* Just clone this or copy/paste :)

### Executing program

* How to run the program
* Step-by-step bullets
* https://legolego-streamlit-demo-streamlitdemo-un56xj.streamlitapp.com/
```
git init
git add *
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/legolego/Streamlit_demo.git
```

### Deepnote file structure

![Deepnote file structure](./streamlit/assets/Deepnote_file_structure.png "Deepnote file structure")

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Oleg


## Acknowledgments

Inspiration, code snippets, etc.
* [simple-readme](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
