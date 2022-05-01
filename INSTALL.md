# Installation and local setup

---

## Clone the repository

```sh
git clone https://github.com/JorgeTerence/codespark
```

## Install and setup Database\*

- Install MySQL or MariaDB on your system

```sh
# Arch Linux
sudo pacman -S mariadb
```

- Create a database called 'Codespark' + create Django user

```sql
CREATE USER 'django'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON *.* TO 'django'@'localhost' WITH GRANT OPTION;
```

- Set mysql credentials and django secret key as environment variables

```sh
# .bashrc or .zshrc
export DJANGO_MYSQL_USER='django'
export DJANGO_MYSQL_PASSWORD='strong_password'
export CODESPARK_SECRET_KEY='very_long_hash'
```

```sh
# config.fish
set -gx DJANGO_MYSQL_USER 'django'
set -gx DJANGO_MYSQL_PASSWORD 'strong_password'
set -gx CODESPARK_SECRET_KEY 'very_long_hash'
```

**\*Note:** you can go into `settings.py` and configure the database as you please. Consider checking out the official documentation: https://docs.djangoproject.com/en/4.0/ref/databases/

## Install dependencies

```sh
pip install -r requirements.txt
npm install
```

## Apply database models

```sh
./manage.py makemigrations
./manage.py migrate
```

## Run the server 🚀

```sh
npm run watch
./manage.py runserver
```
