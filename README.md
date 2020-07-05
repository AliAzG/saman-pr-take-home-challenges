# Saman PR Take Home Challenges
All works have done by Ali Aminzadeh Gohari
## Getting Started
```
pip install -r requirements.txt
```
## How to run the program
```
python3 html_parse.py [step1, step2,..., step8]
```
for example to run step1 just run:
```
python3 html_parse.py step1
```
## What each stpes mean
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