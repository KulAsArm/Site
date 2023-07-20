# Site
Содержание

1. Вступление
2. Алфавитный перечень страниц и общее содержание проекта
	2.1. Строение приложения <holidays>
	2.2. Строение приложения <users>
	2.3. Строение проекта
3. Описание типовых элементов интерфейса
4. Описания отдельных страниц.
	4.1. abus.html
	4.2. booking.html
	4.3. dest.html
	4.4. index.html
	4.5. dest.html
5. Документация по установке, запуску приложения, администрированию.
6. Приложение 1
7. Приложение 2
8. Приложение 3
9. Приложение 4
10. Приложение 5
11. Приложение 6
1. Вступление

	Разработанное в ходе работы веб-приложение позволяет автоматизировать процесс поиска и брони путёвок для студентов в летние лагеря МГТУ, что позволяет:
1. снизить количество персонала студенческого совета, обслуживающих запросы со стороны студентов;
2. сделать процесс брони доступным круглосуточно;
3. упростить процесс взаимодействия студентов и персонала путём реализации всех основных функций, требуемых для реализации потребностей членов студсовета, внутри веб-приложения.
	Большое количество студентов могут воспользоваться сервисом, который сможет подерживать один человек, при этом на одном веб-приложении можно разместить как информацию общего характера, так и детали отдыха студентов в конкретном месте, что повышает информированность отдыхающих и может сделать их отдых интереснее и продуктивнее.


2. Алфавитный перечень страниц и общее содержание проекта

	Алфавитный перечень страниц представляет собой список страниц в формате *.html, доступных в проекте:
- abus.html,
- booking.html,
- dest.html,
- index.html,
- login.html,
- profile.html,
- reg.html,
- regr.html.
	Также, благодаря фреймворку Django, доступна такая страница, как 
admin.html.
	Проект содержит в себе 2 Django-приложения:
1) <holidays>,
2) <users>.
	Каждое приложение разработано с использованием фреймворка Django через использование команды: 
	python3.11 manage.py startapp <имя_приложения>
	
2.1. Строение приложения <holidays>
	Приложение <holidays> реализует логику работы со всем содержимым сайта, кроме регистрации, авторизации пользователей. 
	Строение приложения представлено в листинге 1, полученном с помощью команды <tree> выполненной в консоли.

├── admin.py 
├── apps.py 
├── __init__.py 
├── migrations 
│   ├── __init__.py 
├── models.py 
├── static 
│   └── holidays 
│       ├── css 
│       │   ├── booking_bg_long.png 
│       │   ├── main_bg.png 
│       │   └── styles.css 
│       └── img 
│           ├── blue_cogwheel.svg 
│           ├── booking_bg_long.png 
│           ├── booking_bg.png 
│           ├── cogs.png 
│           ├── djantugan.jpg 
│           ├── logo_prototype.svg 
│           ├── main_bg.png 
│           ├── pic_cogwheel.svg 
│           └── Yellowcogwheel.svg 
├── templates 
│   └── holidays 
│       ├── abus.html 
│       ├── booking.html 
│       ├── dest.html 
│       ├── index.html 
│       ├── login.html 
│       ├── profile.html 
│       └── reg.html 
├── tests.py 
├── urls.py 
└── views.py
Листинг 1. Строение приложения <holidays>.

	Фреймворк Django при создании приложения разворачивает требуемую инфраструктуру, такую, как в листинге 2.
├── admin.py 
├── apps.py 
├── __init__.py 
├── migrations 
│   └── __init__.py 
├── models.py 
├── tests.py 
└── views.py

Листинг 2. Строение инфраструктуры пустого приложения.

	Разработчику требуется лишь заполнить требуемые файлы кодом, подключить нужные файлы, такие как изображения или страницы *.html, чтобы потом успешно обрабатывать запросы.
	В приложении <holidays> инфраструтура была дополнена следующими вложенными в директорию приложения директориями:
1) <static>
	Поддиректория содержит в себе такие материалы, как *.css файл с настройками стилей, и изображения для размещения на страницах в браузере пользователя.
