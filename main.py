import requests
from flask import Flask, render_template, request

app = Flask(__name__)

class Pokedex():
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/pokemon'

    def get_pokemon(self, pokemon=None, limit=100):
        if pokemon:
            r = requests.get(f"{self.url}/{pokemon}", params={"limit": limit})
            try:
                return r.json()
            except:
                print("Not a valid Pokemon")
                return None
        else:
            r = requests.get(self.url, params={"limit": limit})
            return r.json()['results']

    def get_all_pokemon(self, limit=1000):
        r = requests.get(self.url, params={"limit": limit})
        return r.json()['results']

    def get_pokemon_details(self, pokemon):
        pmon = self.get_pokemon(pokemon)
        if pmon:
            details = {
                'name': pmon['name'],
                'id': pmon['id'],
                'height': pmon['height'],
                'weight': pmon['weight'],
                'base_experience': pmon['base_experience'],
                'types': [t['type']['name'] for t in pmon['types']],
                'abilities': [a['ability']['name'] for a in pmon['abilities']],
                'stats': {s['stat']['name']: s['base_stat'] for s in pmon['stats']},
                'moves': [m['move']['name'] for m in pmon['moves'][:5]],  # Limiting to first 5 moves
                'sprites': {
                    'front_default': pmon['sprites']['front_default'],
                    'back_default': pmon['sprites']['back_default'],
                    'front_shiny': pmon['sprites']['front_shiny'],
                    'back_shiny': pmon['sprites']['back_shiny']
                },
                'versions': [g['version']['name'] for g in pmon['game_indices']]
            }
            return details
        return None

myPokedex = Pokedex()

@app.route('/', methods=['GET', 'POST'])
def index():
    all_pokemon = myPokedex.get_all_pokemon()
    if request.method == 'POST':
        pokemon_name = request.form['pokemon'].lower()
        pokemon_details = myPokedex.get_pokemon_details(pokemon_name)
        if pokemon_details:
            return render_template('result.html', pokemon=pokemon_details)
        else:
            return render_template('index.html', error="Not a valid Pokemon", all_pokemon=all_pokemon)
    return render_template('index.html', all_pokemon=all_pokemon)

if __name__ == '__main__':
    app.run(debug=True)