hello = "Здравствуйте, здесь вы можете заказать видео "
hello_admin = "Вы вошли как администратор"
cancel_input = "Ввод остановлен"

support = "По всем вопросам: @skilord1988"

trial_error = "Вы использовали свой пробный период"

new_trial_order = """Новый заказ от @{username}
Ссылка {url}
Слоган: {text}
Примечание: пробный вариант"""

new_order = """Новый заказ от @{username}
Ссылка: {url}
Слоган: {text}"""

order_for_user = "Результат"

sub_error = "Для того, чтобы пользоваться ботом, подпишитесь на канал и повторите попытку"

admin_settings = "Вы перешли в настройки"


class Settings:
    enter_price = "Введите новую цену"
    enter_channel_id = "Введите id канала"
    enter_channel_url = "Введите ссылку на канал"
    finish = "Данные обновлены"


class TrialVideo:
    enter_url = "Перейдите по ссылке https://www.renderforest.com/ru/intro-videos, выберите интро и пришлите ссылку на него"
    enter_logo = "Пришлите фото логотипа в высоком качестве"
    enter_text = "Введите слоган или сайт, либо пропустите этот шаг"
    finish = "Ожидайте, ваша заявка отправлена"


class Video:
    enter_url = "Стоимость интро: {price} рублей\n\nПерейдите по ссылке https://www.renderforest.com/ru/intro-videos, выберите интро и пришлите ссылку на него"
    enter_logo = "Пришлите фото логотипа в высоком качестве"
    enter_text = "Введите слоган или сайт, либо пропустите этот шаг"
    pay = "Стоимость интро: {price} рублей"
    finish = "Ожидайте, ваша заявка отправлена"


class SendVideo:
    enter_video = "Пришлите видео"
    finish = "Видео отправлено заказчику"
