# Import the necessary modules
import json
import genanki
from os.path import basename

# Read the template JSON file
with open("./templates.json", "r") as f:
    templates = json.load(f)

# Create a custom model with the fields we want
model = genanki.Model(
  1474397062,
  "Carnet B",
  fields=[
    {'name': 'Question'},
    {'name': 'Image'},
    {'name': 'QType (0=kprim,1=mc,2=sc)'},
    {'name': 'Q_1'},
    {'name': 'Q_2'},
    {'name': 'Q_3'},
    {'name': 'Answers'},
    {'name': 'Sources'}
    ],
  templates=[
    {
      'name': 'AllInOne (kprim, mc, sc)',
      'qfmt': templates["front_template"],
      'afmt': templates["back_template"]
      },
  ],
  css = templates["styling"]
  )

# Create the deck
deck = genanki.Deck(
  2177067181,
  "Carnet B"
  )

# Create the package
package = genanki.Package(deck)

# Read the data JSON file
with open("./data.json", "r") as f:
    data = json.load(f)


img_files = []

# Iterate over each JSON element
for item in data:
    img = item["img"]
    fields=[
            item["pregunta"],
            f'<img src="{basename(img)}">',
            "2", #QType
            item["a."], item["b."], item["c."],
            item["correcta"],
            item["explicacion"]
            ]
    
    # Create an Anki note with the custom model and assign values to each field
    note = genanki.Note(
        model=model,
        fields=fields
        )
        
    if img:
        package.media_files.append(img)
        img_files.append(img)
    
    deck.add_note(note)

# Generate and save the apkg file
genanki.Package(deck, img_files).write_to_file("Carnet B.apkg")