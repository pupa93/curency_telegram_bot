import telebot
from secret import Token
from config import keys
from extensions import CryptoConverter, ConversionException


bot = telebot.TeleBot(Token)




@bot.message_handler(commands = ['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Что бы начать работу введите команду бота в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>Увидеть список всех досупных валют /values'
    bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for x in keys.keys():
       text = '\n'.join((text, x ))
    bot.reply_to(message, text)



@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')


        if len(values) != 3:
            raise ConversionException(f'Слишком много или мало параметров {len(values)}')
        quote, base, amount = values
        end_ammount = CryptoConverter.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    else:

        text = f'Цена {amount} {quote} в {base}: {end_ammount}'
        bot.send_message(message.chat.id, text)






bot.polling()