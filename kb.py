from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

volume = [
    [
        InlineKeyboardButton(
            text="Прибавить громкость",
            callback_data="volume_plus",
        ),
    ],
    [
        InlineKeyboardButton(
            text="Убавить громкость",
            callback_data="volume_minus",
        )
    ],
    [
        InlineKeyboardButton(
            text="Выйти",
            callback_data="volume_exit",
        )
    ]
]
start = [
    [
        InlineKeyboardButton(
            text="Звук",
            callback_data="volume",
        ),
    ],
    [
        InlineKeyboardButton(
            text="Выключить ПК",
            callback_data="off",
        )
    ],
    [
        InlineKeyboardButton(
            text="Перезагрузить ПК",
            callback_data="reboot",
        )
    ],
    [
        InlineKeyboardButton(
            text="Отмена",
            callback_data="cancel",
        )
    ]
]
start = InlineKeyboardMarkup(inline_keyboard=start)
volume = InlineKeyboardMarkup(inline_keyboard=volume)
