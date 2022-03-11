# Installation and local setup

---

## Clone the repository

```bash
git clone https://github.com/JorgeTerence/codespark
```

## Install and setup Database\*

- Install MySQL on your system
- Create a database called 'Codespark'
- Create a user for the server to interact with the database
- Update `settings.py` or setup environment variables

**\*Note:** you can go into `settings.py` and configure the database as you please. Consider checking out the official documentation: https://docs.djangoproject.com/en/4.0/ref/databases/

## Install dependencies

```bash
pip install -r requirements.txt
```

## Apply database model configurations

```bash
./manage.py makemigrations
./manage.py migrate
```

## Run the server 🚀

```bash
./manage.py runserver
```
