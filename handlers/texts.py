choose_lang = "Здравствуйте, выберите язык\nHello, choose a language"

hello = {"ru": "текст",
         "en": "text"}
hello_admin = {"ru": "Вы вошли как администратор",
               "en": "You are logged in as an administrator"}
cancel_input = {"ru": "Ввод остановлен",
                "en": "Input stopped"}

support = {"ru": "По всем вопросам: @skilord1988",
           "en": "For all questions: @skilord1988"}

trial_error = {"ru": "Вы использовали свой пробный период",
               "en": "Have you used your trial period"}

new_trial_order = {"ru": """Новый заказ от @{username}
Ссылка {url}
Слоган: {text}
Примечание: пробный вариант""",
                   "en": """New order from @{username}
Link {url}
Slogan: {text}
Note: trial version"""}

new_order = {"ru": """Новый заказ от @{username}
Ссылка: {url}
Слоган: {text}""",
             "en": """New order from @{username}
Link {url}
Slogan: {text}"""}

order_for_user = {"ru": "Результат",
                  "en": "Result"}

sub_error = {"ru": "Для того, чтобы пользоваться ботом, подпишитесь на канал и повторите попытку",
             "en": "In order to use the bot, subscribe to the channel and try again"}

admin_settings = {"ru": "Вы перешли в настройки",
                  "en": "You have gone to settings"}


class Settings:
    enter_price = {"ru": "Введите новую цену",
                   "en": "Enter a new price"}
    enter_channel_id = {"ru": "Введите id канала",
                        "en": "Enter the channel id"}
    enter_channel_url = {"ru": "Введите ссылку на канал",
                         "en": "Enter the link to the channel"}
    finish = {"ru": "Данные обновлены",
              "en": "Data updated"}


class TrialVideo:
    enter_url = {
        "ru": "Перейдите по ссылке: https://www.renderforest.com/ru/intro-videos (выберите интро и пришлите ссылку на него или название)",
        "en": "Follow the link: https://www.renderforest.com/ru/intro-videos (select an intro and send a link to it or a title)"}
    enter_logo = {"ru": "Пришлите фото логотипа в высоком качестве в PNG на прозрачном фоне",
                  "en": "Send a photo of the logo in high quality in PNG on a transparent background"}
    enter_text = {"ru": "Введите слоган или сайт, либо пропустите этот шаг",
                  "en": "Enter a slogan or website, or skip this step"}
    finish = {"ru": "текст",
              "en": "Wait, your application has been sent"}


class Video:
    enter_url = {
        "ru": "Перейдите по ссылке: https://www.renderforest.com/ru/intro-videos (выберите интро и пришлите ссылку на него или название)",
        "en": "Follow the link: https://www.renderforest.com/ru/intro-videos (select an intro and send a link to it or a title)"}
    enter_logo = {"ru": "Пришлите фото логотипа в высоком качестве в PNG на прозрачном фоне",
                  "en": "Send a photo of the logo in high quality in PNG on a transparent background"}
    enter_text = {"ru": "Введите слоган или сайт, либо пропустите этот шаг",
                  "en": "Enter a slogan or website, or skip this step"}
    finish = {"ru": "текст",
              "en": "Wait, your application has been sent"}
    pay = {"ru": "Стоимость интро: {price} рублей",
           "en": "Intro cost: {price} dollars"}


class SendVideo:
    enter_video = {"ru": "Пришлите видео",
                   "en": "Send a video"}
    finish = {"ru": "Видео отправлено заказчику",
              "en": "Video sent to the customer"}
