<div align="center">

# 🐍 Python Projects

**33 hands-on projects built on my Python learning journey — Days 2 → 33**

_From command-line games and OOP, through Turtle graphics and Tkinter GUIs, to live REST APIs and data with pandas._

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-33-success)
![Last commit](https://img.shields.io/github/last-commit/youssefelshahaawy/python-projects)

</div>

---

## 📖 About

This repository is a collection of the Python projects I've built while learning the language — **33 projects so far**, each organized into its own folder by the day it was completed. They start with small command-line scripts and grow into object-oriented games, desktop GUI apps, and tools that talk to live web APIs. Every project is self-contained and can be run on its own.

## 🗂️ Projects

| Day | Project | What it does | Key concepts |
|:---:|---------|--------------|--------------|
| 02 | [Love Calculator](./Day_02_Love_Calculator) | Calculates a fun compatibility score from two names | Strings, `.count()`, operators |
| 03 | [Treasure Island](./Day_03_Treasure_Island) | Branching text-adventure game | `if` / `elif` / `else` |
| 04 | [Rock Paper Scissors](./Day_04_Rock_Paper_Scissors) | Play RPS against the computer | Lists, `random`, indexing |
| 05 | [Password Generator](./Day_05_Password_Generator) | Generates strong random passwords | Loops, `random` |
| 06 | [Reeborg's Hurdles](./Day_06_Reeborg_Hurdles) | Logic to clear hurdles in a maze | Functions, `while`, conditionals |
| 07 | [Hangman](./Day_07_Hangman) | Word-guessing game with ASCII art stages | Lists, loops, modules |
| 08 | [Caesar Cipher](./Day_08_Caesar_Cipher) | Encrypt & decrypt text by shifting letters | Functions, modulo |
| 09 | [Secret Auction](./Day_09_Secret_Auction) | Finds the highest secret bidder | Dictionaries |
| 10 | [Calculator](./Day_10_Calculator) | Chained arithmetic with operator functions | Functions as values, dicts |
| 11 | [Blackjack](./Day_11_Blackjack) | Full Blackjack card game vs. the dealer | Lists, `random`, logic |
| 12 | [Number Guessing](./Day_12_Number_Guessing) | Guess the secret number within limited tries | Scope, loops |
| 13 | [Debugging](./Day_13_Debugging) | Classic debugging exercises & fixes | Debugging techniques |
| 14 | [Higher Lower](./Day_14_Higher_Lower) | Guess which account has more followers | Dicts, modules, game loop |
| 15 | [Coffee Machine](./Day_15_Coffee_Machine) | Procedural coffee machine with coins & stock | Dicts, functions, flow |
| 16 | [OOP Coffee Machine](./Day_16_OOP_Coffee_Machine) | The coffee machine rebuilt with classes | OOP, classes, modules |
| 17 | [Quiz Game](./Day_17_Quiz_Game) | True/False quiz engine | OOP, classes |
| 18 | [Hirst Painting](./Day_18_Hirst_Painting) | Generates a Hirst-style dot painting | `turtle`, `colorgram` |
| 19 | [Turtle Race](./Day_19_Turtle_Race) | Bet on a colourful turtle race | `turtle`, events, `random` |
| 20–21 | [Snake Game](./Day_20-21_Snake_Game) | Classic Snake with score & high score | OOP, `turtle`, inheritance |
| 22 | [Pong](./Day_22_Pong) | Two-player Pong arcade game | OOP, `turtle`, collisions |
| 23 | [Turtle Crossing](./Day_23_Turtle_Crossing) | Frogger-style road-crossing game | OOP, `turtle`, levels |
| 24 | [Mail Merge](./Day_24_Mail_Merge) | Fills a letter template for many names | Files & paths, `open()` |
| 25 | [US States Game](./Day_25_US_States_Game) | Name all 50 states on an interactive map | `pandas`, CSV, `turtle` |
| 26 | [NATO Alphabet](./Day_26_NATO_Alphabet) | Convert words to the NATO phonetic alphabet | Comprehensions, `pandas` |
| 27 | [Tkinter Basics](./Day_27_Tkinter_Basics) | Miles→Km converter & widget playground | `tkinter`, GUI events |
| 28 | [Pomodoro Timer](./Day_28_Pomodoro_Timer) | Pomodoro work/break productivity timer | `tkinter`, `after()`, math |
| 29–30 | [Password Manager](./Day_29-30_Password_Manager) | Save, search & generate passwords (GUI) | `tkinter`, `json`, exceptions |
| 31 | [Flash Cards](./Day_31_Flash_Cards) | French → English flash-card learner | `tkinter`, `pandas` |
| 32 | [Birthday Wisher](./Day_32_Birthday_Wisher) | Auto-emails birthday wishes from a CSV | `smtplib`, `datetime`, `pandas` |
| 33 | [ISS Overhead](./Day_33_ISS_Overhead) | Emails you when the ISS flies over at night | REST APIs, `requests` |
| 33 | [Kanye Quotes](./Day_33_Kanye_Quotes) | GUI that fetches a random Kanye quote | REST APIs, `requests`, `tkinter` |

> 💡 Some days include a `practice/` subfolder containing the smaller lesson exercises that led up to that day's main project.

## 🧠 Topics & Skills

- **Python fundamentals** — variables, data types, loops, conditionals, functions, scope
- **Data structures** — lists, dictionaries, tuples, list/dict comprehensions
- **Object-Oriented Programming** — classes, inheritance, encapsulation, multiple modules
- **Graphics & games** — the `turtle` module (Snake, Pong, Turtle Crossing)
- **Desktop GUIs** — `tkinter` (Pomodoro, Password Manager, Flash Cards)
- **Working with data** — `pandas`, CSV files, reading & writing the file system
- **Web & automation** — `requests`, REST APIs, `smtplib` email automation
- **Good habits** — exception handling, keeping secrets in environment variables

## 🛠️ Tech Stack

**Language:** Python 3

**Standard library:** `turtle` · `tkinter` · `smtplib` · `datetime` · `json` · `csv` · `random` · `math`

**Third-party:** `requests` · `pandas` · `prettytable` · `colorgram.py` — see [`requirements.txt`](./requirements.txt)

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/youssefelshahaawy/python-projects.git
cd python-projects

# 2. (Optional) create & activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run any project
python Day_11_Blackjack/Blackjack.py
```

### 📧 Email projects (Days 32 & 33)

The **Birthday Wisher** and **ISS Overhead** projects send email, so they read credentials from environment variables rather than hard-coding them. Copy [`.env.example`](./.env.example), fill in your details, and set these variables in your shell (for Gmail, use a 16-character **App Password**):

```
SENDER_EMAIL · SENDER_PASSWORD · RECIPIENT_EMAIL
```

## 📁 Repository Structure

```
python-projects/
├── Day_02_Love_Calculator/
├── Day_03_Treasure_Island/
├── ...
├── Day_33_ISS_Overhead/
├── Day_33_Kanye_Quotes/
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

## 🙏 Acknowledgements

These projects are based on the **_100 Days of Code_ Python course** by **Dr. Angela Yu (The App Brewery)**. The implementations in this repository are my own work.

## 📜 License

Released under the [MIT License](./LICENSE).

---

<div align="center">

⭐ _If you find this useful, a star is always appreciated!_

</div>
