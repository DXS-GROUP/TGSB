HELLO_FOR_ADMIN = """
Привет админ.
Для тебя доступны следующие команды:

/adduser %user_id% - Добавить пользователя в белый список
/removeuser %user_id% - Удалить пользователя из белого списка
/addadmin %admin_id% - Добавить админа
/removeadmin %admin_id% - Удалить админа
/whitelist - Вывести содержимое whitelist
"""

HELLO_FOR_CREATOR = """
Привет разраб.
Для тебя доступны следующие команды:

/addadmin %admin_id% - Добавить админа
/removeadmin %admin_id% - Удалить админа
/adduser %user_id% - Добавить пользователя в белый список
/removeuser %user_id% - Удалить пользователя из белого списка
/whitelist - Вывести содержимое whitelist
/block %user_id% - Заблокировать пользователя
/unblock %user_id% - Разблокировать пользователя
"""

HELLO_FOR_USER = """
Привет, этот бот представляет собой сервис для смс спама и спама звонками.
Выбери нужный пункт
"""

MESSAGE_FOR_NOT_IN_WHITELIST = """
Вы не в белом списке.
Если вы скачали этот сервис с github, то вы можете добавить id своего аккаунта в data.json
Если вы запустили бота: https://t.me/project3098_bot, то для добавления в белый список обратитесь к @Night3098
"""

SERVER_IS_NOT_UP = """
Сервер отключен главным администратором. Пожалуйста, подождите включения.
"""

NO_ACCESS = """
У вас нет доступа к этой функции
"""

FILE_NOT_FOUND = """
Ошибка. Файл не найден.
"""

DONE = """
Команда выполнена успешно
"""

RM_LOG = """
Логи успешно удалены
"""

GET_PHONE = """
Введи через пробел:
    Номер телефона в формате 8XXXXXXXXXX
    Количество кругов
"""

BLACKLIST = """
Вы находитесь в чёрном списке
Сори (
"""
