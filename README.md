

### Создаём виртуальное окружение:
    py -m venv venv
- - - 
### Активируем виртуальное окружение:
    venv\Scripts\Activate.ps1
- - - 
### Устанавливаем все библиотеки 
    pip install -r .\requirements.txt
- - - 
### Cоздания основного проекта:
    py -m django startproject news_portal
- - - 
### Переходим в директорию проекта:
    cd news_portal

# Здесь файл manage.py, который является точкой входа для управления проектом.

- - - 
### Создание нового приложение core.
    py manage.py startapp core


## Базовая настройка Django flatpages
- - -
### В файле news_portal/news_portal/settings.py :
- - -
    SITE_ID = 1 # для корректной работы 'django.contrib.sites'
- - -
    В список INSTALLED_APPS добавляем строки :

        'django.contrib.sites', # для site в файле news_portal/news_portal/urls.py
        'django.contrib.flatpages', # для встроенного приложения flatpages применения стилей
- - - 
    В список MIDDLEWARE добавляем строку :
        
        MIDDLEWARE — это нечто вроде декораторов, которые применяются к абсолютно любой ссылке в веб-приложении и так же могут менять её поведение.
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', # для корректной работы встроенного приложения flatpages
- - - 
    В список TEMPLATES добавляем в 'DIRS'
        
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Путь до шаблонов
- - - 
    В конец файла добавить:
        
        STATICFILES_DIRS = [ BASE_DIR / 'static']
        Это настройка в Django, которая говорит:
        Ищи статические файлы (например, CSS, JavaScript, картинки)
        в папке static, которая находится внутри вашего проекта.
        BASE_DIR — это папка, где находится ваш проект.
        BASE_DIR / 'static' — это путь к папке static внутри вашего проекта.
- - -
### Команда для создания миграций в Django,
    py manage.py makemigrations
---
### Применение миграции
    py .\manage.py migrate
- - -
### Создание администратора
    py manage.py createsuperuser
    (admin admin)
---
### Запустить сервер
    py .\manage.py runserver
---
### Атрибуты сущностей:
---
    | Сущность  |  Атрибуты
---
    | Пользователи (User) | Это сужность описывает пользователя исходя из его роли Автора и просто Пользователея
                          |  - Ник  - - - - - - - - - - - - - username
                          |  - Пароль - - - - - - - - - - - - password 
                          |  - Почта  - - - - - - - - - - - - emaail
                          |  - Имя  - - - - - - - - - - - - - first_name
                          |  - Фамилия  - - - - - - - - - - - last_name
                          |  - Активен  - - - - - - - - - - - is_active
                          |  - Является сотрудником - - - - - is_staff
                          |  - Являеться суперпользователем - is_superuser
                          |  - Дата присоединение - - - - - - date_joined
                          |  - Роль - - - - - - - - - - - - - role
                          |  - Биография  - - - - - - - - - - bio
                          |  - Аватар - - - - - - - - - - - - avatar
                          |  - Телефон  - - - - - - - - - - - phone
---
    | Автор (AuthorProfile) | Эта сущность описывает профиль Автора
                            | - Пользователь (связь) - - - - user (OneToOneField)
                            | - Специализация  - - - - - - - specialization
                            | - Веб-сайт - - - - - - - - - - website
                            | - Подтвержденный автор - - - - is_verified
                            | - Опыт работы (лет)  - - - - - experience_years
                            | - Twitter  - - - - - - - - - - twitter_url
                            | - GitHub - - - - - - - - - - - github_url
                            | - Рейтинг  - - - - - - - - - - rating (добавить)
                            | - ФИО  - - - - - - - - - - - - full_name (добавить)
---
    | Профиль пользователя (UserProfile) | Эта сущность описывает профиль обычного Пользователя
                                         | - Пользователь (связь) - - - - user (OneToOneField)
                                         | - Предпочтения - - - - - - - - preferences
                                         | - Тип подписки - - - - - - - - subscription_type
                                         | - Email уведомления  - - - - - email_notifications
---
    | Пост      |  - Заголовок
                |  - Текст
                |  - Дата создание
                |  - Кто автор
                |  - Рейтинг
--- 
    | Новость   |  - Заголовок
                |  - Текст
                |  - Дата создание
                |  - Кто автор
                |  - Рейтинг
---






#### version :
    0.0.1 - Создал Gjango проект
    0.0.2 - Настроил news_portal - главное прилодение
    0.0.3 - Cоздал приложение users и частично прописал атрибуты сущностей в README.md













