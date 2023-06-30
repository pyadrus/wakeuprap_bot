from aiogram import types

from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'answers_main_questions')
async def answers_main_questions_handlers(callback_query: types.CallbackQuery):
    """Ответы от пользователей"""
    message_text_clothing = ("<b>Оригинал❓</b>\n"
                             "<i>Весь товар в предложенных нами приложениях и сайтах является оригинальным.</i>\n\n"
                             "<b>Сколько дней доставка❓</b>\n"
                             "<i>Примерное время доставки 14-21 день с момента поступления товара на наш склад в "
                             "Польше или Китае.</i>\n\n"
                             "<b>Не нашли интересующую вас модель❓</b>\n"
                             "<i>Если вы не смогли найти интересующую вас модель, отправьте фото модели менеджеру, мы "
                             "постараемся найти самый выгодный для вас вариант.</i>\n\n"
                             "<b>Как происходит оплата❓</b>\n"
                             "<i>Мы работаем по предоплате 20%. После поступления средств мы оформляем выкуп товара и "
                             "доставляем его в Минск. Остаток стоимости оплачивается при получении.</i>\n\n"
                             "<b>🚚 Доставка по Беларуси и России</b>\n"
                             "<i>Беларусь: самовывоз Минск (ст. метро Якуба Коласа), Европочта/Белпочта (наложенный "
                             "платеж).</i>\n"
                             "<i>Россия: СДЕК</i>\n\n"
                             "<b>✏️ Для уточнения всех интересующих вопросов писать менеджеру – </b>@wakeuplogistic"
                             "\n\nДля возврата в начало нажмите /start")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, parse_mode=types.ParseMode.HTML)


def register_answers_main_questions_handlers():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(answers_main_questions_handlers)
