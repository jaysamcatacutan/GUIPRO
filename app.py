from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        croissant = request.form['croissant']
        quantity = request.form['quantity']
        message = request.form.get('message')

        return render_template('thankyou.html', name=name, email=email,
                               croissant=croissant, quantity=quantity, message=message)

    return render_template('order.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)