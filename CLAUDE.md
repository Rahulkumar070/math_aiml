# CLAUDE.md — Project Instructions

This file tells Claude Code how to work in this repository. Read it first.

## What this project is

This repo is **Rahul's hands-on journey learning AI/ML from scratch**, built in
public on GitHub. It doubles as a learning record and a portfolio. The repo
grows over time: each topic is a numbered folder containing small, runnable
projects, committed and pushed as they're finished.

GitHub: https://github.com/Rahulkumar070/math_aiml

## Who the user is

- **New to coding** — explain everything in plain language, no unexplained jargon.
- **Project-first learner** — teach by building small runnable programs, not walls of theory.
- **Has lots of time** (~10+ hrs/week) and is motivated. Moves quickly.
- Goal: learn AI/ML AND build a visible GitHub portfolio at the same time.

## How to teach (important)

1. **One concept at a time.** Introduce it, then show it in a small script.
2. **Comment every script heavily** — write comments as if teaching a beginner.
   Each lesson file should be understandable on its own by reading top to bottom.
3. **Always run the code** after writing it, and show/explain the output.
4. **Recap the key takeaways** in a few bullet points after each lesson.
5. **Give a small "your turn" challenge** so the user practices actively.
6. Be honest about scope, timelines, and what's "enough vs. nice-to-have".
7. Keep momentum: after each lesson, commit and push, then offer the next step.

## The workflow rhythm (repeat for every lesson/project)

Learn a concept → build a tiny script → run it → explain output → commit → push.

```bash
cd "/Users/rahul/Desktop/Math Aiml"
git add .
git commit -m "clear message describing what was learned/built"
git push
```

## Repo structure & conventions

```
Math Aiml/
├── CLAUDE.md            ← this file
├── README.md            ← roadmap + progress tracker (keep checkboxes updated)
├── .gitignore
├── requirements.txt     ← libraries (numpy, pandas, matplotlib, scikit-learn)
├── 00-python-basics/    ← lessons 01..10 (DONE)
├── 01-numpy/            ← (next)
├── 02-pandas/
└── ...
```

- Topic folders are numbered: `00-`, `01-`, `02-`, ...
- Lesson files inside are numbered with a short name: `03_math_operators.py`.
- When a roadmap step is complete, tick its checkbox in `README.md`.

## Roadmap & progress

- [x] 00 — Python basics (lessons 01–10 complete: hello, variables, math,
      input, conditionals, loops, lists/dicts, functions, strings/f-strings,
      list comprehensions)
- [ ] 01 — NumPy (arrays, the math behind ML)
- [ ] 02 — Pandas (loading and exploring real data)
- [ ] 03 — First ML model (scikit-learn classifier)
- [ ] 04 — Train & evaluate (train/test split, accuracy, plots)
- [ ] 05 — End-to-end mini-project

## Environment

- **Python 3.14** (brand new — if a library fails to install, find a workaround).
- Git configured as: Rahul Pal / rk035199@gmail.com
- No `gh` CLI installed — GitHub repos are created on the website; push over HTTPS.
- Virtual environment: `.venv` (create with `python3 -m venv .venv`, activate with
  `source .venv/bin/activate`, install with `pip install -r requirements.txt`).
  Not yet created as of the last session — set it up before Step 01 (NumPy).

## Conventions for commit messages

Short, descriptive, present tense. Examples:
- "Add Python basics lesson: loops"
- "Add NumPy lesson: creating and reshaping arrays"
- "Mark Python basics (step 00) complete in roadmap"
