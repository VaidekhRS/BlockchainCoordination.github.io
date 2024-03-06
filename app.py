from flask import Flask, render_template

app = Flask(__name__)

# TRB data
trb_data = [
    {
        "TRB Code": "GWEC22FA01",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Attenuator",
        "Level Number": "One (01)",
        "Level Meaning": "Concept & Research"
    },
    {
        "TRB Code": "GWEC22FA02",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Attenuator",
        "Level Number": "Two (02)",
        "Level Meaning": "Concept Design"
    },
    {
        "TRB Code": "GWEC22FA03",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Attenuator",
        "Level Number": "Three (03)",
        "Level Meaning": "Early Prototype"
    },
    {
        "TRB Code": "GWEC22FOWC01",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Oscillating Water Column",
        "Level Number": "One (01)",
        "Level Meaning": "Concept & Research"
    },
    {
        "TRB Code": "GWEC22FOWC02",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Oscillating Water Column",
        "Level Number": "Two (02)",
        "Level Meaning": "Concept Design"
    },
    {
        "TRB Code": "GWEC22FOWC03",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Oscillating Water Column",
        "Level Number": "Three (03)",
        "Level Meaning": "Early Prototype"
    }
]

@app.route('/')
def index():
    return render_template('index.html', trb_data=trb_data)

if __name__ == '__main__':
    app.run()
