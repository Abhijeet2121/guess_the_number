from flask import Flask
import random
random_num = random.randint(0,9)
print(f"{random_num}")

app = Flask(__name__)
@app.route("/")
def welcome():
    return '<h1>Welcome to Guess a number</h1>'\
            '<h2>Guess a number between 0 and 9</h2>'\
            '<img src = "https://media4.giphy.com/media/xUn3CftPBajoflzROU/200w.webp?cid=ecf05e47vcf4ujscddfol56qrasdqn9g3q27ecuplliea7m1&ep=v1_gifs_search&rid=200w.webp&ct=g", width = 200/>'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_num:
        return '<h1>Guess is Too High</h1>'\
                '<img src= "https://media0.giphy.com/media/I1t1F5ClYKrWyHtpYQ/200.webp?cid=ecf05e470ltowvamvcinpwkj6zwvrby0sxhybdq5jwdboyht&ep=v1_gifs_search&rid=200.webp&ct=g", width=300/>'

    elif guess < random_num:
        return '<h1>Guess is Too Low</h1>'\
                '<img src="https://media3.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif?cid=ecf05e47gc39ogqtdgi7j14qw5dfn6445c3d1r6kbuq30ol4&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=300/>'
    else:
        return '<h1>Yes you guessed it right </h1>'\
                '<img/ src="https://media3.giphy.com/media/6HbDw9NLMJwcDanStP/200w.webp?cid=ecf05e47ox0boaywfb2yf6oms4s0zbryzqdeb2f4wr124w4x&ep=v1_gifs_search&rid=200w.webp&ct=g", width =300/>'
    