2) <templates>
	Поддиректория содержит в себе файлы *.html в которых содержится информация о структуре страниц.
	Код приложения был вставлен в следующие файлы:
1) <urls.py>
	Файл должен содержать в себе код указания фреймворку на URL-паттерны. При выборке перехода на стребуемый URL-адрес фреймворк выбирает требуемую строку из файла и переходит по содержащейся в нём функции в  файл <views.py>. Код представлен в приложении 1. 
2) <views.py>
	Файл содержит в себе код для реализации работы логики при требуемых запросах. Каждая функция получает объект запроса <request>. По завершению работы любой функции возвращается объект ответа <HttpResponse>. Каждая функция возвращает в качестве содержимого ответа страницу *.html формата из поддиректории приложения <templates>.
	<Holidays>, описание методов приложения(по порядку):
1) создание брони
2) обновление данных в БД в таблице направлений
3) расчёт процентном отношении занятых мест от общего количества
4) переход на главную страницу
5) второе и далее отвечает за букинги, код одинков, просто названия и даты разные.
6) обычные функции обычных страниц.
	Более подробно можно ознакомиться в приложении.



2.2. Строение приложения <users>
	Приложение <users> реализует логику работы по регистрации, авторизации пользователей.
	Т.о. приложение <users> является независимым от основного проекта приложением, которое можно встраивать в другие проекты использующие фреймворк Django. 
	Строение приложения представлено в листинге 3.
├── admin.py 
├── apps.py 
├── forms.py 
├── __init__.py 
├── migrations 
│   ├── __init__.py 
├── models.py 
├── templates 
│   └── users 
│       ├── login.html 
│       └── register.html 
├── tests.py 
└── views.py
	Листинг 3. Строение приложения <users>

	В ходе разработки приложения был добавлен код в следующие файлы:
1) <forms.py>;
2) <views.py>.
	Код каждого файла представлен в приложениях 3 и 4 соответственно.
	Приложение <users> представляет 3 функции и располагает 2-мя страницами *.html. Функции:
1) <sign_in> - функция для авторизации пользователя,
2) <sign_out> - функция для выхода пользователя с сайта,
3) <sign_up> - функция для регистрации нового пользователя.
	Для реализации использовались формы, определяемые разработчиком в файле <forms.py>:
1) <UserRegisterForm>
2) <UserLoginForm>
	В самом файле определяются именно классы форм, чьи конструкторы затем будут вызваны в нужных функциях файла <views.py>.
	Фреймворк предоставляет базовые формы как для регистрации, так и для авторизации. В коде эти формы были вызваны и была реализована работа с их содержимым.
	Графическое представление форм, получаемых от фреймворка, можно изменять с помощью написания специальных функций. В приложении была реализована функция по скруглению краёв полей ввода для форм авторизации и регистрации:
1) def __init__(self, *args, **kwargs)
	Для изменения внешнего вида полей регистрации.
2) для изменения полей авторизации в функцию вызова форм был передан параметр <widget> с подробными свдениями о требуемом закруглении.
	Подробно ознакомиться с кодом можно в приложении 3.
	Отметим, что модель пользователя была импортирована из инструментария фреймвора Django и расширена для соответствия модели студента из приложения <holidays> с чем связан большой размер кода. Таким образом осуществляется отображение один к одному. 
	В коде можно заметить применение декоратора <@transaction.atomic> который отвечает за передачу данных в БД при соблюдении связи двух выше упомянутых сущностей.


2.3. Строение проекта


3. Описание типовых элементов интефрейса

	Пользовательский интерфейс – это та среда, с помощью которой человек взаимодействует с программой или сайтом. Соответственно, комфорт работы с ним напрямую влияет на посещаемость сайта, рейтинги сайта среди студентов и, в конечном счете, реализацию путёвок.
	Типовыми элементами интерфейса для пользователя являются следующие элементы:
- кнопки,
- поля для ввода текста,
- текстовые поля вывода текста.
	Перечисленные элементы пользовательского интерфейса являются частью страницы, отображаемой в веб-браузере при запросе пользователя. 
	Действия пользователя:
