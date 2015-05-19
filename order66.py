"""
Order 66
"""

import asyncio

def _initialise(Handlers, bot=None):
	Handlers.register_admin_command(["resetjedi"])
	Handlers.register_user_command(["iamajedi", "amiajedi", "ajediiam", "whoisjedi", "iamsith", "order"])
	return[]

def iamajedi(bot, event, *args):
	bot.user_memory_set(event.user.id_.chat_id, 'jedi_status', 'Jedi')
	text =  bot.conversation_memory_get(event.conv_id, 'Yoda')
	if text == event.user.id_.chat_id:
		bot.conversation_memory_set(event.conv_id, 'Yoda', None)
		bot.send_message_parsed(event.conv, ("<b>{}</b> has stepped down from being Yoda and is just a Jedi.").format(event.user.full_name))
	else:
		bot.send_message_parsed(event.conv, ("<b>{}</b> has become a Jedi.").format(event.user.full_name))

def ajediiam(bot, event, *args):
	text = bot.conversation_memory_get(event.conv_id, 'Yoda')
	if text is None:
		bot.conversation_memory_set(event.conv_id, 'Yoda', event.user.id_.chat_id)
		text = bot.user_memory_set(event.user.id_.chat_id, 'jedi_status', 'Jedi')
		bot.send_message_parsed(event.conv, ("<b>{}</b> has become Yoda.").format(event.user.full_name))
	else:
		bot.send_message_parsed(event.conv, "There is already a Yoda for this chat")

def amiajedi(bot, event, *args):
	text = bot.user_memory_get(event.user.id_.chat_id, 'jedi_status')
	if text is None:
		bot.send_message_parsed(event.conv, ("<b>{}</b>, you are not even a youngling.").format(event.user.full_name))
	else:
		if text == 'Jedi':
			text =  bot.conversation_memory_get(event.conv_id, 'Yoda')
			if text == event.user.id_.chat_id:
				bot.send_message_parsed(event.conv, ("<b>{}</b>, a Jedi you are.").format(event.user.full_name))
			else:
				bot.send_message_parsed(event.conv, ("<b>{}</b>, you are a Jedi.").format(event.user.full_name))

def iamsith(bot, event, *args):
	bot.send_message_parsed(event.conv, ("Coming soon..."))

def resetjedi(bot, event, *args):
	bot.conversation_memory_set(event.conv_id, 'Yoda', None)
	for u in sorted(event.conv.users, key=lambda x: x.full_name.split()[-1]): 
		bot.user_memory_set(u.id_.chat_id, 'jedi_status', None)

def whoisjedi(bot, event, *args):
	yoda = bot.conversation_memory_get(event.conv_id, 'Yoda')
	html = "The Jedi Temple recognizes <br />"
	for u in sorted(event.conv.users, key=lambda x: x.full_name.split()[-1]): 
		jedi_status = bot.user_memory_get(u.id_.chat_id, 'jedi_status')
		if jedi_status is None:
			""" Nada """
		else:
			if yoda == u.id_.chat_id:
				html += ("<b>{}</b> is Yoda <br />").format(u.full_name)
			else:
				html += ("<b>{}</b> is a Jedi <br />").format(u.full_name)
	bot.send_html_to_conversation(event.conv, html)

def order(bot, event, orderNumber, *args):
	if orderNumber == '66':
		html = "Executing all Jedi<br />"
		eliminatedCount = 0
		yoda =  bot.conversation_memory_get(event.conv_id, 'Yoda')
		for u in sorted(event.conv.users, key=lambda x: x.full_name.split()[-1]): 
			jedi_status = bot.user_memory_get(u.id_.chat_id, 'jedi_status')
			if not jedi_status is None:
				html += ("Clone trooper aims at <b>{}</b><br />").format(u.full_name)
				if yoda == u.id_.chat_id:
					html += ("<b>{}</b> escapes to Dagobah<br />").format(u.full_name)
				else:
					html += ("<b>{}</b> is no longer a Jedi<br />").format(u.full_name)
					eliminatedCount += 1
					bot.user_memory_set(u.id_.chat_id, 'jedi_status', None)
		if eliminatedCount > 0:
			html += ("{} jedi eliminated!").format(eliminatedCount)
		else:
			html += "None eliminated!"
		bot.send_html_to_conversation(event.conv, html)
	elif orderNumber == '42':
		bot.send_message_parsed(event.conv, ("<b>{}</b> In the wrong Sci Fi universe you are! Babel Fish we have not.").format(event.user.full_name)) 
	elif orderNumber == '55':
		bot.send_message_parsed(event.conv, ("<b>{}</b> Sammy Hagar you are not!").format(event.user.full_name)) 
	elif orderNumber == '65':
		bot.send_message_parsed(event.conv, ("<b>{}</b> so close...").format(event.user.full_name)) 
	elif orderNumber == '67':
		bot.send_message_parsed(event.conv, ("<b>{}</b> too far...").format(event.user.full_name)) 
	elif orderNumber == '69':
		bot.send_message_parsed(event.conv, ("<b>{}</b> your mind out of the gutter you must get!").format(event.user.full_name)) 
	else:
		bot.send_message_parsed(event.conv, ("<b>{}</b> unknown order.").format(event.user.full_name)) 


