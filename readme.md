# Социальная сеть на Python Django 
____
## INSTALLING 

#### Инструменты разработки

<ul>
    <li>Python +3.7</li>
    <li>Версия Django не ниже 3.x</li>
    <li>Postgresql</li>
</ul>


#### Установка:

<ol>
    <li>Клонировать репозиторий<pre><code>git clone https://github.com/Untouchable17/social-web.git</code></pre><br></li>
    <li>Создать виртуальное окружение и активируйте его<pre><code>python -m venv env</code></pre><br></li>
    <li>Установите все зависимости<pre><code>pip install -r requirements.txt</code></pre><br></li>
    <li>Подготовьте модели<pre><code>python manage.py makemigrations</code></pre><br>
    <li>Запустите миграции<pre><code>python manage.py migrate</code></pre><br>
    <li>Создайте суперпользователя<pre><code>python manage.py createsuperuser</code></pre><br>
    <li>Запустите сайт<pre><code>python manage.py runserver</code></pre><br></li>
</ol>

