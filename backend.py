import openai 

class chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self,user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            promppt = user_input,
            max_token = 4000,
            temperature = 0.5
        ).choice[0].text
        return response
    

if __name__ == "__name__":
    chatbot = chatbot()
    response = chatbot.get_response("write a joke")
    print(response)