1) щёлкнуть на кнопку — переход на другую страницу, или подтверждение ввода и отправки информации на сервер.
2) ввести текст — пользователь вводит в текстовое поле текст.
	Информация обрабатывается как http-запрос с помощью написанных функций для фреймворка Django. Фреймворк обрабатывает запрос и возвращает назад ответ в виде <HttpResponse>.
	Любая страница веб-приложения в браузере может быть условно разделена на несколько частей:
1) шапка страницы;
2) центральная колонка информации, занимает среднюю часть страницы;
3) боковые колонки для вспомогательной информации, имеющий более низкий статус востребованности;
4) подвал страницы — область страницы в самом её низу, содержащая информацию с наименьшей востребованностью.
	Все веб-страницы приложения <holidays> имеют одинковую шапку и подвал. 
	Шапка состоит из:
1) кнопки «Главная»
	Кнопка возвращает пользователя на страницу index.html, главную страницу проекта.
2) кнопки «О нас»
	Кнопка переводит пользователя на страницу abus.html, содержащую информацию о авторах сайта и прочем.
3) «Направления»
	Переводит пользователя на страницу dest.html, содержащую в виде таблицы все заголовки направлений.
4) «Личный кабинет»
	Переводит пользователя на страницу profile.html. Информация о статусе пользователя, его поездках.
	
4. Описания отдельных страниц

	Каждая страница в проекте имеет некоторую уникальную информацию, что является элементом структуризации информации с целью улучшения её обрабатываемости человеком.
4.1. abus.html
	Страница abus.html предоставляет пользователю информацию о веб-приложении:
1) кто автор приложения,
2) информацию о чём и какого рода предоставляет данный сайт,
3) общую информацию о содержимом сайта.
	За обработку запросов отвечает функция:
	def aboutus(request)
находящася в файле <views.py> основной директории приложения.


4.2. booking.html
	Страница booking.html предоставляет пользователю информацию о выбранном направлении поездки:
1) название направления;
2) детали размещения отдыхающих;
3) всё о питании отдыхающих;
4) как добраться до места отдыха;
5) поле <e-mail> для ввода электронной почты;
6) поле телефонного номера;
7) кнопка «Забронировать».
	Таким образом предоставляется информация о направлении и тут же инструмент для бронирования места.
	Кроме того, для более точного информирования пользователя введён прогресс-бар на страницу. Он отмечает процентное содержание оставшихся мест и окрашивается в соответствующий цвет.

4.3. dest.html
	Страница предоставляет информацию о всех доступных направлениях отдыха. Информация предоставляется в виде 2-ух столбчатой таблицы, содержащей заголовки доступных мест отдыха. Информация о направлении:
1) название направления;
2) картинка направления;
3) описание направления;
4) «Оставить заявку» - кнопка перевода пользователя на booking.html с соответствующей информацией о направлении.

4.4. index.html
	Страница предоставляет пользователю актуальную информацию о количестве направлений поездок.

4.5. profile.html
	Страница предоставляет пользователю инструменты по заполнению данных о себе для актуализации данных в базе данных отдыхающих. Доступные для заполнения поля:
1) ФИО;
2) e-mail;
3) факультет;
4) номер студенческого билета;
5) имя аккаунта;
6) льготы студента;
7) путёвки студента;
8) кнопку «Сохранить данные».

5. Документация по установке, запуску приложения, администрированию.

	Для запуска сайта при наличии только лишь приложений на некотором удалённом сервере с OS Ubuntu потребуется сделать следующие действия в директории проекта:
1) установить пакет <nginx>;
	sudo apt install nginx
2) создаём директорию для хранения файлов сайта;
	mkdir /var/mysite
3) создаём виртуальное окружения в данной директории;
	python3 -m venv mysite_venv
4) активируем виртуальное окружение;
	source mysite_venv/bin/activate
5) устанавливаем в него Django и gunicorn:
	pip install django 
	pip install gunicorn
6) создаём проект:
	python3.11 -m django-admin startproject <имя проекта>
