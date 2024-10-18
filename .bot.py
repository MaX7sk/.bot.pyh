const TelegramBot = require('node-telegram-bot-api');
const token =
const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;

  if (text === '/start') {
    bot.sendMessage(chatId, 'مرحبًا بك في بوت التواصل الخاص بي! كيف يمكنني مساعدتك اليوم؟');
  } else {
    bot.sendMessage(chatId, `لقد استقبلت رسالتك: "${text}"`);
  }
});
