Modern Pokedex Web Application
Description
This project is a modern, web-based Pokedex application built with Flask and the PokeAPI. It allows users to search for Pokemon, view detailed information about each Pokemon, and browse a comprehensive list of all available Pokemon.
Features

Search for Pokemon by name
Display detailed information about each Pokemon, including:

Basic stats (ID, height, weight, base experience)
Types
Abilities
Base stats with visual representation
Moves (first 5)
Game versions the Pokemon appears in


View sprites of each Pokemon (normal and shiny, front and back)
Browse a complete list of all available Pokemon
Modern, responsive design with Pokemon-inspired styling

Technologies Used

Python 3.x
Flask
HTML5
CSS3
PokeAPI

Setup and Installation

Clone the repository:
Copygit clone https://github.com/yourusername/modern-pokedex.git
cd modern-pokedex

Create a virtual environment and activate it:
Copypython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
Copypip install -r requirements.txt

Run the Flask application:
Copypython app.py

Open your web browser and navigate to http://127.0.0.1:5000/

Usage

On the home page, you can either:

Enter a Pokemon name in the search bar and click "Search"
Click on any Pokemon name from the list of all Pokemon


View the detailed information about the selected Pokemon
Click "Search Another Pokemon" to return to the home page

Project Structure
Copymodern-pokedex/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
├── static/
│   └── styles.css          # CSS styles for the application
└── templates/
    ├── index.html          # Home page template
    └── result.html         # Pokemon details page template
Contributing
Contributions to improve the project are welcome. Please follow these steps:

Fork the repository
Create a new branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

PokeAPI for providing the Pokemon data
The Pokemon Company for the inspiration and color scheme
