from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factorial/<n>')
def factorial(n):
    fact = 1
    for i in range(1,int(n)+1):
        fact = fact * i
    return f"Output: {fact}"
    
@app.route('/fibonacci/<n>')
def fibonacci(n):
    a = 0
    b = 1
    output = 0
    if int(n) < 0:
        print("ERROR")
    elif int(n) == 0:
        output = a
    elif int(n) == 1:
        output = b
    else:
        for i in range(2, int(n)):
            c = a + b
            a = b
            b = c
        output = b
    return f"Output: {output}"

#/average?num1=3&num2=4
@app.route('/average')
def calcAvg():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
    except:
        return f"ERRRRRORRRRR"
    else:
        return f"Output: {(num1 + num2) / 2}"

@app.route('/json', methods = ['GET', 'POST'])
def json():
    data = request.json
    output = ""
    output += factorial(data['factorial']) + ", "
    output += fibonacci(data["fibonacci"]) + ", "
    x = int(data['avg1'])
    y = int(data['avg2'])
    output += str((x+y)/2)
    return output

if __name__ == '__main__':
  app.run()