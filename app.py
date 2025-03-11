from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_kitty():
    return 'hellokitty'

@app.route("/image")
def kuromi_image():
    return render_template('image.html')

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    answers = ['red', 'pink', 'blue', 'black']
if __name__ =='__main__':
    app.run(host='127.0.0.1')