7) Потребуется воспроизвести первичные миграции:
	python3.11 manage.py makemigrations
	python3.11 manage.py migrate
8) Создаём суперпользователя(он же администратор нашего сайта):
	python3.11 manage.py createsuperuser 
	и следуем инструкциям
9) После создания учётной записи суперпользоателя мы должны вложить в директорию проекта сайта директории с нашими приложениями <holidays> и <users>, после чего прописать в файле <settings.py> директории проекта в списке <INSTALLED_APPS> каждое установленное приложение:
	"users.apps.UsersConfig",
	"holidays.apps.HolidaysConfig",

	Далее настраиваем <gunicorn>:
1) в каталоге /etc /systemd /system создаём два файла:
	gunicorn.service
	gunicorn.socket
	Код содержимого файла представлен в приложениях 5 и 6 соответственно.
2) Проверим файлы на наличие ошибок:
	systemd-analyze verify gunicorn.service

	Далее настраиваем <nginx>:
1) В каталоге /etc /nginx /sites-available создаём файл c именем нашего сайта:\
	sudo vim <название_нашего_сайта>
	Содержимое файла представлено в приложении 7.

	Финальная часть:
1)Для проверки конфигурации <nginx>:
	sudo nginx -t
2) Если проверка прошла, то запускаем <gunicorn> и создаём <socket>:
	sudo systemctl enable gunicorn
	sudo systemctl start gunicorn
3) для проверки создания сокета:
	file /run/gunicorn.sock
4) если всё работает нормально, то:
	sudo service nginx start

	Получаем сертификат SSL для домена:
1) Выполним команду:
	sudo apt-get install certbot python-certbot-nginx
2) Первичная настройка:
	certbot: sudo certbot certonly --nginx
3) Автоматически поправим конфигурацию сервиса:
	sudo certbot install --nginx 
4) Перезапуск службы:
	sudo systemctl restart nginx

	Если в наличии имееся директория с проектом, то пункты 6-9 из первого раздела можно не выполнять, а сразу развернуть в целевой директории папку с проектом.
	
	Для поддержания работы сайта потребуется обновлять направления выезда, работать с пользователями и прочим.
	
	Для обновления направлений потребуется добавлять новые шаблоны *.html, чтобы серер их учёл потребуется выполнять:
	service gunicorn restart
	
	Если потребуется вручную добавить новых пользователей, удалить старых, то для этого потребуется воспользоваться формой суперпользователя, которая доступна по адресу /admin. Для доступа к функционалу потребуется ввести пароль и логин администратора.
	
	
Приложение 1
from django.urls import path
from . import views


urlpatterns = [path('', views.index, name='base'),
               path('booking/', views.booking, name='booking'),
               path('booking2/', views.booking2, name='booking2'),
               path('booking3/', views.booking3, name='booking3'),
               path('booking4/', views.booking4, name='booking4'),
               path('booking5/', views.booking5, name='booking5'),
               path('booking6/', views.booking6, name='booking6'),
               path('booking7/', views.booking7, name='booking7'),
               path('booking8/', views.booking8, name='booking8'),
               path('aboutus/', views.aboutus, name='aboutus'),
               path('dest/', views.dest, name='dest')]
Приложение 2

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from .models import Destinations
from users.models import Booking


def booking_create(request, dests):
    booking = Booking()
    booking.student_id = request.user.student.id
    booking.destination_id = dests.id
    booking.save()


def dest_update(date, name):
    dest = Destinations.objects.get(name=name, date=date[0])
    dest.occ_seats = dest.occ_seats + 1
    dest.save()
    return dest


def views_occ(date, dest_name):
    # функция считает процент занятых мест от общего количества
    dest = Destinations.objects.get(name=dest_name, date=date)
    occ = dest.occ_seats
    total = dest.tot_seats
    return int(100 * occ / total)


def index(request):
    template = loader.get_template("holidays/index.html")
    context = {'title': 'ГЛАВНАЯ СТРАНИЦА НАШЕГО САЙТА '}
    return HttpResponse(template.render(context, request))


