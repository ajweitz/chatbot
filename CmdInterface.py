from Bot import Bot

bot = Bot()
output_prefix = "You: "
user_input = input(output_prefix)
while user_input != "exit":
    print("Bot: "+bot.talk(user_input))
    user_input = input(output_prefix)
