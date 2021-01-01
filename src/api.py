from flask import Flask, render_template, request
import pprint
app = Flask(__name__)
from codename import *


@app.route('/', methods=['POST','GET'])
def create_game():

    cn=CodeName()
    if request.method=='POST':
        cn.setSeed(int(request.form.get('gameId')))

    data=cn.newGame()
    return render_template('matrix.html', data=data, gameId=cn.seed, starter=cn.starter)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0')