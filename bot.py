from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "توکنی_که_از_BotFather_گرفتی"  # 🔴 اینجا توکن خودت را قرار بده!

LAB_INFO = {
    "hours": "🕒 ساعت کاری:\nشنبه-چهارشنبه: ۷صبح تا ۷شب\nپنجشنبه: ۷صبح تا ۲بعدازظهر",
    "tests": "🔬 آزمایش‌های اصلی:\n- CBC\n- آزمایش ادرار\n- تست قند خون\n- تست تیروئید",
    "precare": "📌 قبل از آزمایش:\n- ۱۲ ساعت ناشتا باشید\n- آب به اندازه کافی بنوشید",
    "insurance": "🏥 بیمه‌های طرف قرارداد:\n- تامین اجتماعی\n- سلامت\n- ایران\n- پارسیان"
}

def start(update: Update, context: CallbackContext):
    keyboard = [
        ['🕒 ساعت کاری', '🔬 آزمایش‌ها'],
        ['📌 مراقبت قبل آزمایش', '🏥 بیمه‌ها']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "سلام! به ربات آزمایشگاه خوش آمدید 🌟\nلطفا گزینه مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup
    )

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    response = LAB_INFO.get(
        text.replace("🕒 ", "").replace("🔬 ", "").replace("📌 ", "").replace("🏥 ", "").lower(),
        "⚠️ لطفاً از منوی زیر انتخاب کنید."
    )
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    print("✅ ربات فعال شد! برای توقف: Ctrl + C")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()