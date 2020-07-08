import os, argparse
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''
  
# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string 
# according to the morse code chart
app = Flask(__name__)
cors = CORS(app)
@app.route("/service/morse", methods=['POST'])
def morse_service():
    message = request.form.get('message', '') # Extract the string from the request
    message_in_base64 = base64.b64encode(message.encode('utf-8')) # Convert the message to the base64 format
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
    
    return jsonify({'Morse Code': cipher, 'Base64': message_in_base64})

# Executes the main function 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default="5002", type=str, help="Running port")
    parser.add_argument("--host", default="0.0.0.0", type=str, help="Running host")
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)