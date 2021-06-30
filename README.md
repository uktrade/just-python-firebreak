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
