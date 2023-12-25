from flask import Flask,render_template
# module flask
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
  title = 'Home'
  user ='suppapol tabudda'
  return render_template('index.html',title = title , name = user)

@app.route('/about')
def about():
  return render_template('about.html', title = 'about meme')

@app.route('/contacts')
def contacts():
  line = 'abcd1234'
  tal = '094xxxxxxx'
  email = 'www@gmail.com'
  return render_template('contacts.html',title = 'contacts',email = email,line=line,tal=tal)

@app.route('/myfriends')
def myfriends():
  friends = [
  {
    'name'  : 'Johny Doe',
    'mobile' : '0989689985',
    'gender' : 'male'
  },
  {
    'name' : 'Beth Smith ',
    'mobile' : '0883647518',
    'gender' : 'female'
  },
  {
    'name' : 'Rick Prime ',
    'mobile' : '0985642715',
    'gender' : 'male'
  },
  
  ]
  return render_template('friends.html' , title = 'Myfriends',friends = friends)