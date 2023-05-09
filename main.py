from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from give_me_photo_adres import give_me_photo_adress
from func_parser import call_parser
import os

if os.listdir("C:/Users/main/Desktop/OPD_2/pic/"):
    print("Файлы уже есть")
else:
    call_parser()#Спарсить 50 случайных фотографий на хост

TOKEN_API = "5680512630:AAErrjnSsVXcBNj16grv_XIp9PkYNXiKemc"

HELP_COMMAND = """
/help - <em>список комманд</em>
/start - <em>начать работу с ботом</em>
/description - <em>описание работы бота</em>
/give - <em>отправляет стикер</em>
/quote - <em>отправляет мотивирующую цитату</em>
"""

DESCRIPTION = """
Это бот, который пока ничего не умеет. Однако в перспективе, он сможет отправлять тебе мотивационные картинки. 

Откуда он их будет брать? Либо из папки на компе, либо парсить с какого-то сайта. Не факт что парсинг будет реализован =(
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот был запущен!')

@dp.message_handler(commands = 'start')
async def start(massage: types.Message):
    await massage.answer(text="Добро пожаловать!")
    await massage.delete()

@dp.message_handler(commands = 'help')
async def help_command(message: types.Message):
    await message.reply(text = HELP_COMMAND, parse_mode="HTML")

@dp.message_handler(commands = 'description')
async def help_command(message: types.Message):
    await message.reply(text=DESCRIPTION)

@dp.message_handler(commands = 'give')
async def help_command(message: types.Message):
    await message.answer(text="Смотри какой крутой крендель сидит 😎")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEI5yFkWOIg2m4t31HQbl6tNQEuVaKDWAACpyoAAmrr8UnbwlrsloFBHS8E")
    await message.delete()


@dp.message_handler(commands = 'quote')
async def help_command(message: types.Message):
    img = InputFile(give_me_photo_adress()[0])
    await bot.send_photo(chat_id=message.chat.id, photo = img)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)