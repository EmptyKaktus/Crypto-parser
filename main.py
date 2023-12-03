from crypto_pars import Price
from API import api
import telebot

bot = telebot.TeleBot(api())

tickers_top10 = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "usdt": "tether",
    "bnb": "bnb",
    "xrp": "xrp",
    "usdc": "usd-coin",
    'ada': "cardano",
    'doge': "dogecoin",
    "sol": "solano",
    "ltc": "litecoin"
}


@bot.message_handler(commands=['start', 'hello'])
def get_text_messages(message):
    bot.send_message(message.chat.id, "Привет! Если хочушь узнать как работает бот, жми /info")


@bot.message_handler(commands=['info'])
def information(message):
    bot.send_message(message.chat.id, "Что бы посмотреть цену той или иной крипто-монеты, напишите его тикер или название монеты."
                                      " \n<i>Например:</i> <b>btc</b> или <b>bitcoin</b>"
                                      " \nЕсли вы написали тикер монеты, а бот выдал ошибку, то попрбуйте написать его полное название. "
                                      "В противном случае либо такой монеты нет, либо он еще не внесен в нашу базу данных", parse_mode="html")


@bot.message_handler()
def crypto_cur(message):
    coin = "-".join(message.text.split())

    with open("tickers.txt", "r") as file:
        for i in file:
            if



    if coin in tickers.keys():
        price = Price(tickers[coin])
        bot.send_message(message.chat.id, f"{price.price()}"
                                              "\n"
                                              "\n Дневной диапозон"
                                              f"\n <b>Max</b>: {price.max_price()}"
                                              f"\n <b>Min</b>: {price.min_price()}", parse_mode='html')
    elif coin in tickers.values():
        price = Price(coin)
        bot.send_message(message.chat.id, f"{price.price()}"
                                              "\n"
                                              "\n Дневной диапозон"
                                              f"\n <b>Max</b>: {price.max_price()}"
                                              f"\n <b>Min</b>: {price.min_price()}", parse_mode='html')
    else:
        price = Price(coin.lower())
        if price.status_code() == 200:
            bot.send_message(message.chat.id, f"{price.price()}"
                                                "\n"
                                                "\n Дневной диапозон"
                                                f"\n <b>Max</b>: {price.max_price()}"
                                                f"\n <b>Min</b>: {price.min_price()}", parse_mode='html')
            with open("tickers.txt", "a") as file:
                file.write(f"\n{price.ticker()} {coin.lower()}")
        else:
            bot.send_message(message.chat.id, "хз")


bot.polling(none_stop=True, interval=0)
