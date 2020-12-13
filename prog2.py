import requests
import telebot


url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = 'f08d891b7ca049242cf7bab3fc3f0034'
api_telegram = '1420145285:AAH9gbkuYwKryrO7Xaw6HSZr5QjKl2mnO7o'

bot = telebot.TeleBot(api_telegram)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Алматы', 'Астана')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name)+ '. ' 'В каком городе хотите узнать погоду?' 'Если тут нет вашего города, можете написать через клавиатуру', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def weather_send(message):
	Oltym_city = message.text


	try:

		params = {'APPID': api_weather, 'q': Oltym_city, 'units': 'metric', 'lang': 'ru'}
		result = requests.get(url, params=params)
		weather = result.json()


		if weather["main"]['temp'] < 0:
			state = "Шарф и перчатки не забудь!"
		elif weather["main"]['temp'] < 15:
			state = "Прохладно будет!"
		elif weather["main"]['temp'] < 25:
			state = "Возьми ветровку!"
		elif weather["main"]['temp'] > 38:
			state = "Не забудь головной убор! Вдруг солнечный удар получишь"
		else:
			state = "Можешь гулять в рубажке!"

		bot.send_message(message.chat.id, "В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + ' °C' + "\n" +
				"Скорость ветра " + str(float(weather['wind']['speed'])) + ' км/ч' + "\n" +
				"Давление " + str(float(weather['main']['pressure'])) + ' мм рт.ст.' + "\n" +
				"Влажность " + str(float(weather['main']['humidity'])) + ' %' + "\n\n" +
				"Описание " + str(weather['weather'][0]["description"]) +
				"\n\n" + state)

	except:
		bot.send_message(message.chat.id, "Город " + Oltym_city + " не найден")


if __name__ == '__main__':
    bot.polling(none_stop=True)


