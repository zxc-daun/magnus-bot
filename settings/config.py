import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = '5820296439:AAElx6FktK4KaVXd8Izr3C1t8EiAxdKx6qQ'
# название БД
NAME_DB = 'products.db'
# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'Shokhzod https://t.me/zxcIown'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Select products'),
    'INFO': emojize(':speech_balloon: About us'),
    'SETTINGS': emojize('⚙️ Manuals'),
    'DEVICES': emojize('🎧 Devices'),
    'PC': emojize('💻 PC components'),
    'PHONES': emojize('📱 Smartphones'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ORDER'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Confirm order',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'DEVICES': 1,
    'PC': 2,
    'PHONES': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
