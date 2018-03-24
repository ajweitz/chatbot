from Bot import Bot

bot = Bot()
output_prefix = "You: "
user_input = input(output_prefix)
while user_input != "exit":
    print("Bot: "+bot.respond(user_input))
    user_input = input(output_prefix)
