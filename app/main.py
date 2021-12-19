from flask import Flask, render_template
app = Flask(__name__)
import os

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/tox/')
def my_link1():
    os.system('py tox.py')
    return ('', 204)
@app.route('/concen/')
def my_link2():
    os.system('py concen.py')
    return ('', 204)
@app.route('/gamma/')
def my_link3():
    os.system('py gamma.py')
    return ('', 204)
@app.route('/phif/')
def my_link4():
    os.system('py phif.py')
    return ('', 204)
@app.route('/temp/')
def my_link5():
    os.system('py temp.py')
    return ('', 204)


if __name__ == '__main__':
  app.run(debug=True)
