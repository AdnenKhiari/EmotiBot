from voice import get_user_input_voice, text_to_speech

class CLI():
    def __init__(self,bot) -> None:
        self.bot = bot
    
    def render(self):
        
        while True:
            # query = input("UserInput: ")
            query = get_user_input_voice()
            if query == "exit":
                break
            result = self.bot.get_result(query)
            print("EmotiBot",result)
            text_to_speech(result)