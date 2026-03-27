#!/usr/bin/env python3
"""
TFA Meta Seeder — run this ONCE from the root of your
thefrequencyacademy-lessons repo to create meta.json in every lesson folder.
Then commit and push. GitHub Action handles everything after that.
"""
import json, os

lessons = [
    {"folder": "01-quantum-physics/quantum-physics/lesson-01", "id": "Q1", "title": "What Is Quantum Physics", "description": "The foundation of frequency science", "status": "live"},
    {"folder": "01-quantum-physics/quantum-physics/lesson-02", "id": "Q2", "title": "The Observer Effect", "description": "How consciousness shapes reality", "status": "live"},
    {"folder": "01-quantum-physics/quantum-physics/lesson-03", "id": "Q3", "title": "Wave-Particle Duality", "description": "", "status": "live"},
    {"folder": "01-quantum-physics/quantum-physics/lesson-04", "id": "Q4", "title": "Quantum Entanglement", "description": "", "status": "live"},
    {"folder": "01-quantum-physics/quantum-physics/lesson-05", "id": "Q5", "title": "Superposition & Collapse", "description": "", "status": "live"},
    {"folder": "01-quantum-physics/quantum-physics/lesson-06", "id": "Q6", "title": "Zero Point Field", "description": "", "status": "live"},
    {"folder": "04-symbolic-sciences/numerology/lesson-01-language-of-numbers", "id": "N1", "title": "The Language of Numbers", "description": "Vibration Encoded in Mathematics", "status": "live"},
    {"folder": "11-meditations-and-soundscapes/creating-sacred-space/lesson-01", "id": "MS1", "title": "Creating Sacred Space", "description": "The foundation of ceremonial practice", "status": "live"},
    {"folder": "11-meditations-and-soundscapes/breathwork/lesson-1", "id": "MS2", "title": "Breathwork Preparation", "description": "3 foundational techniques", "status": "live"},
    {"folder": "11-meditations-and-soundscapes/dropping into the heart", "id": "MS3", "title": "Dropping Into the Heart", "description": "Heart coherence meditation", "status": "live"},
    {"folder": "Companion/Companion.html", "id": "L1", "title": "Academy Companion", "description": "Your AI guide through the curriculum", "status": "live"},
    {"folder": "17-TheSovereignPath/lesson-01-welcome", "id": "SP1", "title": "Welcome to The Sovereign Path", "description": "VIP 1:1 Mentorship with BabaKeegs", "status": "live"},
]

created = 0
skipped = 0
for l in lessons:
    folder = l["folder"]
    if not os.path.isdir(folder):
        print(f"  SKIP (folder not found): {folder}")
        skipped += 1
        continue
    meta_path = os.path.join(folder, "meta.json")
    meta = {
        "id":          l["id"],
        "title":       l["title"],
        "description": l["description"],
        "status":      l["status"]
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"  ✓ {l['id']} → {meta_path}")
    created += 1

print(f"\nDone — {created} meta.json files created, {skipped} folders skipped.")
print("Now: git add . && git commit -m \"Auto: seed meta.json files\" && git push")