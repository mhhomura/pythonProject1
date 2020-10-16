from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime
import pyttsx3;


engine = pyttsx3.init ();


now = datetime.now()
[]
bot = ChatBot('bot')
conv1 = ["Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What Day is Today?",
    '{}/{}/{} - {}:{}'.format(now.day,now.month,now.year,now.hour,now.minute),
    'What is your name?',
    'Thor',
    'Nice To meet you Thor',
    'Nice to meet you too User',
    'Can you help me?',
    'Of course, How can I help?']
Hey_Joe = ["Hey Joe", "Hey Joe, where you goin with that gun of your hand? Hey Joe, I said, where you goin with that gun in your hand? Oh Im goin down to shoot my old lady You know I caught her messin round with another man, yeah Im goin down to shoot my old lady You know I caught her messin round with another man Huh, and that aint too cool Hey Joe, I heard you shot your mama down You shot her down now Hey Joe, I heard you shot your lady down Shot her down in the ground, yeah Yeah Yes, I did, I shot her You know I caught her messin round, messin round town Yes, I did, I shot her You know I caught my old lady messin round town And I gave her the gun I shot her Alright Shoot her one more time again, baby Yeah Oh, dig it Ah, alright Hey, Joe Where you gonna run to now? Where you gonna run to? Hey Joe, I said Where you gonna run to now? Where you, where you gonna go? Well, dig Im goin way down south Way down to Mexico way Alright Im goin way down south Way down where I can be free Aint no one gonna find me Aint no hangman gonna He aint gonna put a rope around me You better believe right now I gotta go now Hey, Joe You better run on down Goodbye, everybody, ow Hey, hey, Joe"]
Simple_Man = ['Simple Man', "Mama told me when I was young Come sit beside me, my only son And listen closely to what I say And if you do this itll help you some sunny day, ah yeah Oh, take your time, dont live too fast Troubles will come and they will pass Youll find a woman, yeah, and youll find love And dont forget, son, there is someone up above And be a simple kind of man Oh, be something you love and understand Baby, be a simple kind of man Oh, wont you do this for me, son, if you can Forget your lust for the rich mans gold All that you need is in your soul And you can do this, oh baby, if you try All that I want for you my son, is to be satisfied And be a simple kind of man Oh, be something you love and understand Baby, be a simple kind of man Oh, wont you do this for me, son, if you can Oh yes, I will Boy, dont you worry, youll find yourself Follow your heart and nothing else And you can do this, oh baby, if you try All that I want for you my son, is to be satisfied And be a simple kind of man Oh, be something you love and understand Baby, be a simple kind of man Oh, wont you do this for me, son, if you can Baby, be a simple, be a simple man Oh, be something you love and understand Baby, be a simple kind of man"]


trainer = ListTrainer(bot)

trainer.train(conv1)
trainer.train(Hey_Joe)
trainer.train(Simple_Man)


while True:

    quest = input('Você: ')
    response = bot.get_response (quest)
    engine.say(response);
    engine.runAndWait();
    print('Bot: ',response)
