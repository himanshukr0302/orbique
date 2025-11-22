from flask import Flask, request, jsonify, send_from_directory

# simple chatbot implementation using python
def chatBot(user_input):
    if not user_input:
        return "Please say something."
    user_input = user_input.lower()
    if 'hello' in user_input:
        return 'hello, how can I serve you'
    if 'name' in user_input:
        return 'My name is Himanshu'
    elif 'old' in user_input:
        return "i am 22 years old"
    elif 'capital' in user_input:
        return 'Delhi'
    elif 'available' in user_input:
        return 'yes 5 rooms are available'
    elif 'charge' in user_input:
        return '₹1500 for 24 hours'
    elif 'tourist place' in user_input:
        return 'Yes, Taj Mahal , India Gate , Lotus Temple and many more'
    elif 'cab' in user_input:
        return 'Yes, ₹12/KM'
    elif 'food' in user_input:
        return 'Yes'
    elif 'wifi' in user_input:
        return 'yes'
    elif 'payment' in user_input:
        return 'we are accepting UPI or Cash'
    elif 'cancellation' in user_input:
        return 'Free cancellation'
    elif 'parking' in user_input:
        return 'Yes, we are providing parking in front of your room'
    else:
        return "Sorry, I don't have more information"


app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json(silent=True)
    if data and 'message' in data:
        user_input = data['message']
    else:
        user_input = request.form.get('message')
    if user_input is None:
        return jsonify({'response': 'No message provided'}), 400
    return jsonify({'response': chatBot(user_input)})


if __name__ == '__main__':
    app.run(debug=True)
