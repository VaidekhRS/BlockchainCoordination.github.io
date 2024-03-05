# Import necessary modules
import json

# Define the Tech Ready Blocks data as a list of dictionaries
tech_ready_blocks = [
    {
        "TRB Code": "GWEC22FA01",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Attenuator",
        "Level Number": 1,
        "Level Meaning": "Concept & Research"
    },
    {
        "TRB Code": "GWEC22FA02",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Attenuator",
        "Level Number": 2,
        "Level Meaning": "Concept Design"
    },
    {
        "TRB Code": "GWEC22FA02",
        "Technology Area": "Garden Wave Energy Converter",
        "Year Commenced": 2022,
        "Specific Invention": "Fountain Attenuator",
        "Level Number": 3,
        "Level Meaning": "Early Prototype"
    },
]

# Convert the Tech Ready Blocks data to JSON format
trb_json = json.dumps(tech_ready_blocks)

# Write the JSON data to a file
with open('trb_data.json', 'w') as file:
    file.write(trb_json)
