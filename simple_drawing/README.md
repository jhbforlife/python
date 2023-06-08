# simple_drawing

this is just me playing around with the `cmu_graphics` package used in [CMU's CS Academy CSP module](https://academy.cs.cmu.edu/course-info). this will be a part of the AP Computer Science Principles classroom where I'll be a [Microsoft TEALS volunteer TA](https://www.microsoft.com/en-us/teals) during the 2023-2024 school year

## dependencies
- [pycairo 1.23.0](https://pycairo.readthedocs.io/en/latest/getting_started.html)
    - pkg-config and cairo (follow link for installation instructions)
- [cmu-graphics 1.1.23](https://pypi.org/project/cmu-graphics/1.1.23/)

## local environment

### setup

#### create virtual environment
```
python -m venv venv
```

#### activate virtual environment
```
source venv/bin/activate
```

#### install dependencies
```
pip install -r requirements.txt
```

### teardown

#### deactivate virtual environment
```
deactivate
```

#### delete virtual environment
```
rm -rf venv
```