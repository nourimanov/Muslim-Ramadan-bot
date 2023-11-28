from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
import os
from aiogram.dispatcher import FSMContext
from buttons import kb, namoz, admin
from data import DATA, EXTRA
import aiogram.utils.markdown as md
from texts import text1, text2, text3, text4, text5, text6, text7
from base import get_user, add_user, members, add_admins, members2, remove_admins, checker_type, function_db
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
   

HELP_COMMAND = """
/start - ботни ишга тушуриш
/help - буйруқлар ҳақида
/description - бот ҳақида
"""
   

class AddAdmin(StatesGroup):
    user_id = State()
    checker = State()


class RemoveAdmin(StatesGroup):
    user_id2 = State()
    checker2 = State()


@dp.message_handler(Text(equals='Bot users 🤖'))
async def menu_user(message: types.Message):
    if members():
        await message.answer(text=md.text(md.bold('Botimiz foydalanuchilari')), parse_mode=ParseMode.MARKDOWN,
                             reply_markup=admin)
        await message.answer(members(), reply_markup=admin)
    else:
        await message.answer('Hozirda foydalanuvchilarimiz yoq!')


@dp.message_handler(Text(equals='Add admin ➕'))
async def menu_user(message: types.Message):
    if not members():
        await message.answer('Hozirda foydalanuchilarimiz yoq!')
    else:
        await message.answer(members())
        await AddAdmin.user_id.set()
        await message.answer('User ID ni yuboring: ')


@dp.message_handler(state=AddAdmin.user_id)
async def adder(message: types.Message, state: FSMContext):
    await state.update_data(user_id=message.text)
    async with state.proxy() as data:
        if get_user(message.text):
            ikm = InlineKeyboardMarkup()
            ikm.add(InlineKeyboardButton('Ha', callback_data='ha'),
                    InlineKeyboardButton('Yoq', callback_data='yoq'))
            await AddAdmin.next()
            await message.answer('Siz shu userni haqiqatda ham admin qilmoqchimsiz?', reply_markup=ikm)
        else:
            await message.answer('Bunday ID dagi user bazada yoq!')
            await state.finish()


