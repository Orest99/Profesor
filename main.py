import telebot
import time
bot = telebot.TeleBot('7607049913:AAGZIfJPpNJrVd8BSEInb-1Q4PtWWHLvtqE')
@bot.message_handler(commands = ['start'])
def start (message):
    buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = telebot.types.KeyboardButton('До вибору :)')
    buttons.add(button1)

    bot.send_message(message.chat.id, 'Вітаю,я допоможу обрати/зробити павер',reply_markup=buttons)
@bot.message_handler(content_types=['text'])

def next(message):
    if message.text == 'До вибору :)':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Ознайомча інформація')
        button2 = telebot.types.KeyboardButton('Купити')
        button3 = telebot.types.KeyboardButton('Зробити')
        buttons.add(button1, button2,button3)
        bot.send_message(message.chat.id, 'Який бажаєте павер?', reply_markup=buttons)
    elif message.text == 'Ознайомча інформація':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, 'Посилання на відео : https://www.youtube.com/watch?v=G1XFOxnjMEM')
        bot.send_message(message.chat.id,' https://www.youtube.com/watch?v=iPkC28W1qfk')
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Чудовий вибір', reply_markup=buttons)
    elif message.text == 'Купити':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, 'Посилання на магазин : https://taksa.com.ua/')
        bot.send_message(message.chat.id,' https://allo.ua/')
        button1 = telebot.types.KeyboardButton('Ціна')
        button2 = telebot.types.KeyboardButton('Back')
        button3 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2,button3)
        bot.send_message(message.chat.id, 'Чудовий вибір', reply_markup=buttons)
    elif message.text == 'Зробити':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'Інформація збирання:   https://www.youtube.com/watch?v=ckn34_LugJE ')
        bot.send_message(message.chat.id,' https://www.youtube.com/watch?v=3Lr8am6iElg')
        button1 = telebot.types.KeyboardButton('Ціна')
        button2 = telebot.types.KeyboardButton('Деталі')
        button3 = telebot.types.KeyboardButton('Back')
        button4 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, 'Супер', reply_markup=buttons)

    elif message.text == 'Деталі':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Основні')
        button2 = telebot.types.KeyboardButton('Корпус')
        button3 = telebot.types.KeyboardButton('Додатково до павера')
        button4 = telebot.types.KeyboardButton('Back')
        buttons.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Деталі', reply_markup=buttons)
    elif message.text == 'Ціна':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Середня')
        button2 = telebot.types.KeyboardButton('Дорогий')
        button3 = telebot.types.KeyboardButton('Призначення')
        button4 = telebot.types.KeyboardButton('Back')
        button5 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2,button3,button4,button5)
        bot.send_message(message.chat.id, 'За яку ціну?', reply_markup=buttons)

    elif message.text == 'Середня':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, 'Як варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/romoss-30000mah-sense8-php30-401-02-belyj_2.html ')
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Чудово', reply_markup=buttons)
    elif message.text == 'Дорогий':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, 'Як варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/vneshnij-akb-romoss-60000mah-pea60-pea60-152-2142.html')
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Супер', reply_markup=buttons)
    elif message.text == 'Основні':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Плата зарядки')
        button2 = telebot.types.KeyboardButton('акумулятор')
        button3 = telebot.types.KeyboardButton('кабель_пайки')
        button4 = telebot.types.KeyboardButton('Back')
        buttons.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Деталі', reply_markup=buttons)
    elif message.text == 'Корпус':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'Тут: https://www.aliexpress.com/w/wholesale-%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81-%D0%BF%D0%BE%D0%B2%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0-18650.html?spm=a2g0o.home.auto_suggest.1.650c76dbKoRezo')
        button1 = telebot.types.KeyboardButton('Готовий')
        button2 = telebot.types.KeyboardButton('альтернатива')
        button3 = telebot.types.KeyboardButton('Back')
        buttons.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Підходить', reply_markup=buttons)
    elif message.text == 'Готовий':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'https://www.aliexpress.com/item/1005005054012421.html?spm=a2g0o.productlist.main.9.5bdfvBimvBimPm&algo_pvid=9813f3da-e651-4658-94c3-c79b9a54a09b&algo_exp_id=9813f3da-e651-4658-94c3-c79b9a54a09b-4&pdp_npi=4%40dis%21UAH%21188.14%21188.14%21%21%2131.72%2131.72%21%40211b819117294310332757687eadba%2112000031468355370%21sea%21UA%214780673103%21X&curPageLogUid=8vnt0bHo5V32&utparam-url=scene%3Asearch%7Cquery_from%3A' )
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Підходить', reply_markup=buttons)
    elif message.text == 'альтернатива':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'Можна купити харчовий лоточок для їжі в: https://avrora.ua/' )
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Підходить', reply_markup=buttons)
    elif message.text == 'Плата зарядки':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'https://www.aliexpress.com/?spm=a2g0o.productlist.logo.1.5bdfvBimvBimPm' )
        button1 = telebot.types.KeyboardButton('Повільна')
        button2 = telebot.types.KeyboardButton('Швидка')
        button3 = telebot.types.KeyboardButton('Back')
        button4 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2,button3,button4)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'Повільна':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'https://www.aliexpress.com/item/1005006178609600.html?spm=a2g0o.order_list.order_list_main.1049.6ccf1802sjjVBl#nav-review' )
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'Швидка':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'https://www.aliexpress.com/item/1005007378714516.html?spm=a2g0o.productlist.main.73.746fA3qmA3qmRu&algo_pvid=5adb9100-9b05-425d-b6df-680d680d96de&algo_exp_id=5adb9100-9b05-425d-b6df-680d680d96de-38&pdp_npi=4%40dis%21UAH%21297.19%21297.19%21%21%217.06%217.06%21%4021015c7617294316220011899e5619%2112000040492857408%21sea%21UA%214780673103%21X&curPageLogUid=4ziE01WAdPH1&utparam-url=scene%3Asearch%7Cquery_from%3A' )
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'акумулятор':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'https://akkb.com.ua/')
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'кабель_пайки':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'Рекомендую від 22 і нижче ставити: https://www.aliexpress.com/item/1005006539408592.html?srcSns=sns_Telegram&spreadType=socialShare&bizType=ProductDetail&social_params=60833899642&aff_fcid=7a7fc6f4eb9c4cc7aae5637d3671aba9-1729431938995-04738-_EJVJynr&tt=MG&aff_fsk=_EJVJynr&aff_platform=default&sk=_EJVJynr&aff_trace_key=7a7fc6f4eb9c4cc7aae5637d3671aba9-1729431938995-04738-_EJVJynr&shareId=60833899642&businessType=ProductDetail&platform=AE&terminal_id=a73dbcd17275452997c4b19b9cd970f6&afSmartRedirect=y' )
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'Додатково до павера':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('кабель зарядки')
        button2 = telebot.types.KeyboardButton('ліхтарик')
        button3 = telebot.types.KeyboardButton('стрічка(освітлення)')
        button4 = telebot.types.KeyboardButton('Back_category')
        button5 = telebot.types.KeyboardButton('Back')
        buttons.add(button1, button2, button3,button4,button5)
        bot.send_message(message.chat.id, 'Додатково', reply_markup=buttons)
    elif message.text == 'кабель зарядки':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, 'Брав такий: https://www.aliexpress.com/item/1005006129902590.html?srcSns=sns_Telegram&spreadType=socialShare&bizType=ProductDetail&social_params=60828472883&aff_fcid=4292859f20bb4e539333448703398f34-1729431986302-06446-_EQ4UzGd&tt=MG&aff_fsk=_EQ4UzGd&aff_platform=default&sk=_EQ4UzGd&aff_trace_key=4292859f20bb4e539333448703398f34-1729431986302-06446-_EQ4UzGd&shareId=60828472883&businessType=ProductDetail&platform=AE&terminal_id=a73dbcd17275452997c4b19b9cd970f6&afSmartRedirect=y')
        button1 = telebot.types.KeyboardButton('Back_category')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'ліхтарик':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id, 'https://www.aliexpress.com/item/1005005991033841.html?spm=a2g0o.productlist.main.1.5e9a7807ebu9iY&algo_pvid=a664dfa5-fb89-4b2f-aff9-585b48bc070f&algo_exp_id=a664dfa5-fb89-4b2f-aff9-585b48bc070f-0&pdp_npi=4%40dis%21UAH%2175.77%2175.77%21%21%211.80%211.80%21%40211b618e17294324548054233eb8e2%2112000035206740195%21sea%21UA%214780673103%21X&curPageLogUid=3xj21nwiJ0mS&utparam-url=scene%3Asearch%7Cquery_from%3A')
        button1 = telebot.types.KeyboardButton('Back_category')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'стрічка(освітлення)':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'https://www.aliexpress.com/item/1005007445971292.html?spm=a2g0o.order_list.order_list_main.53.3d721802oMfJZV' )
        button1 = telebot.types.KeyboardButton('Back_category')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'Призначення':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Ноут')
        button2 = telebot.types.KeyboardButton('Телефон')
        button3 = telebot.types.KeyboardButton('Back')
        button4 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2,button3,button4)
        bot.send_message(message.chat.id, 'Супер', reply_markup=buttons)
    elif message.text == 'Ноут':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'Варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/vneshnij-akb-romoss-40000mah-pea40-pro-pd-65w-pea40-282-2183h-chernyj.html')
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Супер', reply_markup=buttons)
    elif message.text == 'Телефон':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(message.chat.id,'Варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/romoss-30000mah-sense8-php30-401-02-belyj_2.html')
        button1 = telebot.types.KeyboardButton('Back')
        button2 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, 'Супер', reply_markup=buttons)
    elif message.text == 'Exit':
        bot.send_message(message.chat.id,'Exit?')
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Complete_and_exit')
        button2 = telebot.types.KeyboardButton('Stay_and_back')
        button3 = telebot.types.KeyboardButton('Back')
        buttons.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'Complete_and_exit':
        bot.send_message(message.chat.id, "Okay")
        bot.stop_polling()

    elif message.text == 'Stay_and_back':
        bot.send_message(message.chat.id, ":)")
    elif message.text == 'Back':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Купити')
        button2 = telebot.types.KeyboardButton('Зробити')
        button3 = telebot.types.KeyboardButton('Деталі')
        button4 = telebot.types.KeyboardButton('Призначення')
        button5 = telebot.types.KeyboardButton('Exit')
        buttons.add(button1, button2,button3,button4,button5)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
    elif message.text == 'Back_category':
        buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = telebot.types.KeyboardButton('Додатково до павера')
        buttons.add(button1)
        bot.send_message(message.chat.id, 'Complete', reply_markup=buttons)
bot.polling(non_stop=True)
