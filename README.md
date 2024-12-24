# Counter Card: Hi-Lo Counting System

## Overview

The Counter Card is a Python-based application designed to help users practice and understand the Hi-Lo card counting system commonly used in Blackjack. The program features a graphical interface where users can track card counts, simulate a game deck, and evaluate the probabilities for strategic decisions.

---

## Features

- Graphical user interface (GUI) for simulating card counting.
- Real-time updates on the Hi-Lo count and true count.
- Visual indicators (color signals) to represent the current game situation:
  - **Red**: Negative count (unfavorable situation).
  - **Yellow**: Neutral count (balanced situation).
  - **Blue**: Positive count (favorable situation).
- Buttons representing all cards, grouped logically for easy interaction.
- Displays the number of remaining cards in the deck for accurate tracking.

---

## Prerequisites

Ensure you have Python installed on your system (version 3.6 or higher).

### Required Libraries

- `tkinter`
- `messagebox` (part of `tkinter`)

These libraries come pre-installed with Python. No additional installations are necessary.

---

## How to Run

1. Clone the repository or download the `CountCard.py` file.

2. Open a terminal and navigate to the directory containing the file.

3. Run the following command:

   ```bash
   python CountCard.py
   ```

4. The graphical interface will open, displaying the card buttons and count details.

---

## How It Works

### Card Values

The Hi-Lo system assigns the following values to cards:

- **+1**: Cards 2, 3, 4, 5, 6
- **0**: Cards 7, 8, 9
- **-1**: Cards 10, J, Q, K, A

### Steps:

1. When you click a card, the program updates the count based on the Hi-Lo value of that card.
2. The true count is calculated by dividing the running count by the number of decks remaining.
3. Color signals provide a visual cue:
   - **Red**: Count < 0 (unfavorable).
   - **Yellow**: Count between 0 and 6 (neutral).
   - **Blue**: Count > 6 (favorable).
4. The interface also shows the number of cards left in the deck.

---

## File Structure

- `CountCard.py`: Main script containing the application logic and GUI.

---

## Tips for Card Counting

- Practice counting with a single deck before moving to multiple decks.
- Familiarize yourself with the Hi-Lo system to improve speed and accuracy.
- Remember, card counting provides an edge but does not guarantee a win.

---

## Disclaimer

This program is for educational purposes only. Card counting is prohibited in many casinos, and misuse of this tool is at your own risk.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it.

