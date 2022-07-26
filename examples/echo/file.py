import os
from quanario.bot import *


def echo_file(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():   # :ru Проверяем, есть ли вложения к сообщению от пользователя
                                        # :en Check if there are attachments to the message from the user
        if message.is_files():   # :ru Проверяем, есть ли во вложениях файлы
                                 # :en Check if there are files in the attachments
            attachments = []
            for file in message.get_files():  # :ru В цикле, перебираем все файлы
                                              # :en In a loop, we go through all the files
                path = os.path.join(os.getcwd(), f"{file.id}.{file.extension}")  # :ru Указываем путь, для сохранения
                                                                                 # :en Specify the path to save
                file.save(path_to_save=path)  # :ru Сохраняем файл
                                              # :en Saving the file
                # :ru Загружаем файлы на сервера Вк и добавляем полученную строку в список 'attachments'
                # :en Upload the files to the Vk servers and add the resulting string to the list of 'attachments'
                attachments.append(bot.upload.file(user_id=message.user_id, path_to_file=path))
            bot.send.file(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
                                                     # :en Transmitting a unique user ID
                          attachment=attachments)  # :ru Передаём вложение в аргумент 'attachments'
                                                    # :en Passing the attachment to the 'attachments' argument


TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

# :ru Создаём экземпляр класса Bot, передаём в него полученный токен и идентификатор сообщества
# :en Create an instance of the Bot class, pass the received token and community ID to it
bot = Bot(token=TOKEN, app_id=APP_ID)

# :ru В методе 'run' передаём название метода, который хотим сделать вызываемым при каждом сообщении пользователя
# :en In the 'run' method, we pass the name of the method that we want to make called with each user message
bot.run(init_method=echo_file)