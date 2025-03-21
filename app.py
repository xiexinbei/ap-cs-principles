from flask import Flask, render_template, request 
from getcharacter import GetCharacter

app = Flask(__name__)

apple_home = GetCharacter(0, 0, 0, 0)

@app.route("/hello")
def hello_kitty():
    return 'hellokitty'

@app.route("/image")
def kuromi_image():
    return render_template('image.html')

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    answers = ['red', 'pink', 'blue', 'black']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)

    if request.method == 'POST':
        selected = request.form ['selected']
        if selected == answers[0]:
            apple_home.add('hellokitty')
        if selected == request.form[1]:
            apple_home.add('melody')
        if selected == request.form[2]:
            apple_home.add('hangyodon')
        if selected == request.form[3]:
            apple_home.add('kuromi')

if __name__ =='__main__':
    app.run(host='127.0.0.1')