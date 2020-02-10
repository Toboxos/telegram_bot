class User:

    def __init__(self, data):
        self.id = data['id']
        self.is_bot = data['is_bot']
        self.first_name = data['first_name']

        self.last_name = ""
        if "last_name" in data:
            self.last_name = data['last_name']

        self.username = ""
        if "username" in data:
            self.username = data['username']

        self.language_code = None
        if "language_code" in data:
            self.language_code = data['language_code']

        self.can_join_groups = None
        if "can_join_groups" in data:
            self.can_join_groups = data['can_join_groups']

        self.can_read_all_group_messages = None
        if "can_read_all_group_messages" in data:
            self.can_read_all_group_messages = data['can_read_all_group_messages']

        self.supports_inline_queries = None
        if "supports_inline_queries" in data:
            self.supports_inline_queries = data['supports_inline_queries']   

class Chat:

    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']

        self.title = None
        if "title" in data:
            self.title = data['title']

        self.username = None
        if "username" in data:
            self.username = data['username']

        self.firstname = None   
        if "firstname" in data:
            self.firstname = data['firstname']

        self.lastname = None
        if "lastname" in data:
            self.lastname = data['lastname']

        self.photo = None
        if "photo" in data:
            self.photo = ChatPhoto(data['photo'])

        self.description = None
        if "description" in data:
            self.description = data['description']

        self.invite_link = None
        if "invite_link" in data:
            self.invite_link = data['invite_link']

    def sendText(self, text, bot, **kwargs):
        return bot.sendMessage( chat_id=self.id, text=text, **kwargs )

    def sendHTML(self, text, bot, **kwargs):
        return bot.sendMessage( chat_id=self.id, text=text, parse_mode="HTML", **kwargs )

class Message:

    def __init__(self, data):
        self.id = data['message_id']
        self.date = data['date']

        self.fromUser = None
        if "from" in data:
            self.fromUser = User(data['from'])
        
        self.chat = None
        if "chat" in data:
            self.chat = Chat(data['chat'])

        self.text = None
        if "text" in data:
            self.text = data['text']

    def reply(self, text, bot, **kwargs):
        self.chat.sendText( text, bot, reply_to_message_id=self.id, **kwargs)

class ChatPhoto:

    def __init__(self, data):
        self.small_file_id = data['small_file_id']
        self.small_file_unique_id = data['small_file_unique_id']
        self.big_file_id = data['big_file_id']
        self.big_file_unique_id = data['big_file_unique_id']