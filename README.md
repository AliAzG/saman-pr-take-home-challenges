# Saman PR Take Home Challenges
All works were done by Ali Aminzadeh Gohari.
## Getting Started Challenge1: HTML PASER
```
pip install -r requirements.txt
```
## How to run the program for html parser:
```
python3 html_parse.py [step1, step2,..., step8]
```
for example to run step1 just run:
```
python3 html_parse.py step1
```
## What each step mean
* step1: Write a script that parses the HTML files in that directory, extracts the artist names and outputs a JSON array of the unique names to stdout.
Example:
```
  ['Pablo Picasso', 'Marc Chagall', ...]
```
* step2: Modify your script to extract the title of the work as well. Modify your output format to be an array of objects.
Example:
```
[
  {
    artist: 'Pablo Picasso',
    works: ['Quatre Femmes nues et Tête sculptée, from: La Suite Vollard' ...],
  },
  ...
]
```
* step3: Modify your script yet again, extracting the price realized and including it alongside the works.
Example:
```
[
  {
    artist: 'Pablo Picasso',
    works: [
      { title: 'Femme accroupie (Jacqueline)', price: 'USD 25,000' },
      ...
    ],
  },
  ...
]
```
* step4: Modify your script one more time, separating the currency from the amount.
Example:
```
[
  {
    artist: 'Pablo Picasso',
    works: [
      { title: 'Femme accroupie (Jacqueline)', currency: 'GBP', amount: '25,000' },
      ...
    ],
  },
  ...
]
```
* step5 to step8 do the same things for `2017-12-20` directory.

## Getting Started Challenge2: MORSE SERVICE
Just run the following command in your terminal to start the Flask API:
```
python3 morse_service.py --host '0.0.0.0' --port '5002'
```
## How to Send a Request to the API:
You can send your message to the API using curl. run the following command in terminal:
```
curl -X POST '0.0.0.0:5002/service/morse' -d "message=THIS IS A TEST"
```
Instead of *THIS IS A TEST* you can write your own message
**Make sure you write your own message all in CAPITALS**

## OUTPUT
The output is something like this:
```
{"Base64":"VEhJUyBJUyBBIFRFU1Q=","Morse Code":"- .... .. ...  .. ...  .-  - . ... - "}
```
