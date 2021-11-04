# Python venv in win10 wsl2
Versions

- Ubuntu 20.04.2 LTS
- Python 3.8.5
***
commands for venv
``` bash
# create venv
python3 -m venv .venv

# activate venv
source .venv/bin/activate 

# shows python version
which python

# deactivate venv
deactive

# installs dependen
pip install -r requirements.txt
```

requirements.txt is generated with

```bash
pip freeze > requirements.txt
```
***

installed libaryies
  beautifulsoup4
  lxml

site that is used as an example
https://yle.fi/uutiset/3-12025156




