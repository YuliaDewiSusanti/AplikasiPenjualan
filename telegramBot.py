import telebot
import django
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'Aplikasi_Penjualan2024.settings' 
django.setup()

# from .models import *

from telegram import Update, Bot
from telegram.ext import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import KeyboardButton
from Aplikasi_Penjualan2024.models import *

API_KEY = '7276642882:AAEViQpaSKAkKmoR6WrPaj9QTK9uS8w1p0s'
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Aplikasi Penjualan Kambing')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, 'Informasi Data Pembayaran')

# @bot.message_handler(commands=['data'])
def isValidPinCode(pinCode):
	regex = "^[1-9]{1}[0-9]{2}\\S{0,1}[0-9]{3}$";
	p = re.compile(regex)
	if (pinCode == ''):
		return False;
	m = re.match(p, pinCode)
	if m is None:
		return False
	else:
		return True

def here(S):
	return any(i.isdigit() for i in S)

def tampildata(update, context):
	text = str(update.message.text).lower()
	# if here(text):
	# 	if isValidPinCode(text):
	# 		data = Model_formulir_izin_santri_send.objects.filter(pinCode =  text)
	
	Tampil = Model_transaksis.objects.all()
	message = f""" Total {Tampil.count()} Data """
			
	for data in Tampil:				
		message += f"""Daftar Data Pembayaran
					Nama Pelanggan = {data.pelanggan}
					Jenis Kambing = {data.jenis}
					Jumlah  = {data.jumlah}
					Bayar = {data.bayar} 
					Status TF = {data.status_transfer} \n \n """


	update.message.reply_text(f"{message}")	
	return	
	# print(update)
	update.message.reply_text(f"Hi, {update['message']['chat']['first_name']} PEMBAYARAN KAMBING")



print('bot Success Running')
print(Model_transaksis.objects.first())
# bot.polling()


if __name__== '__main__':
	updater = Updater(API_KEY, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(MessageHandler(Filters.text, tampildata))
	# dispatcher.add_handler(CommandHandler('start', startCommand))
	updater.start_polling(1.0)
	updater.idle()