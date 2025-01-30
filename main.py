from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
YOUR_TELEGRAM_ID = 'YOUR_TELEGRAM_ID'

def start(update: Update, context: CallbackContext) -> None:
    user_first_name = update.message.from_user.first_name
    welcome_message = (
        f"سلام {user_first_name}! خوش آمدید به ربات ما 🌟\n\n"
        "راهنمای منو:\n"
        "🤖 **ساخت ربات‌های تلگرام**: ما به شما کمک می‌کنیم ربات‌های فوق‌العاده‌ای برای نیازهای خود بسازید.\n"
        "👥 **درباره ما**: با تیم پرشور و خلاق ما بیشتر آشنا شوید و از کارهای فوق‌العاده‌ای که انجام می‌دهیم، مطلع شوید.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
    )

    update.message.reply_text(welcome_message, parse_mode='Markdown')

    keyboard = [
        [KeyboardButton("👥 درباره ما"), KeyboardButton("🤖 ساخت ربات")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text('لطفاً یکی از گزینه‌های زیر را انتخاب کنید:', reply_markup=reply_markup)

def about(update: Update, context: CallbackContext) -> None:
    keyboard = [[KeyboardButton("🔙 بازگشت")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text(
        "ما یک تیم پرشور و پرانرژی هستیم که به توسعه ربات‌های تلگرام مشغولیم. برای اطلاعات بیشتر با ما تماس بگیرید!",
        reply_markup=reply_markup
    )

def build_bot(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("📦 سفارش", url=f"https://t.me/{YOUR_TELEGRAM_ID}")],
        [KeyboardButton("🔙 بازگشت")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text('برای ساخت ربات، لطفاً روی دکمه زیر کلیک کنید:', reply_markup=reply_markup)

def back(update: Update, context: CallbackContext) -> None:
    start(update, context)

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == "👥 درباره ما":
        about(update, context)
    elif text == "🤖 ساخت ربات":
        build_bot(update, context)
    elif text == "🔙 بازگشت":
        back(update, context)
    else:
        update.message.reply_text('لطفاً یکی از گزینه‌های منو را انتخاب کنید.')

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
