# -*- coding: utf-8 -*-
import requests, vk_api, random,time,traceback,json,importlib
try:
	import info
	import pod
except:
	pass
from threading import Thread
import traceback
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from python3_anticaptcha import ImageToTextTask
from python3_anticaptcha import errors
print('Yakima Visus')
time.sleep(1)
menu='Выберите функцию:\n\n1.Запустить антикик и спам\n2.Настройка\n3.Зайти в беседу по ссылке\n4.Убрать капчу на аккаунтах\n'
while True:
	try:
		a=int(input(menu))
		if a == 1:
			class MyThread(Thread):
				def __init__(self, name):
					Thread.__init__(self)
					self.name = name
				def run(self):
					vk_session = vk_api.VkApi(token=self.name)
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type_id == VkChatEventType.USER_KICKED:
									requests.get("https://api.vk.com/method/messages.addChatUser?access_token="+self.name+"&v=5.92&chat_id="+str(event.chat_id)+"&user_id="+str(event.info['user_id']))
						except:
							pass
						print('Выйти из антикика вы сможете только закрыв окно с терминалом или нажав ctrl+c\nАктивировать спам можно командой '+info.info.call+' с акка любого бота\nЗапускается антикик...')
						time.sleep(1)
			class MyThread4(Thread):
				def __init__(self, name):
					Thread.__init__(self)
					self.name = name
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											titled=vk.messages.getChat(chat_id=event.chat_id)['title']
											if titled == info.info.title:
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												a=vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,message="Приветик")
												vk.messages.edit(peer_id=event.peer_id,message=info.info.msg,message_id=a)
											if titled != info.info.title:
												a=vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,message="Вы слиты)")
												vk.messages.edit(peer_id=event.peer_id,message=info.info.msg,message_id=a)
												vk.messages.editChat(chat_id=event.chat_id,title=info.info.title)
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
										except:
											pass
						except:
							pass
			class MyThread6(Thread):
				def __init__(self, name,media):
					Thread.__init__(self)
					self.name = name
					self.media = media
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											titled=vk.messages.getChat(chat_id=event.chat_id)['title']
											if titled == info.info.title:
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,attachment=media)
											if titled != info.info.title:
												vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,attachment=media)
												vk.messages.editChat(chat_id=event.chat_id,title=info.info.title)
												try:
													vk.messages.deleteChatPhoto(chat_id=event.chat_id)
												except:
													pass
												try:
													vk.messages.unpin(peer_id=event.peer_id)
												except:
													pass
										except:
											pass
						except:
							pass
			class MyThread3(Thread):
				def __init__(self, name):
					Thread.__init__(self)
					self.name = name
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											a=vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,message="Вы слиты)")
											vk.messages.edit(peer_id=event.peer_id,message=info.info.msg,message_id=a)
										except:
											pass
						except:
							pass
			class MyThread5(Thread):
				def __init__(self, name,media):
					Thread.__init__(self)
					self.name = name
					self.media = media
				def run(self):
					def captcha_handler(captcha):
						key = ImageToTextTask.ImageToTextTask(anticaptcha_key=info.info.captcha, save_format='const') \
								.captcha_handler(captcha_link=captcha.get_url())
						return captcha.try_again(key['solution']['text'])
					vk_session = vk_api.VkApi(token=self.name, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					longpoll = VkLongPoll(vk_session)
					while True:
						try:
							for event in longpoll.listen():
								if event.type == VkEventType.MESSAGE_NEW and str(event.user_id) in info.info.ids and event.text == info.info.call:
									while True:
										try:
											vk.messages.send(random_id=random.randint(100000,999999),chat_id=event.chat_id,attachment=media)
										except:
											pass
						except:
							pass

			choice=int(input('Выберите:\n1.Просто антикик\n2.Антикик+спам\n3.Антикик + спам + смена названия конфы\n4.Спам + смена названия\n5.Только спам!\n6.спам фото/видео\n7.спам фото/видео + антикик\n8.спам фото/видео + антикик + смена названия кф\n\n'))
			if choice == 1:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread(name)
					my_thread.start()
				else:
					time.sleep(1)
			if choice == 2:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread3(name)
					my_thread.start()
					my_thread = MyThread(name)
					my_thread.start()
				else:
					print('Антикик + спам запущен! Активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 3:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread4(name)
					my_thread.start()
					my_thread = MyThread(name)
					my_thread.start()
				else:
					print('Антикик + спам + смена названия запущены! Активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 4:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread4(name)
					my_thread.start()
				else:
					print('Спам + смена названия запущены! Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 5:
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread3(name)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 6:
				media=input('Вставьте часть ссылки на фото или видео таким образом, как  в примере "photo123_45":\n')
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread5(name,media)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 7:
				media=input('Вставьте часть ссылки на фото или видео таким образом, как  в примере "photo123_45":\n')
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread5(name,media)
					my_thread.start()
					my_thread = MyThread(name)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
			if choice == 8:
				media=input('Вставьте часть ссылки на фото или видео таким образом, как  в примере "photo123_45":\n')
				for i in range(len(info.info.tokenlist)):
					name = info.info.tokenlist[i]
					my_thread = MyThread5(name,media)
					my_thread.start()
					my_thread = MyThread6(name,media)
					my_thread.start()
				else:
					print('Спам активируйте командой '+info.info.call+'!')
					time.sleep(1)
		if a == 2:
			b=int(input('Выберите, откуда будет прога брать данные:\n1.Номер + пароль в acc.txt\n2.Токены в token.txt\n\n'))
			if b == 1:
				try:
					print('Генерация конфига...')
					accs=len(open('acc.txt', 'r',encoding='utf8').readlines())
					k=open('info.py',"wt")
					k.write('class info():')
					k.close()
					print('генерация токенов и айди')
					tk=[]
					iddd=[]
					for x in range (accs):
						f=open('acc.txt',encoding='utf8').read()
						num_and_passwd=f.split('\n')[x]
						b=num_and_passwd.find(':')
						phone=num_and_passwd[:b]
						passwd=num_and_passwd[b+1:]
						try:
							f=requests.get("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=%s" % str(phone) + "&password="+str(passwd))
							tk.append(str(f.json()["access_token"]))
							iddd.append(str(f.json()["user_id"]))
						except:
							print("Акк в файле 'acc.txt', строка "+str(x+1)+" невалид")
							pass
					k=open('info.py',"at",encoding='utf8')
					k.write('\n	tokenlist ='+str(tk)+'\n	ids='+str(iddd))
					k.close()
					print("установка сообщения")
					text1=open('message.txt',"rt",encoding='utf8').read().strip("\n")
					a=open('info.py',"at",encoding='utf8')
					a.write("\n	msg='"+text1+"'\n	title='"+input('Сообщение для спама у вас теперь обновлено в файле "message.txt". Введите название беседы, какое будет при рейде: ')+"'\n	captcha='"+input('Ключ от "https://anti-captcha.com/": ')+"'\n	call='"+input("Введите боевой клич, на который рейд боты начнут спамить: ")+"'")
					a.close()
					try:
						importlib.reload(info)
						print('Готово! Данные обновлены!')
					except:
						print('Готово! Данные обновлены! НО НУЖНО ПЕРЕЗАПУСТИТЬ ПРОГУ')
						pass
					time.sleep(1)
				except:
					print('\nВы неправильно ввели данные')
					time.sleep(1)
			if b == 2:
				try:
					print('Генерация конфига...')
					k=open('info.py',"wt",encoding='utf8')
					k.write('class info():')
					k.close()
					print('генерация айди')
					accs=len(open('token.txt', 'r',encoding='utf8').readlines())
					tk=[]
					iddd=[]
					for x in range (accs):
						f=open('token.txt',encoding='utf8').read()
						token=f.split('\n')[x]
						try:
							f=requests.get("https://api.vk.com/method/users.get?access_token="+token+"&v=5.92")
							iddd.append(str(f.json()["response"][0]['id']))
							tk.append(token)
						except:
							print("Акк в файле 'acc.txt', строка "+str(x+1)+" невалид")
							pass
					print('ввод токенов')
					k=open('info.py',"at",encoding='utf8')
					k.write('\n	tokenlist ='+str(tk)+'\n	ids='+str(iddd)+'\n')
					k.close()
					print("установка сообщения")
					k=open('info.py',"rt",encoding='utf8').read()
					text=k[0:len(k)-1]
					text1=open('message.txt',"rt",encoding='utf8').read().strip("\n")
					a=open('info.py',"wt",encoding='utf8')
					a.write(text+"\n	msg='"+text1+"'\n	title='"+input('Сообщение для спама у вас теперь обновлено в файле "message.txt". Введите название беседы, какое будет при рейде: ')+"'\n	captcha='"+input('Ключ от "https://anti-captcha.com/": ')+"'\n	call='"+input("Введите боевой клич, на который рейд боты начнут спамить: ")+"'")
					a.close()
					try:
						importlib.reload(info)
						print('Готово! Данные обновлены!')
					except:
						print('Готово! Данные обновлены! НО НУЖНО ПЕРЕЗАПУСТИТЬ ПРОГУ')
						pass
					time.sleep(1)
				except Exception as e:
					print('Ошибка:\n', traceback.format_exc())
					print('\nВы неправильно ввели данные')
					time.sleep(1)
		if a == 3:
			link=input('Ссылка на беседу: ')
			print('Заход в конфу...')
			for user in info.info.tokenlist:
				requests.get("https://api.vk.com/method/messages.joinChatByInviteLink?access_token="+user+"&v=5.92&link="+link)
			else:
				print('Все зашли!')
		if a == 4:
			captcha_key=info.info.captcha
			for x in range (len(info.info.tokenlist)):
				def captcha_handler(captcha):
					key = ImageToTextTask.ImageToTextTask(anticaptcha_key=captcha_key, save_format='const') \
							.captcha_handler(captcha_link=captcha.get_url())
					return captcha.try_again(key['solution']['text'])
				try:
					token=info.info.tokenlist[x]
					iduser=info.info.ids[x]
					vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
					vk = vk_session.get_api()
					vk.messages.send(user_id=iduser,message=".",random_id=random.randint(100000,999999))
					vk.messages.editChat(chat_id=1,title=".",random_id=random.randint(100000,999999))
				except:
					pass
			else:
				print('Акки очищены от каптч!')
		if a == 00000000000000000000:
			class photos(Thread):
				def __init__(self,token,group_id,album_id,photo):
					Thread.__init__(self)
					self.token = token
					self.group_id = group_id
					self.album_id = album_id
					self.photo = photo
				def run(self):
					a=requests.get("https://api.vk.com/method/photos.getUploadServer?access_token="+self.token+"&v=5.92&album_id="+self.album_id+"&group_id="+self.group_id).json()['response']['upload_url']
					img = {'photo': ('ha.jpg', open(self.photo, 'rb'))}
					response = requests.post(a, files=img).json()
					print(response)
					while True:
						requests.get("https://api.vk.com/method/photos.save?access_token="+self.token+"&v=5.92&album_id="+self.album_id+"&group_id="+self.group_id+"&server="+str(response['server'])+'&photos_list='+str(response['photos_list'])+'&hash='+str(response['hash']))
			token=info.info.tokenlist[0]
			print("Внимание! Фото отправляются от того акка, который первый по списку в acc.txt или token.txt")
			group_id =input("Айди группы: ")
			album_id =input("Айди альбома: ")
			photo = input("Вставьте полную ссылку на фото, например, C:\\Users\\VasyaDolmat\\Pictures\\a.png: ").strip('"')
			print('Фото загружено. Началось засерание!')
			photo1 = photos(token,group_id,album_id,photo)
			photo1.start()
	except Exception as e:
		print('Ошибка:\n', traceback.format_exc())
		break
