from aiogram import types

from system.dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'product_selection_application')
async def application_handlers(callback_query: types.CallbackQuery):
    """Приложение и сайты"""
    message_text_clothing = ("✨ <b>Популярные интернет-площадки для покупки одежды:</b>\n\n"
                             "👉 <a href='https://www.dewu.com/'>Poizon</a>\n"
                             "👉 <a href='https://www.zalando.pl/'>Zalando</a>\n"
                             "👉 <a href='https://supersklep.pl/'>Supersklep</a>\n"
                             "👉 <a href='https://allegro.pl/'>Allegro</a>\n"
                             "👉 <a href='https://warsawsneakerstore.com/'>Warsawsneakerstore</a>\n"
                             "👉 <a href='https://streetstyle24.pl/'>Streetstyle24</a>\n"
                             "👉 <a href='https://www.amazon.pl/'>Amazon</a>\n"
                             "👉 <a href='https://www.spartoo.com/'>Spartoo</a>\n\n"
                             "🛍️<b> Не нашли нужного сайта или приложения?</b>\n\n"
                             "<i>Мы выкупаем товары практически с любой интернет-площадки Европы.</i>\n\n"
                             "<i>Все, что нужно сделать – отправить ссылку на интересующий товар менеджеру</i> "
                             "@wakeuplogistic"
                             "\n\nДля возврата в начало нажмите /start")
    # Клавиатура для выбора товара
    await bot.send_message(callback_query.from_user.id, message_text_clothing, disable_web_page_preview=True,
                           parse_mode=types.ParseMode.HTML)


def register_application_handlers():
    """Регистрируем handlers для обработчиков сообщений"""
    dp.register_message_handler(application_handlers)
