from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Saxarlik duosi 🤲🏻')
b2 = KeyboardButton(text='Iftorlik duosi 🤲🏻')
b3 = KeyboardButton(text='Namoz vaqtlari ⏰')
b4 = KeyboardButton(text='Hadislar 📚')
b5 = KeyboardButton(text="Bog'lanish 📥")
b6 = KeyboardButton(text='🔄')
kb.add(b5).add(b1, b2).add(b3, b4).add(b6)


namoz = ReplyKeyboardMarkup(resize_keyboard=True)
xorazm = KeyboardButton(text='Xorazm 🏠')
toshkent = KeyboardButton(text='Toshkent 🏠')
samarqand = KeyboardButton(text='Samarqand 🏠')
andijon = KeyboardButton(text='Andijon 🏠')
buxoro = KeyboardButton(text='Buxoro 🏠')
back = KeyboardButton(text='Orqaga 🚪')
namoz.add(xorazm, buxoro).add(toshkent, andijon, samarqand).add(back)


admin = ReplyKeyboardMarkup(resize_keyboard=True)
bot_users = KeyboardButton(text='Bot users 🤖')
add_admin = KeyboardButton(text='Add admin ➕')
remove_admin = KeyboardButton(text='Remove admin ➖')
# send_ads = KeyboardButton(text='Send ads 📜')
user_menu = KeyboardButton(text='User menu 🧩')
admin.add(user_menu, bot_users).add(add_admin, remove_admin)


