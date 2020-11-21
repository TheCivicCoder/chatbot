import aiml
import os

kernel= aiml.Kernel()

if os.path.isfile("aiml/bot_brain.brn"):
    kernel.bootstrap(brainFile = "aiml/bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = os.path.abspath("std-startup.xml"), commands="LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")


while True:
    message = input("enter your message to the bot: ")
    if message == "quit":
        exit(0)
    elif message == "save":
        kernel.saveBrain("aiml/bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print(bot_response)
