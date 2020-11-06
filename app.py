from flask import Flask, request, render_template
import random

app = Flask(__name__)
app.debug = True
def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What are your favorite Fro-Yo toppings? <br/>
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get("flavor")
    users_froyo_toppings = request.args.get("toppings")
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {users_froyo_toppings}!'

    
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color?<br/>
        <input type="text" name="color"><br/>
        What is your favorite animal?<br/>
        <input type="text" name="animal"><br/>
        What is your favorite city?<br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_favorite_color = request.args.get("color")
    users_favorite_animal = request.args.get("animal")
    users_favorite_city = request.args.get("city")
    return f"Wow, I didn't know {users_favorite_color} {users_favorite_animal} lived in {users_favorite_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Type a secret message:<br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get("message")
    return sort_letters(users_message)

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    users_operand1 = request.args.get("operand1")
    users_operand2 = request.args.get("operand2")
    users_operator = request.args.get("operation")

    if users_operator == "add":
        calc = int(users_operand1) + int(users_operand2)
    elif users_operator == "subtract":
        calc = int(users_operand1) - int(users_operand2)
    elif users_operator == "multiply":
        calc = int(users_operand1) * int(users_operand2)
    else:
        calc = int(users_operand1) / int(users_operand2)
    return f"{calc}"

# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
