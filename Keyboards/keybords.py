from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def hello_keyboard():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
        .add(InlineKeyboardButton("Поиск по геолокации", callback_data="location", request_location=True)) \
        .add(InlineKeyboardButton("Поиск по имени", callback_data="name", request_location=True))
    return keyboard


def artist_name_keyboard(arists: list):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for artist in arists:
        keyboard.add(InlineKeyboardButton(artist["Name"], callback_data=artist["Artist_code"]))
    return keyboard


def buy_ticket_keyboard(concert: dict):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Купить билет", url=f"https://www.songkick.com/{concert['Link']}"))
    return keyboard


def pagination_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("<", callback_data="forward_page"),
        KeyboardButton("Назад", callback_data="cancel"),
        KeyboardButton(">", callback_data="next_page"))
    return keyboard


def location_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("Отправить геолокацию", request_location=True))
    return keyboard
