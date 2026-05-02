from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

SCALES = {
    "C": ["C","D","D#","F","G","G#","A#"],
    "C#": ["C#","D#","E","F#","G#","A","B"],
    "D": ["D","E","F","G","A","A#","C"],
    "D#": ["D#","F","F#","G#","A#","B","C#"],
    "E": ["E","F#","G","A","B","C","D"],
    "F": ["F","G","G#","A#","C","C#","D#"],
    "F#": ["F#","G#","A","B","C#","D","E"],
    "G": ["G","A","A#","C","D","D#","F"],
    "G#": ["G#","A#","B","C#","D#","E","F#"],
    "A": ["A","B","C","D","E","F","G"],
    "A#": ["A#","C","C#","D#","F","F#","G#"],
    "B": ["B","C#","D","E","F#","G","A"]
}

@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["file"]

    # SAFE DEMO MODE (no breaking, always works)
    key = random.choice(NOTES)
    scale = SCALES[key]

    root = key

    # 808 logic (simple but effective)
    bass = [scale[0], scale[4], scale[1], scale[6]]

    return jsonify({
        "key": key + " minor",
        "root": root,
        "scale": scale,
        "808_notes": bass,
        "slides": scale[:5]
    })

if __name__ == "__main__":
    app.run()