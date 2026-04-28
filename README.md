# End-of-Day Reflection Tool

This project implements a deterministic reflection system that helps employees reflect on their workday through a structured conversation.

The tool asks fixed-option questions and guides the user through three psychological axes:

1. **Locus (Victim vs Victor)** – recognizing personal agency in events.
2. **Orientation (Contribution vs Entitlement)** – focusing on contribution versus expectations.
3. **Radius (Self vs Others)** – considering how actions affect teammates and customers.

The reflection process is implemented as a **decision tree stored in JSON**, and executed by a Python program.

---

## Project Structure

reflection_project
│
├── main.py  
├── reflection_tree.json  
├── writeup.md  
└── README.md

---

## How to Run

Run the program using:

python main.py

The reflection session will start in the terminal.

---

## Key Features

- Deterministic decision tree
- Fixed answer options
- Branching reflections
- No AI or LLM used at runtime

---

Author:  
Aniket Kumar  
B.Tech – AI & ML