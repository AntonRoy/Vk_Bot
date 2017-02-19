import vk_api


class VkPlus:
    api = None

    def __init__(self, login, password, app_id=-1):
        try:
            if app_id == -1:
                self.api = vk_api.VkApi(login, password)
            else:
                self.api = vk_api.VkApi(login, password, app_id)

            self.api.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return None


    def send(self, text, photo):
        values = {
            'chat_id': 99,
            'message': text,
            'attachment':photo
        }
        self.api.method('messages.send', values)


    def markasread(self, id):
        values = {
            'message_ids': id
        }
        self.api.method('messages.markAsRead', values)


    def remove_user(self, user_id):
        values = {
            'chat_id':99,
            'user_id': user_id
        }
        print('ok')
        self.api.method('messages.removeChatUser', values)

    def add_user(self, user_id):
        values = {
            'chat_id': 99,
            'user_id': user_id
        }
        print('ok')
        self.api.method('messages.addChatUser', values)

