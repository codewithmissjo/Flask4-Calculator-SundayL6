from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/factorial/<n>')
def factorial(n):
  fact = 1
  for i in range(1,int(n)+1):
      fact = fact * i
  return f"Factorial: {fact}"



if __name__ == '__main__':
  app.run()