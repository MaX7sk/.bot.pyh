from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions

TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'  #7701101261:AAGQcU74I38WPBm6kR9KWk774yP1OOBCy7U

def start(update, context):
    update.message.reply_text('مرحبًا! أنا بوت حماية المجموعة. كيف يمكنني مساعدتك اليوم؟')

def mute_user(update, context):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=user_id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        update.message.reply_text('تم كتم المستخدم.')

def unmute_user(update, context):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=user_id,
            permissions=ChatPermissions(can_send_messages=True)
        )
        update.message.reply_text('تم فك كتم المستخدم.')

def restrict_user(update, context):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=user_id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            )
        )
        update.message.reply_text('تم تقييد المستخدم.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('mute', mute_user))
    dp.add_handler(CommandHandler('unmute', unmute_user))
    dp.add_handler(CommandHandler('restrict', restrict_user))

    updater.start_polling()
    updater.idle()

if name == '__main__':#start

    main()
