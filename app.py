from flask import Flask, render_template

app = Flask(__name__)

# Define the participant dictionaries
participant1 = {
    "TRB Code": "GWEC22FA01",
    "Technology Area": "Garden Wave Energy Converter",
    "Year Commenced": 2022,
    "Specific Invention": "Fountain Attenuator",
    "Level Number": 1,
    "Level Meaning": "Concept & Research"
}

participant2 = {
    "TRB Code": "GWEC22FA02",
    "Technology Area": "Garden Wave Energy Converter",
    "Year Commenced": 2022,
    "Specific Invention": "Fountain Attenuator",
    "Level Number": 2,
    "Level Meaning": "Concept Design"
}

participant3 = {
    "TRB Code": "GWEC22FA03",
    "Technology Area": "Garden Wave Energy Converter",
    "Year Commenced": 2022,
    "Specific Invention": "Fountain Attenuator",
    "Level Number": 3,
    "Level Meaning": "Early Prototype"
}

participant4 = {
    "TRB Code": "GWEC22FOWC01",
    "Technology Area": "Garden Wave Energy Converter",
    "Year Commenced": 2022,
    "Specific Invention": "Fountain Oscillating Water Column",
    "Level Number": 1,
    "Level Meaning": "Concept & Research"
}

participant5 = {
    "TRB Code": "GWEC22FOWC02",
    "Technology Area": "Garden Wave Energy Converter",
    "Year Commenced": 2022,
    "Specific Invention": "Fountain Oscillating Water Column",
    "Level Number": 2,
    "Level Meaning": "Concept Design"
}

participant6 = {
    "TRB Code": "GWEC22FOWC03",
    "Technology Area": "Garden Wave Energy Converter",
    "Year Commenced": 2022,
    "Specific Invention": "Fountain Oscillating Water Column",
    "Level Number": 3,
    "Level Meaning": "Early Prototype"
}

# Store all participants in a list
participants = [participant1, participant2, participant3, participant4, participant5, participant6]

@app.route('/')
def index():
    return render_template('index.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)
