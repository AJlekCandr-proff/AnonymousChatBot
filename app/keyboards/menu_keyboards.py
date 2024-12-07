from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton


def start_menu() -> ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.row(KeyboardButton(text='🚀 Поиск случайного собеседника'))
    keyboard_builder.row(KeyboardButton(text='Премиум поиск'), KeyboardButton(text='📖 Интересы поиска'))

    return keyboard_builder.as_markup(resize_keyboard=True)
