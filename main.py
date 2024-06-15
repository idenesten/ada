from config import settings

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TELEGRAM_BOT_TOKEN = settings.SERGREY_BOT_TOKEN

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Send me a PDF file, and I will process it.')

async def handle_document(update: Update, context: CallbackContext) -> None:
    document = update.message.document
    if document.mime_type == 'application/pdf':
        file = await context.bot.get_file(document.file_id)
        await file.download_to_drive('received.pdf')
        await update.message.reply_text('PDF received and downloaded.')
        # Process the PDF file here
        # For now, just send a confirmation message
        await update.message.reply_text('PDF processing complete.')

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.MimeType('application/pdf'), handle_document))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