def booking2(request):
    dest_name = 'СОЛ "Бауманец"'
    dest_date = ['2023-06-10', '2023-07-01', '2023-07-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking2.html")
            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)
            res3 = views_occ(date=dest_date[2], dest_name=dest_name)
            context = {'seat_num2': res2, 'seat_num3': res3, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)
        res3 = views_occ(date=dest_date[2], dest_name=dest_name)
        template = loader.get_template("holidays/booking2.html")
        context = {'seat_num2': res2, 'seat_num3': res3, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking3(request):
    dest_name = 'СОЛ "КИТ"'
    dest_date = ['2023-06-16', '2023-07-01']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking3.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        template = loader.get_template("holidays/booking3.html")
        context = {'seat_num2': res2, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking4(request):
    dest_name = 'Пансионат "Сердоликовая бухта"'
    dest_date = ['2023-06-10', '2023-07-01']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking4.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking4.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking5(request):
    dest_name = 'Пансионат "Смена"'
    dest_date = ['2023-06-20', '2023-07-10']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking5.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking5.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking6(request):
    dest_name = 'СОЛ "Алушта"'
    dest_date = ['2023-07-01', '2023-07-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking6.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking6.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking7(request):
    dest_name = 'База отдыха "Охта"'
    dest_date = ['2023-06-10', '2023-07-01', '2023-08-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking7.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)
            res3 = views_occ(date=dest_date[2], dest_name=dest_name)
            context = {'seat_num2': res2, 'seat_num3': res3, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking7.html")
        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)
        res3 = views_occ(date=dest_date[2], dest_name=dest_name)
        context = {'seat_num2': res2, 'seat_num3': res3, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking8(request):
    dest_name = 'Кумысная поляна'
    dest_date = ['2023-08-10', '2023-08-20']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking8.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking8.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def booking(request):
    dest_name = 'Альплагерь Джан-Туган'
    dest_date = ['2023-07-15', '2023-08-01']
    if request.method == 'POST':
        date = request.POST.getlist('date')
        if (date[0] in dest_date) and (len(date) == 1):
            dest = dest_update(date, name=dest_name)

            booking_create(request=request, dests=dest)

            template = loader.get_template("holidays/booking.html")

            res = views_occ(date=dest_date[0], dest_name=dest_name)
            res2 = views_occ(date=dest_date[1], dest_name=dest_name)

            context = {'seat_num2': res2, 'seat_num': res}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("holidays/booking.html")

        res = views_occ(date=dest_date[0], dest_name=dest_name)
        res2 = views_occ(date=dest_date[1], dest_name=dest_name)

        context = {'seat_num2': res2, 'seat_num': res}
        return HttpResponse(template.render(context, request))


def aboutus(request):
    template = loader.get_template("holidays/abus.html")
    context = {}
    return HttpResponse(template.render(context, request))


def dest(request):
    template = loader.get_template("holidays/dest.html")
    context = {}
    return HttpResponse(template.render(context, request))
Приложение 3
from django import forms
from django.contrib.auth.models import User
from .models import Student


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "field_item",
                "placeholder": 'Введите пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': "field_item",
                "placeholder": 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", 'email']

        widgets = {
            "username": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите имя пользоваетля'
            }),
            "first_name": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите имя'
            }),
            "last_name": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите фамилию'
            }),
            "email": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите email'
            }),
        }

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={ 'class': "field_item",   "placeholder": 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': "field_item",
                "placeholder": 'Пароль'}), label='Пароль')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['FIO', 'email', 'phone', 'group', 'names_of_priority', 'telegram']

        widgets = {
            "FIO": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Иванов Иван Иванович'
            }),
            "email": forms.EmailInput(attrs={
                'class': "field_item",
                "placeholder": 'email@mail.ru'
            }),
            "phone": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": '+79953422112'
            }),
            "group": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'РК9-63Б'
            }),
            "names_of_priority": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите льготы'
            }),
            "telegram": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите telegram-аккаунт'
            }),

        }
Приложение 4
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.template import loader
from django.http import HttpResponse
from .forms import UserRegisterForm, LoginForm, UserProfileForm, User
from django.db import transaction
from .models import Booking, Destinations


