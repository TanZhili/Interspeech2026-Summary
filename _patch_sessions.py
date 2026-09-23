import json
import re
from pathlib import Path

p = Path(r"d:\projects\interspeech2026\data\sessions.json")
sessions = json.loads(p.read_text(encoding="utf-8"))

fixes = {
    "mon-002": {
        "time": "11:00-13:00",
        "area": "1",
        "format": "Oral",
        "title": "Model of Speech Perception",
        "header": "Monday 28 September 2026 - 11:00-13:00 - Area 1 - Oral 1 - Model of Speech Perception",
    },
    "tue-037": {
        "time": "09:00-11:00",
        "area": "2",
        "format": "Oral",
        "title": "Voice Quality Aspects of Speech",
        "header": "Tuesday 29 September 2026 - 09:00-11:00 - Area 2 - Oral 5 - Voice Quality Aspects of Speech",
    },
    "wed-094": {
        "time": "09:00-11:00",
        "area": "3",
        "format": "Oral",
        "title": "Multimodal Emotion Recognition",
        "header": "Wednesday 30 September 2026 - 09:00-11:00 - Area 3 - Oral 3 - Multimodal Emotion Recognition",
    },
    "thu-152": {
        "time": "09:00-11:00",
        "area": "1",
        "format": "Oral",
        "title": "Modeling Articulation",
        "header": "Thursday 1 October 2026 - 09:00-11:00 - Area 1 - Oral 4 - Modeling Articulation",
    },
}

def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:70] or "session"

for s in sessions:
    if s["id"] in fixes:
        s.update(fixes[s["id"]])
        # refresh output slug portion
        folder, fname = s["output_path"].rsplit("/", 1)
        prefix = fname.split("-" + s["id"] + "-")[0]
        # fname is NN-id-slug
        m = re.match(r"(\d+)-", fname)
        nn = m.group(1)
        s["output_path"] = f"{folder}/{nn}-{s['id']}-{slugify(s['title'])}.md"

# Insert Monday keynote at start of Monday if missing
if not any(s["id"] == "mon-keynote" for s in sessions):
    keynote = {
        "id": "mon-keynote",
        "day": "Monday 28 September 2026",
        "day_key": "Program-Mon",
        "time": "09:30-10:30",
        "area": "",
        "format": "Keynote",
        "title": "Keynote: John H. L. Hansen",
        "header": "Monday 28 September 2026 - 09:30-10:30 - Keynote speaker - Prof John H. L. Hansen",
        "items": [
            {
                "paper_id": "",
                "time": "09:30-10:30",
                "type": "Keynote",
                "title": "Balancing Speech, Language and Hearing Science with Machine Learning Modeling in the Age of AI: “Know your Problem, Data, and Solution”",
                "presenter": "John H. L. Hansen",
                "authors": "John H. L. Hansen",
                "abstract": "The talk connects speech, language and hearing science with machine-learning modeling in the age of AI. It reviews how problem formulation, data, and solution design must stay coupled, contrasts earlier speech modeling with more recent innovations used in today's systems, and offers guidance for researchers entering the field. The take-home theme is: know your problem, know your data, and know your solution. Hansen's research has shaped speech recognition, speaker recognition and robust speech processing in noisy, stressed or emotional conditions, spanning speech production, speaker models, telecommunications, security/privacy, and assistive speech and hearing technologies.",
            }
        ],
        "output_path": "docs/by-program/2026-09-28-monday/00-mon-keynote-john-hansen.md",
    }
    # insert before first Monday session
    idx = next(i for i, s in enumerate(sessions) if s["day"].startswith("Monday"))
    sessions.insert(idx, keynote)

# Add Thursday survey talk if missing
thu = next(s for s in sessions if s["id"] == "thu-152")
if not any("Bio-Informed" in it["title"] for it in thu["items"]):
    thu["items"].insert(0, {
        "paper_id": "",
        "time": "09:00-09:40",
        "type": "Survey Talk",
        "title": "Bio-Informed Speech Processing, Modeling, and Generation",
        "presenter": "",
        "authors": "",
        "abstract": "Survey talk opening the Modeling Articulation oral session. The official program grid preserves the title but not a full abstract in the exported sheet. Treat it as a survey of biologically informed approaches to speech processing, articulatory modeling, and generation, and do not invent specific claims, datasets, or results.",
    })

p.write_text(json.dumps(sessions, ensure_ascii=False, indent=2), encoding="utf-8")
print("sessions", len(sessions))
print("patched", [s["id"] + " -> " + s["title"] for s in sessions if s["id"] in fixes or s["id"]=="mon-keynote"])
