from flask import Flask, render_template, request
import os
import aiml
from autocorrect import spell

app = Flask(__name__)
#path = os.path.dirname(os.path.realpath(__file__))
BRAIN_FILE="./pretrained_model/aiml_pretrained_model.dump"
k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
    k.bootstrap(learnFiles="./pretrained_model/up.aiml")
    #k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml ")
    #k.learn(path + "/ai.aiml" )
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/up.aiml")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/getw")
def get_bot_response2():
    quest = request.args.get('msg1')
    
    answ = request.args.get('msg2')
    print(quest)
    c="<category>"
    p="<pattern>"
    t="<template>"
    cc="</category>"
    pc="</pattern>"
    tc="</template>"

    #print(query)
    f = open("./pretrained_model/up.aiml", "a")
    size=f.tell()               # the size...
    f.truncate(size-7)
    f.write('\n')
    f.write(c)
    f.write('\n\t')
    f.write(p)
    f.write(quest)
    f.write(pc)
    f.write('\n\t')

    f.write(t)
    f.write(answ)
    f.write(tc)
    f.write('\n')
    f.write(cc)
    f.write('\n')
    f.write('</aiml>')
    f.close()
    k.bootstrap(learnFiles="./pretrained_model/up.aiml")
    return 1
@app.route("/get")

    


def get_bot_response():
    query = request.args.get('msg')
    
    #query = [spell(w) for w in (query.split())]
    #question =" ".join(query)
    #questionw=question
    
    response = k.respond(query)
    if response:
        return (str(response))
    else:
        return (str(":)"))
 


    
if __name__ == "__main__":
    # app.run()
    app.run()


