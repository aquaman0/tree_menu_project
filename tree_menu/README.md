# DJANGO-APP для отрисовки древовидного меню

#### Установка:
1. Клонируем репозиторий GIT:
   #### `git clone git@github.com:aquaman0/tree_menu_project.git`
2. Переходим в папку проекта, устанавливаем и активируем виртуальное окружение:
   #### `cd /YOUR_DIRECTORY/tree_menu_project`
   #### `pip3 install virtualenv`
   #### `virtualenv menu_env`
   #### `cd menu_env/Scripts`
   #### `activate.bat`
3. Выполняем установку и миграции:
   #### `pip install -r requirements.txt`
   #### `python manage.py makemigrations`
   #### `python manage.py migrate`
4. При необходимости создаем пользователя для входа в админ-панель:
   #### `python manage.py createsuperuser`
5. Запускаем сервер:
   #### `python manage.py runserver`
6. Переходим в админ панель:
   #### http://127.0.0.1:8000/admin/
Здесь добавляем своё меню и его элементы.
7. Переходим на домашнюю страницу для проверки корректности работы:
   #### http://127.0.0.1:8000/menu/