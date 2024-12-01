from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Bot tokeningizni kiriting
TOKEN = '7733320431:AAG3OPuuzytTPOAUzLZXZ-2fxYeky1nbRe4'

# /start komanda
async def start(update: Update, context):
    main_menu = [
        ['📚 Kurslar', 'ℹ️ Biz haqimizda'],
        ['📞 Murojaat qilish', '📍 Manzil']
    ]
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    
    await update.message.reply_text(
        """🖋️ ***Assalomu alaykum va o'quv markazimizga xush kelibsiz!***

***Biz — Perfect Generation O'quv Markazi, ilg'or ta'lim va sifatli kurslar bilan sizni o'qitishni maqsad qilganmiz.***  
📚 **Kurslarimiz:**  
🔹 **IT kurslari**  
🔹 **Gimnastika va jismoniy tarbiya**  
🔹 **Ingliz tili va Rustili tillari**  
🔹 **Maxsus o'quv dasturlari va individual mashg'ulotlar**  
🔹 **Onlayn darslar va o'qituvchilar bilan doimiy aloqalar**  

🔍 ***Quyidagi menyudan kerakli bo‘limni tanlang:***""", 
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Katalog bo‘limini ko‘rsatish
async def show_catalog(update: Update, context):
    catalog_menu = [
        ['💻️IT', '👶 Bolalar uchun'],
        ['📑 Fan to`garaklar', '🏋 Sport'],
        ['🔙 Ortga']
    ]
    reply_markup = ReplyKeyboardMarkup(catalog_menu, resize_keyboard=True)
    
    await update.message.reply_text(
        "Pastdagi tugmalardan o'zingizga kerakli mahsulot kategoriyasini tanlang:", 
        reply_markup=reply_markup
    )

# Turli kurslar bo'yicha ma'lumotlar
async def show_divans(update: Update, context):
   await update.message.reply_text(
        "💻 ***IT kurslarimiz:***\n\n"
        "- ***Zamonaviy Kompyuter savodxonligi:***\n"
        "  ***Davomiyligi:*** 3 oy, Haftasiga 3 marta\n"
        "  ***Narxi:*** Oyiga 390,000 so‘m\n\n"
        "- ***Frontend kursi:***\n"
        "  ***Davomiyligi:*** 6 oy\n"
        "  ***Narxi:*** 490,000 so‘m\n\n"
        "- Batafsil ma'lumot olish uchun biz bilan bog'laning",
         parse_mode="Markdown"
    )


async def show_stols(update: Update, context):
    await update.message.reply_text(
        "📚 ***Fan to‘garaklari:***\n\n"
        "- ***Ingliz tili:***\n"
        "  Boshlang‘ich va o‘rta darajadagi o‘quvchilar uchun.\n"
        "  ***Davomiyligi:*** 6 oy, Haftasiga 2 marta\n"
        "  ***Narx:*** 350,000 so‘m\n\n"
        "- ***Rus tili:***\n"
        "  Suhbat va yozuv ko‘nikmalarini rivojlantirish.\n"
        "  ***Davomiyligi:*** 4 oy, Haftasiga 3 marta\n"
        "  ***Narx:*** 350,000 so‘m\n\n"
        "- ***Matematika:***\n"
        "  Maktab darsliklari asosida chuqurlashtirilgan mashg‘ulotlar.\n"
        "  ***Davomiyligi:*** 6 oy, Haftasiga 3 marta\n"
        "  ***Narx:*** 350,000 so‘m\n\n"
        "- ***Ona tili va Adabiyot:***\n"
        "  Yozma va og‘zaki savodxonlikni rivojlantirish.\n"
        "  ***Davomiyligi:*** 5 oy, Haftasiga 2 marta\n"
        "  ***Narx:*** 270,000 so‘m\n\n"
        "- ***Biologiya:***\n"
        "  Biologiyani chuqur o‘rganish uchun qo‘shimcha mashg‘ulotlar.\n"
        "  ***Davomiyligi:*** 3 oy, Haftasiga 2 marta\n"
        "  ***Narx:*** 350,000 so‘m\n\n"
        "- ***Mental arifmetika:***\n"
        "  Bolalar uchun tez hisoblash ko‘nikmalarini rivojlantirish.\n"
        "  ***Davomiyligi:*** 4 oy, Haftasiga 2 marta\n"
        "  ***Narx:*** 300,000 so‘m\n\n"
        "- Batafsil ma'lumot olish uchun biz bilan bog'laning",
        parse_mode="Markdown"
    )


async def show_beds(update: Update, context):
    await update.message.reply_text(
        "🏋️ ***Sport bo‘limi:***\n\n"
        "- ***Sog‘lomlashtiruvchi gimnastika:***\n"
        "  ***Davomiyligi:*** 3 oy, Haftasiga 3 marta\n"
        "  ***Narxi:*** 350,000 so‘m\n\n"
        "- ***Fitness ayollar uchun:***\n"
        "  ***Davomiyligi:*** 3 oy, Haftasiga 3 marta\n"
        "  ***Narxi:*** 250,000 so‘m\n\n"
        "- Batafsil ma'lumot olish uchun biz bilan bog'laning",
        parse_mode="Markdown"
    )


async def show_shelves(update: Update, context):
    await update.message.reply_text(
        "🤸 ***Gimnastika:***\n\n"
        "- ***Bolajonlar uchun gimnastika***\n"
        "  ***Davomiyligi:*** 4 oy, Haftasiga 3 marta\n"
        "  ***Narxlar:*** 350,000 so‘m\n\n"
        "- ***Uy vazifalarni bajarish:***\n"
        "  Individual mashg‘ulotlar bilan yordam beriladi.\n"
        "  ***Narx:*** 400,000 so‘m\n\n"
        "- ***Maktabgacha mukammal tayyorgarlik \\(6\\-7 yosh\\):***\n"
        "  Yozish, o‘qish, matematikaga tayyorlash.\n"
        "  ***Davomiyligi:*** 6 oy, Haftasiga 2 marta\n"
        "  ***Narx:*** 350,000 so‘m\n\n"
        "- ***Logoped:***\n"
        "  Nutqni to‘g‘irlash va rivojlantirish uchun maxsus mashg‘ulotlar.\n"
        "  ***Narx:*** 80,000 so‘m\n\n",
        parse_mode="Markdown"
    )


# Manzil
async def handle_location(update: Update, context):
    google_maps_link = "https://www.google.com/maps?q=41.416307,69.312220"
    await update.message.reply_text(
        f"***Bizning manzilimiz***:\n***Mo`ljal: 26-maktab***\n\nGoogle Xarita: [Google Maps]({google_maps_link})", 
        parse_mode="Markdown"
    )


# Aloqa
async def handle_contact(update: Update, context):
    await update.message.reply_text(
        """🖋️ ***Assalomu alaykum va o'quv markazimizga xush kelibsiz!***

***Biz — Perfect Generation O'quv Markazi, ilg'or ta'lim va sifatli kurslar bilan sizni o'qitishni maqsad qilganmiz.***  
📚 ***Kurslarimiz:***  
🔹 ***IT kurslari***  
🔹 ***Gimnastika va jismoniy tarbiya***  
🔹 ***Ingliz tili va Rus tili***  
🔹 ***Maxsus o'quv dasturlari va individual mashg'ulotlar***  
🔹 ***Onlayn darslar va o'qituvchilar bilan doimiy aloqalar***\n\n"""
        "***Biz bilan bog‘lanish uchun:***\n\n"
        "📞 ***Telefon:*** +998971005351\n"
        "📸 ***Instagram:*** [Perfect Generation](https://www.instagram.com/perfect__generation/)\n"
        "💬 ***Telegram:*** [@perfect_generation26]",
        parse_mode="Markdown"
    )


# Global o'zgaruvchi
user_contact_requesting = {}

# Buyurtma berish
async def handle_order(update: Update, context):
    global user_contact_requesting
    user_contact_requesting[update.message.chat_id] = True

    # Telefon raqamini so'rash uchun menyu
    order_menu = [
        [KeyboardButton("📞 Telefon raqamini yuborish", request_contact=True)],
        [KeyboardButton("🔙 Ortga")]
    ]
    reply_markup = ReplyKeyboardMarkup(order_menu, resize_keyboard=True)

    await update.message.reply_text(
        "📞 ***Kurslarga yozilish yoki murojaat uchun telefon raqamingizni yuboring yoki orqaga qaytish uchun tugmani bosing.***",
        reply_markup=reply_markup,
         parse_mode="Markdown"
    )

# Telefon raqamini qabul qilish
# Telefon raqamini qabul qilish
async def receive_contact(update: Update, context):
    chat_id = update.message.chat_id
    
    # Foydalanuvchi telefon raqamini yuborsa
    if update.message.contact:
        user_contact = update.message.contact.phone_number

        # Telefon raqami faqat bir marta qabul qilinadi
        if user_contact_requesting.get(chat_id, False):
            # Telefon raqamini saqlash
            save_phone_number(user_contact)
            print(f"Telefon raqami qabul qilindi: {user_contact}")
            
            # Foydalanuvchiga javob
            await update.message.reply_text(f"✅ Telefon raqamingiz qabul qilindi: {user_contact}")
            user_contact_requesting[chat_id] = False  # So'rovni yakunlash
        else:
            # Agar foydalanuvchi bir necha marta yuborsa
            await update.message.reply_text(f"✅ Telefon raqamingiz qabul qilindi: {user_contact}")

 

## Foydalanuvchi xabarlarini boshqarish
async def handle_message(update: Update, context):
    text = update.message.text.strip()

    if text == '📚 Kurslar':
        await show_catalog(update, context)
    elif text == 'ℹ️ Biz haqimizda':
        await handle_contact(update, context)
    elif text == '📞 Murojaat qilish':
        await handle_order(update, context)
    elif text == '📍 Manzil':
        await handle_location(update, context)
    elif text == '🔙 Ortga':
        await start(update, context)
    elif text == '💻️IT':
        await show_divans(update, context)
    elif text == '📑 Fan to`garaklar':
        await show_stols(update, context)
    elif text == '🏋 Sport':
        await show_beds(update, context)
    elif text == '👶 Bolalar uchun':
        await show_shelves(update, context)
    else:
        # Nomalum xabar yuborilganda
        await update.message.reply_text("Nomalum habar, o'zingizga kerakli tugmani bosing.")

# Botni ishga tushirish
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.CONTACT, receive_contact))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
