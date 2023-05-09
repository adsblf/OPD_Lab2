from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from give_me_photo_adres import give_me_photo_adress
from func_parser import call_parser
import os

def bot_func():
    if os.listdir("C:/Users/main/Desktop/OPD_Lab2/pic/"):
        print("Файлы уже есть")
    else:
        call_parser()#Спарсить 50 случайных фотографий на хост

    TOKEN_API = "5680512630:AAErrjnSsVXcBNj16grv_XIp9PkYNXiKemc"

    DESCRIPTION = """
    <b>MotivationBot</b> @OPD_Lab2_Motivation_Bot \nЭто бот, который толком ничего не умеет. Всё на что он способен: отправить крутой стикер или мотивационную цитату.
    """
    bot = Bot(TOKEN_API)
    dp = Dispatcher(bot)

    async def on_startup(_):
        print('Бот был запущен!')

    @dp.message_handler(commands = 'start')
    async def start(massage: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["help", "стикер", "цитата"]
        keyboard.add(*buttons)
        await massage.answer(text="Добро пожаловать!", reply_markup=keyboard)


    @dp.message_handler(lambda message: message.text == "help")
    async def help_command(message: types.Message):
        await message.answer(text=DESCRIPTION, parse_mode="HTML")
        await message.delete()

    @dp.message_handler(lambda message: message.text == "стикер")
    async def help_command(message: types.Message):
        await message.answer(text="Смотри какой крутой крендель сидит 😎")
        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEI5yFkWOIg2m4t31HQbl6tNQEuVaKDWAACpyoAAmrr8UnbwlrsloFBHS8E")
        await message.delete()

    @dp.message_handler(lambda message: message.text == "цитата")
    async def help_command(message: types.Message):
        img = InputFile(give_me_photo_adress()[0])
        await bot.send_photo(chat_id=message.chat.id, photo=img)
        await message.delete()

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)