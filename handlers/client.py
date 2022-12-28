from aiogram import Bot
from confige import telegram_bot_token
from aiogram.utils import executor

from aiogram import types, Dispatcher
from keyboards import kb_client, kb_material, kb_voltage, kb_params

bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Привіт, {message.from_user.full_name},'
                                                     f' Сподіваюсь я стану твоїм надійним помічником'
                                                     f' \U0001F477', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Ти можеш написати боту через особисті повідомлення, звернись до нього:\n'
                            'https://t.me/electrician_assistant_bot')


@dp.message_handler(content_types='text')
async def command_main(message: types.Message):
    if message.text == 'Підказка':
        await bot.send_message(message.from_user.id, 'Поки що я вмію підказувати тільки перетин кабелю, але з часом '
                                                     'я буду знати більше.')
    elif message.text == 'Переріз кабелю':
        await command_area(message)
    elif message.text == 'Підбір автомату захисту':
        await command_automatic_protection(message)


@dp.message_handler(content_types='text')
async def command_area(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оберіть матеріал виконання', reply_markup=kb_material)
    if message.text == 'Алюміній':
        await aluminium(message)
    elif message.text == 'Мідь':
        await copper(message)
    elif message.text == 'До головного меню':
        await command_main_menu(message)


@dp.message_handler(content_types='text')
async def aluminium(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оберіть напругу живлення', reply_markup=kb_voltage)

"""
@dp.message_handler(text='Мідь')
async def copper(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оберіть напругу живлення', reply_markup=kb_voltage)


# @dp.message_handler(text='400 В')
async def four_hundred(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оберіть за яким значенням необхідний розрахунок',
                           reply_markup=kb_params)


# @dp.message_handler(text='200 В')
async def two_hundred(message: types.Message):
    await bot.send_message(message.from_user.id, 'Оберіть за явким значенням необхідний розрахунок',
                           reply_markup=kb_params)


# @dp.message_handler(text='Потужність')
async def capacity(message: types.Message):
    await message.reply('Введіть номінальну потужність в кВт')


# @dp.message_handler(text='Струм')
async def amperage(message: types.Message):
    await message.reply('Введіть номінальну силу струму, А')
    await message.reply(message.text)


# @dp.message_handler(text='Підбір автомату захисту')
async def command_automatic_protection(message: types.Message):
    await bot.send_message(message.from_user.id, 'Скоро стане доступно')


dp.message_handler(text='До головного меню')


async def command_main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Повернення до головного меню', reply_markup=kb_client)


dp.message_handler()


async def empty(message: types.Message):
    await message.reply('Такої команди в мене немає')


# def register_handlers_client(dp: Dispatcher):
#    dp.register_message_handler(command_start, commands=['start'])
#    dp.register_message_handler(command_main, commands=['help'])
#    dp.register_message_handler(command_area, text=['Переріз кабелю'])
#    dp.register_message_handler(command_automatic_protection, text=['Підбір автомату захисту'])
#    dp.register_message_handler(aluminium, text=['Алюміній'])
#    dp.register_message_handler(copper, text=['Мідь'])
#    dp.register_message_handler(four_hundred, text=['400 В'])
#    dp.register_message_handler(two_hundred, text=['220 В'])
#    dp.register_message_handler(capacity, text=['Потужність'])
#    dp.register_message_handler(amperage, text=['Струм'])
#    if dp.register_message_handler(command_area) == 'Алюміній' and dp.register_message_handler(aluminium)\
#            == '400 В': # and dp.register_message_handler(four_hundred) == 'Потужність':
#        print('sldkg')
#    dp.register_message_handler(command_main_menu, text=['До головного меню'])
#    dp.register_message_handler(empty)

"""
executor.start_polling(dp, skip_updates=True)
