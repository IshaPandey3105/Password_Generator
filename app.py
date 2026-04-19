from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_numbers, use_symbols):
    # Base characters (lowercase always included)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    all_chars = lower
    password = []

    # Ensure at least one character from each selected option
    if use_upper:
        password.append(random.choice(upper))
        all_chars += upper
    if use_numbers:
        password.append(random.choice(numbers))
        all_chars += numbers
    if use_symbols:
        password.append(random.choice(symbols))
        all_chars += symbols

    # Fill the rest of the password length
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_chars))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    strength = ""

    if request.method == 'POST':
        length = int(request.form.get('length'))
        use_upper = request.form.get('uppercase') == 'on'
        use_numbers = request.form.get('numbers') == 'on'
        use_symbols = request.form.get('symbols') == 'on'

        password = generate_password(length, use_upper, use_numbers, use_symbols)

        # Password strength logic
        if length < 6:
            strength = "Weak"
        elif 6 <= length <= 10:
            strength = "Medium"
        else:
            strength = "Strong"

    return render_template('index.html', password=password, strength=strength)

if __name__ == '__main__':
    app.run(debug=True)