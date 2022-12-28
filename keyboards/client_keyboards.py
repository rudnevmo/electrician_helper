from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

k0 = KeyboardButton('До головного меню')
k1 = KeyboardButton('Переріз кабелю')
k2 = KeyboardButton('Підбір автомату захисту')
k3 = KeyboardButton('Підказка')

k4 = KeyboardButton('Алюміній')
k5 = KeyboardButton('Мідь')

k6 = KeyboardButton('400 В')
k7 = KeyboardButton('220 В')

k8 = KeyboardButton('Струм')
k9 = KeyboardButton('Потужність')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(k1).insert(k2).insert(k3)

kb_material = ReplyKeyboardMarkup(resize_keyboard=True).row(k4, k5).add(k0)

kb_voltage = ReplyKeyboardMarkup(resize_keyboard=True).row(k6, k7).add(k0)

kb_params = ReplyKeyboardMarkup(resize_keyboard=True).row(k8, k9).add(k0)
