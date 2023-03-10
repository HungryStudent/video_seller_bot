choose_lang = "Здравствуйте, выберите язык\nHello, choose a language"

hello = {"ru": "текст",
         "en": "text"}
hello_admin = "Вы вошли как администратор"
cancel_input = {"ru": "Ввод остановлен",
                "en": "Input stopped"}

feedbacks = {"ru": "Отзывы: @reviews_renderforest",
             "en": "Feedbacks: @reviews_renderforest"}

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

new_gift_order = {"ru": """Новый заказ от @{username}
Ссылка {url}
Слоган: {text}
Примечание: интро за отзыв""",
                  "en": """New order from @{username}
Link {url}
Slogan: {text}
Note: intro for the review"""}

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

admin_settings = "Вы перешли в настройки"

error_logo = {"ru": "Пришлите логотип как фото, а не как документ (поставьте галочку 'Сжать изображение')",
              "en": "Send the logo as a photo, not as a document (check the box 'Compress image')"}


class Settings:
    enter_price = "Введите новую цену"
    enter_channel_id = "Введите id канала"
    enter_channel_url = "Введите ссылку на канал"
    finish = "Данные обновлены"


class TrialVideo:
    enter_url = {
        "ru": "Перейдите по ссылке: https://www.renderforest.com/ru/intro-videos (выберите интро и пришлите ссылку на него или название)",
        "en": "Follow the link: https://www.renderforest.com/ru/intro-videos (select an intro and send a link to it or a title)"}
    enter_logo = {"ru": "Пришлите фото логотипа в высоком качестве в PNG на прозрачном фоне",
                  "en": "Send a photo of the logo in high quality in PNG on a transparent background"}
    enter_text = {"ru": "Введите слоган или сайт, либо пропустите этот шаг",
                  "en": "Enter a slogan or website, or skip this step"}
    finish = {"ru": "Ожидайте, ваша заявка отправлена",
              "en": "Wait, your application has been sent"}


class Video:
    enter_url = {
        "ru": "Перейдите по ссылке: https://www.renderforest.com/ru/intro-videos (выберите интро и пришлите ссылку на него или название)",
        "en": "Follow the link: https://www.renderforest.com/ru/intro-videos (select an intro and send a link to it or a title)"}
    enter_logo = {"ru": "Пришлите фото логотипа в высоком качестве в PNG на прозрачном фоне",
                  "en": "Send a photo of the logo in high quality in PNG on a transparent background"}
    enter_text = {"ru": "Введите слоган или сайт, либо пропустите этот шаг",
                  "en": "Enter a slogan or website, or skip this step"}
    gift = {"ru": "За интро платить не нужно, так как вы оставили отзыв.\nОжидайте, ваша заявка отправлена",
            "en": "There is no need to pay for the intro, since you left a review.\nWait, your application has been sent"}
    finish = {"ru": "Оплата проведена успешно, ожидайте выполнение заказа",
              "en": "The payment was made successfully, wait for the order to be completed"}
    pay = {"ru": "Стоимость интро: {price} рублей",
           "en": "Intro cost: {price} dollars"}


class StayFeedback:
    enter_feedback = {"ru": "Напишите отзыв", "en": "Write a review"}
    finish = {"ru": "Отзыв отправлен, вам начислен один бесплатный заказ интро",
              "en": "The review has been sent, you are credited with one free order intro"}


class SendVideo:
    enter_video = "Пришлите видео"
    finish = "Видео отправлено заказчику"
