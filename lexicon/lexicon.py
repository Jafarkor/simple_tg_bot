LEXICON_RU: dict[str, str] = {
    '/start': 'Привет, {}!\n\nЯ бот для игры в Камень - Ножницы - Бумага!\n\n'
    'Если хотите - можем поиграть :)\n'
    'Или же узнать правила игры, отправив команду /help',

    '/help': 'Основные правила игры «камень, ножницы, бумага»:\n\n'
    'В классической игре участвуют два игрока.\n\n'
    'Каждый игрок одновременно показывает одну из трёх фигур: камень, ножницы или бумага.\n\n'
    '«Камень» побеждает «ножницы» («камень ломает ножницы»).\n'
    '«Ножницы» побеждают «бумагу» («ножницы режут бумагу»).\n'
    '«Бумага» побеждает «камень» («бумага обертывает камень»).\n\n'
    'Если оба игрока показывают одинаковую фигуру, это ничья.',

    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',

    'start_playing': 'Ну, {}, Я вижу ты смелый парень, раз решил потягаться со мной. Хорошо, делай свой выбор!',
    'stop_playing': 'Хорошо, когда захочешь сыграть, открой клавиатуру и нажми Давай!',

    'draw': 'Ты выбрал {}, Я же выбрал {}\nУ нас ничья! Вот это да, а ты хорош)\nНо учти, в следующий раз тебе повезет меньше',
    'loss': 'Ты выбрал {}, Я же выбрал {}\nТы проиграл, как я и ожидал. Как же я хорош :)',
    'victory': 'Ты выбрал {}, Я же выбрал {}\nТы выиграл... НО КАК? Ладно, давай еще раз, я тебе покажу'

}