from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton


def start_menu() -> ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.row(KeyboardButton(text='🚀 Поиск случайного собеседника'))
    keyboard_builder.row(KeyboardButton(text='🔎 Поиск по полу'), KeyboardButton(text='📖 Интересы поиска'))

    return keyboard_builder.as_markup(resize_keyboard=True)


def chat_menu() -> ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder()

    return keyboard_builder.row(KeyboardButton(text='Стоп ❌')).as_markup(resize_keyboard=True)
