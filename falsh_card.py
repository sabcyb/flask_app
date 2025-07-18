from flask import Flask, render_template,redirect,request, url_for,abort

cards = [
    {"id": 1, "country": "Germany", "capital": "Berlin"},
    {"id": 2, "country": "France", "capital": "Paris"},
    {"id": 3, "country": "Spain", "capital": "Madrid"},
    {"id": 4, "country": "Italy", "capital": "Rome"},
    {"id": 5, "country": "Portugal", "capital": "Lisbon"},
    {"id": 6, "country": "Netherlands", "capital": "Amsterdam"},
    {"id": 7, "country": "Belgium", "capital": "Brussels"},
    {"id": 8, "country": "Sweden", "capital": "Stockholm"},
    {"id": 9, "country": "Norway", "capital": "Oslo"},
    {"id": 10, "country": "Finland", "capital": "Helsinki"},
    {"id": 11, "country": "Denmark", "capital": "Copenhagen"},
    {"id": 12, "country": "Poland", "capital": "Warsaw"},
    {"id": 13, "country": "Czech Republic", "capital": "Prague"},
    {"id": 14, "country": "Hungary", "capital": "Budapest"},
    {"id": 15, "country": "Austria", "capital": "Vienna"},
    {"id": 16, "country": "Switzerland", "capital": "Bern"},
    {"id": 17, "country": "Greece", "capital": "Athens"},
    {"id": 18, "country": "Turkey", "capital": "Ankara"},
    {"id": 19, "country": "Russia", "capital": "Moscow"},
    {"id": 20, "country": "Ukraine", "capital": "Kyiv"}
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html', name="Saber", card = cards)
@app.route('/card/<int:number>')
def card(number):
    if number > 0 and number <= len(cards):
        card = cards[int(number-1)]
        return render_template('card_view.html', id = number, card = card)
    else:
        return "Card not found", 404

@app.route('/add_cards', methods=['GET', 'POST'])
def add_cards():
    if request.method == 'POST':
        new_card = {
            "id": len(cards) + 1,
            "country": request.form['country'],
            "capital": request.form['capital']
        }
        cards.append(new_card)
        return redirect(url_for('index'))
    else:
        return render_template('add_card.html')

@app.route('/delete_card/<int:number>', methods=['GET', 'POST'])
def delete_card(number):
    if request.method == 'POST':
        del cards[number-1]
        # Adjust IDs of remaining cards
        return redirect(url_for('index'))
    else:
        return render_template('delete_card.html', id=number, card=cards[number-1])

if __name__ == '__main__':
    app.run(debug=True)