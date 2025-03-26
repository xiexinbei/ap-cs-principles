from flask import Flask, render_template, request, redirect
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
        if selected == answers[1]:
            apple_home.add('melody')
        if selected == answers[2]:
            apple_home.add('hangyodon')
        if selected == answers[3]:
            apple_home.add('kuromi')

        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    answers = ['bunny or kitty', 'cute sheep', 'fish', 'black cat']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form ['selected']
        if selected == answers[0]:
            apple_home.add('hellokitty')
        if selected == answers[1]:
            apple_home.add('melody')
        if selected == answers[2]:
            apple_home.add('hangyodon')
        if selected == answers[3]:
            apple_home.add('kuromi')

        return redirect('/question/3')
    
@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    answers = ['a caring character who is always listening', 'the friend who always brings a lot of fun', 'quiet, supportive friend', 'never afraif of speak for your mind']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form ['selected']
        if selected == answers[0]:
            apple_home.add('hellokitty')
        if selected == answers[1]:
            apple_home.add('melody')
        if selected == answers[2]:
            apple_home.add('hangyodon')
        if selected == answers[3]:
            apple_home.add('kuromi')
            
if __name__ =='__main__':
    app.run(host='127.0.0.1')