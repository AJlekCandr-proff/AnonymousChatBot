from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


def interests_keyboard() -> InlineKeyboardMarkup:
    inline_builder = InlineKeyboardBuilder()

    inline_builder.row(InlineKeyboardButton(text='', callback_data=''))
