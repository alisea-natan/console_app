
### _USING poetry_
1) `cd console_app`  // go to project directory
1) `brew install poetry` // for macOS (you can find installation instructions here https://python-poetry.org/docs/)
1) `poetry config virtualenvs.in-project true` // .venv will be in the project dir
1) `poetry install` // install all dependencies
1) `poetry shell` // activate venv
1) `poetry run say-hello` // run script
1) `poetry run say-hello -n Name` // run script with options using click module
   
### _USING setuptools_
1) unzip package dist/console_app-0.1.0.tar.gz // download and unzip archive
1) `cd console_app-0.1.0` // go to unzipped directory
1) `virtualenv venv` // initialize virtual environment
1) `source venv/bin/activate` // activate virtual environment
1) `python3 setup.py install` // install all packages and dependencies
1) `greeting` // run script using entry point
1) `greeting -n Name` // run script using entry point and click

To create archive you need a command `python3 setup.py sdist`