def user_dest(request):
    st_id = request.user.student.id
    books = Booking.objects.filter(student_id=st_id)
    dests_list = []
    for book in books:
        dests_list.append(book.destination_id)
    print(dests_list)
    info = []
    for dest_id in dests_list:
        dest = Destinations.objects.get(id=dest_id)
        info.append(f'{dest.name}: {dest.date}')
    return info

def registration(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    template = loader.get_template('users/registration.html')
    context = {'user_form': user_form}
    return HttpResponse(template.render(context, request))


@transaction.atomic
def user_profile(request):
    if request.method == 'POST':
        student = UserProfileForm(request.POST, instance=request.user.student)
        if student.is_valid():
            print(request.path)
            idx = request.user.id
            email = request.user.email
            print(email)
            cd = student.cleaned_data
            cd['email'] = email
            user_change_profile = User.objects.get(id=idx)
            user_change_profile.student.FIO = cd['FIO']
            user_change_profile.student.email = cd['email']
            user_change_profile.student.group = cd['group']
            user_change_profile.student.phone = cd['phone']
            user_change_profile.student.names_of_priority = cd['names_of_priority']
            user_change_profile.student.telegram = cd['telegram']
            user_change_profile.save()
            return redirect('complited_profile')
        else:
            error = "Формат заполнения полей неверный"
            template = loader.get_template("users/profile.html")
            context = {'student': student, 'error': error}
            return HttpResponse(template.render(context, request))
    else:
        student = UserProfileForm()
    template = loader.get_template("users/profile.html")
    context = {'student': student}
    return HttpResponse(template.render(context, request))


@transaction.atomic
def user_complited_profile(request):
    temp_user = request.user.student
    dests = user_dest(request)
    cd = temp_user
    context = {'cd': cd, 'dests': dests}
    template = loader.get_template("users/complited_profile.html")
    return HttpResponse(template.render(context, request))


def user_login(request):
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    log = loader.get_template('holidays/index.html')
                    return HttpResponse(log.render({}, request))
                else:
                    return HttpResponse('Disabled account')
            else:
                error = 'Введен неправильный логин или пароль'
                err = loader.get_template('users/login.html')
                context = {'user': user, "err": error}
                return HttpResponse(err.render(context, request))
    else:
        log_form = LoginForm()
    template = loader.get_template('users/login.html')
    context = {'log_form': log_form}
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    template = loader.get_template('users/logout.html')
    context = {}
    return HttpResponse(template.render(context, request))


def user_delete(request):
    if request.method == 'POST':
        id = request.user.id
        user = User.objects.get(id=id)
        user.delete()
        user_form = UserRegisterForm()
        template = loader.get_template('users/registration.html')
        context = {'user_form': user_form}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("users/delete.html")
        context = {}
        return HttpResponse(template.render(context, request))
Приложение 5
[Unit] 
Description=gunicorn daemon 
Requires=gunicorn.socket 
After=network.target

[Service] 
User=root 
WorkingDirectory=/var/www/geekhero #путь до каталога с файлом manage.py ExecStart=/var/www/geekhero/geekhero_env/bin/gunicorn --workers 5 —bind unix:/run/gunicorn.sock ghproj.wsgi:application #путь до файла gunicorn в виртуальном окружении 

[Install] 
WantedBy=multi-user.target
Приложение 6
[Unit] 
Description=gunicorn socket 
[Socket] 
ListenStream=/run/gunicorn.sock 
[Install] 
WantedBy=sockets.target
Приложение 7
server {
	listen 80;
	server_name <укажите_имя_сервера>
	
	location = /favicon.ico{access_log off, log_not_found off;}
	location /static/ {
		root /var/www/<укажите_имя_сайта>	# здесь нужно прописать путь до каталога <static>
	}
	location /media/ {
		root /var/www/<укажите_имя_сайта>	# путь до каталога <media>
	}
	location / {
		include proxy_params;
		proxy_pass http://unix:/run/gunicorn.sock;
	}
} 
