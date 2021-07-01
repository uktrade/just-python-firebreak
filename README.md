# just-python-firebreak

Install Latest version of Python (currently 3.9.6)


## setup virtual environment

```bash
<local python3 install> -m venv venv
source venv/bin/activate
```

Now to make use of the modern type hinting we have to install mypy and then setup up your dev environment to mypy
```bash
python -m pip install mypy
```

Personally when developing code I use black, flake8 and jedi (on windows you may have to smomething other than jedi)
```bash
python -m pip install black flake8 jedi
```


## Using setup tools to make a python executable 

The main documentation that I have used for this is [python setup tools](https://setuptools.readthedocs.io/en/latest/)

The specific part of the docs I have used for making this entry point is [entry points](https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html#entry-points)

This branch of commits is to show the basic common ways of making a python executable. The use of setup tools entry points and the __main__.py file also the basic lines

```python
if __name__ == "__main__":
    run_start_point()
```

## Building a release, Using wheel

the command to build the Python only release
```bash
python setup.py bdist_wheel
```

Here is further documentation for releasing Python code. [python-wheel](https://realpython.com/python-wheels/ "link to real python")


## Running python inbuilt unittests

Python comes with a full set of unittest tools [python-unittest](https://docs.python.org/3/library/unittest.html "link to unittest Python docs.") 
Remember our Python source code is a series of Python modules, so each of these directories have a `__init__.py` file. The unit tests are just a series of scripts, not Python modules, so do __NOT__ have `__init__.py` files in those directory.

The inbuilt Python test suite can be run using
```bash
python -m unittest discover tests
```
