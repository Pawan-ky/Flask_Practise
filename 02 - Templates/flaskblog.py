# 
#  all html files should be in "templates" directory (check the directory name carefully)
# 

from flask import Flask, render_template, url_for

app = Flask(__name__)

posts =[
    {
        'author':'pawan kumar',
        'title':'post 1',
        'content': 'first post',
        'date_posted':'20-08-2022'
    },
        {
        'author':'vayu kumar',
        'title':'post 2',
        'content': 'second post',
        'date_posted':'22-08-2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