@dp.callback_query_handler(state=AddAdmin.checker)
async def yes_handler(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        # await callback.message.delete()
        if callback.data == 'ha':
            add_admins(data['user_id'])
            await bot.edit_message_text('Success', callback.message.chat.id, callback.message.message_id)
        if callback.data == 'yoq':
            await bot.edit_message_text('Operazion cancelled', callback.message.chat.id, callback.message.message_id)
    await callback.answer()
    await state.finish()


@dp.message_handler(Text(equals='Remove admin ➖'))
async def menu_user2(message: types.Message):
    if not members2():
        await message.answer('Hozirda adminlarimiz yoq!')
    else:
        await message.answer(members2())
        await RemoveAdmin.user_id2.set()
        await message.answer('User ID ni yuboring: ')


@dp.message_handler(state=RemoveAdmin.user_id2)
async def adder2(message: types.Message, state: FSMContext):
    await state.update_data(user_id2=message.text)
    async with state.proxy() as data:
        if get_user(message.text):
            ikm2 = InlineKeyboardMarkup()
            ikm2.add(InlineKeyboardButton('Ha', callback_data='ha1'),
                     InlineKeyboardButton('Yoq', callback_data='yoq1'))
            await RemoveAdmin.next()
            await message.answer('Siz shu adminni haqiqatdan ham bekor qilmoqchimisiz?', reply_markup=ikm2)
        else:
            await message.answer('Bunday ID dagi user bazada yoq!')
            await state.finish()


@dp.callback_query_handler(state=RemoveAdmin.checker2)
async def yes_handler2(callback: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        # await callback.message.delete()
        if callback.data == 'ha1':
            remove_admins(data['user_id2'])
            await bot.edit_message_text('Success', callback.message.chat.id, callback.message.message_id)
        if callback.data == 'yoq1':
            await bot.edit_message_text('Operazion cancelled', callback.message.chat.id, callback.message.message_id)
    await callback.answer()
    await state.finish()


@dp.message_handler(Text(equals='User menu 🧩'))
async def menu_user(message: types.Message):
    await message.answer(text=md.text(md.bold('Main menu')), parse_mode=ParseMode.MARKDOWN, reply_markup=kb)


@dp.message_handler(Text(equals='🔄'))
async def backpack(message: types.Message):
    if checker_type(str(message.from_user.id)):
        await message.answer(text=md.text(md.bold('Admin menu')), parse_mode=ParseMode.MARKDOWN, reply_markup=admin)
    else:
        await message.answer(text=md.text(md.bold('Bot updated 🔄')), parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(Text(equals='Namoz vaqtlari ⏰'))
async def namoz_vaqtlari(message: types.Message):
    await message.answer(text=md.text(md.bold('Viloyat yoki shaxarlardan birini tanlang!')), parse_mode=ParseMode.MARKDOWN,
                         reply_markup=namoz)


@dp.message_handler(Text(equals='Xorazm 🏠'))
async def xorazm1(message: types.Message):
    await message.answer(text1, parse_mode=ParseMode.MARKDOWN, reply_markup=namoz)


@dp.message_handler(Text(equals='Toshkent 🏠'))
async def toshkent1(message: types.Message):
    await message.answer(text2, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=namoz)


@dp.message_handler(Text(equals='Samarqand 🏠'))
async def samarqand1(message: types.Message):
    await message.answer(text3, parse_mode=ParseMode.MARKDOWN, reply_markup=namoz)


@dp.message_handler(Text(equals='Andijon 🏠'))
async def andijon1(message: types.Message):
    await message.answer(text4, parse_mode=ParseMode.MARKDOWN, reply_markup=namoz)


@dp.message_handler(Text(equals='Buxoro 🏠'))
async def buxoro1(message: types.Message):
    await message.answer(text5, parse_mode=ParseMode.MARKDOWN, reply_markup=namoz)


@dp.message_handler(Text(equals='Orqaga 🚪'))
async def orqaga(message: types.Message):
    await message.answer(text='Main menu', parse_mode=ParseMode.MARKDOWN, reply_markup=kb)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    if not get_user(str(message.from_user.id)) and str(message.from_user.id) == '190767640':
        add_user(str(message.from_user.id), message.from_user.username, True)
        await message.answer(text=md.text(md.bold('Assalamu aleykum, xush kelibsiz!')),
                             parse_mode=ParseMode.MARKDOWN, reply_markup=admin)
        await message.delete()
    elif not get_user(str(message.from_user.id)) and not checker_type(str(message.from_user.id)):
        add_user(str(message.from_user.id), message.from_user.username, False)
        await message.answer(text=md.text(md.bold('Assalamu aleykum, xush kelibsiz!!')),
                             parse_mode=ParseMode.MARKDOWN, reply_markup=kb)
        await message.delete()
    else:
        if checker_type(str(message.from_user.id)):
            await message.answer(text=md.text(md.bold('Assalamu aleykum, xush kelibsiz!')),
                                 parse_mode=ParseMode.MARKDOWN, reply_markup=admin)
            await message.delete()
        else:
            await message.answer(text=md.text(md.bold('Assalamu aleykum, xush kelibsiz!')),
                                 parse_mode=ParseMode.MARKDOWN, reply_markup=kb)
            await message.delete()


@dp.message_handler(Text(equals='Saxarlik duosi 🤲🏻'))
async def saxarlik(message: types.Message):
    await message.answer(text6, parse_mode=ParseMode.MARKDOWN, reply_markup=kb)


@dp.message_handler(Text(equals='Iftorlik duosi 🤲🏻'))
async def iftorlik(message: types.Message):
    await message.answer(text7, parse_mode=ParseMode.MARKDOWN, reply_markup=kb)


@dp.message_handler(Text(equals="Bog'lanish 📥"))
async def boglanish(message: types.Message):
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton('Admin 📞', callback_data='net', url='https://t.me/nuraliy'))
    await message.answer(EXTRA[0], reply_markup=ikm)


@dp.message_handler(Text(equals='Hadislar 📚'))
async def icon(message: types.Message):
    cur_page = 1
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton('⬅️', callback_data=f'orqa1'),
            InlineKeyboardButton(f'{cur_page}/{len(DATA)}', callback_data='ide'),
            InlineKeyboardButton('➡️', callback_data=f'oldi2'))
    await message.answer(DATA[cur_page-1], reply_markup=ikm)


@dp.callback_query_handler()
async def backer(callback: types.CallbackQuery):
    but = callback.data
    if but.startswith('orqa'):
        cur_page = int(but.split('orqa')[-1])
    elif but.startswith('oldi'):
        cur_page = int(but.split('oldi')[-1])
    else:
        cur_page = int(but.split('ide')[-1])

    ikm = InlineKeyboardMarkup()
    ikm.add(
        InlineKeyboardButton(text='⬅ ', callback_data=f'orqa{len(DATA) if cur_page == 1 else cur_page - 1}'),
        InlineKeyboardButton(text=f'{cur_page}/{len(DATA)}', callback_data='ide'),
        InlineKeyboardButton(text='➡️', callback_data=f'oldi{1 if cur_page == len(DATA) else cur_page + 1}')
    )
    await bot.edit_message_text(DATA[cur_page-1], callback.from_user.id, callback.message.message_id, reply_markup=ikm)
    await callback.answer(str(cur_page))


async def on_startup(dp):
    function_db()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)
