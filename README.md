Created Date: 15 01 2020

## INSTALLATION:
 pip install -r Python-requirements.txt`
 

Some of the best examples of chatbots are:
1. Replika
2. Watson Assistant
3. Alexa
4. Dialogflow
5. Cleverbot

So you want to build a chatbot? No worries! 

We will be using AIML because to build a chatbot using NLP/ML/Deep Learning takes a lot of time to build while AIML helps to build a chatbot easily but the only problem is that you need to feed as many data as you can for the bot to learn and here data doesn't just mean the questions and its category but also the question pattern.


Here you will need 3 files:

1 Python file: bot.py

2,3 aiml file: learningFileList.aiml, and conversation.aiml

Data folder contains all the AIML files
Each aiml file contains the conversation patterns which the kernel will load for chatting

Note: Kernel object is the public interface to the AIML interpreter. "learn" method loads the contents of an AIML file into the kernel. While "respond" method is used to get the response from the learned AIML file. And "LEARN AIML" is the pattern that k.respond from bot.py calls. The <learn> tag loads the AIML file to respond.



