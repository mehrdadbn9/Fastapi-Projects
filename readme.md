## How to create a virtual environment using pipenv
Open the command prompt and point to the project directory

Upgrade pip with the following command
```
py -m pip install --upgrade pip
```
Install pipenv with the following command

```
pip install pipenv
```

If `pipenv` is already installed, skip this step.

Create the virtual environment with the following command

```
pipenv install
```

Activate the virtual environment

```
pipenv shell
```

you can execute any of the following commands to check the installed packages or dependencies and graph

```
pip list
    OR
pip freeze
    OR
pipenv graph
```
### TO DO:
- [ ] Authentication
- [ ] Working with files(upload & download)
- [ ] Middleware 
- [ ] Web sockets 