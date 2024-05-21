# Bob_Raoul

Bob_Raoul is a simple project designed to track the number of beer caps tossed into a receptacle named Bob. This project utilizes a static background image named `bobbg.png` and displays the cap count in the middle of the screen using Tkinter. The cap count is stored in a file named `caps.txt`, and sound effects are played from the "sounds" directory.

## Project Overview

### Concept

Bob_Raoul is a digital adaptation of the traditional Raoul concept, where a receptacle is used to collect beer caps. This project aims to provide a digital version of this experience, allowing users to keep track of the number of caps thrown into Bob.

### Features

- **Static Background**: The project utilizes a single static background image named `bobbg.png`.
- **Cap Counter**: The cap count is displayed in the middle of the screen in a large font size.
- **Sound Effects**: Sound effects are played from the "sounds" directory to provide audio feedback.
- **Cap Storage**: The total number of caps thrown into Bob is stored in a file named `caps.txt`.

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins and a screen output)
- Infrared sensor
- Plastic mannequin (Bob)
- Screen (connected to the Raspberry Pi)
- Beer caps

## Software Requirements

- Python 3
  - Tkinter (included in standard Python distribution)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/adavid1/Bob_Raoul.git
   cd Bob_Raoul
   ```
2. **Install Dependencies**
	```sh
   pip install -r requirements.txt
   ```
3. **Setup the Hardware**
* Place the infrared sensor inside Bob's head.
* Connect the sensor to the Raspberry Pi GPIO pins.
* Connect the screen to the Raspberry Pi.

4. **Run the Program**
	```sh
   python bob.py
   ```

## Usage

- Run the bob.py script.
- Toss a beer cap into Bob.
- The cap count displayed on the screen will increment accordingly.
- Sound effects from the "sounds" directory provide additional feedback.

## Directory Structure

```
Bob_Raoul/
├── bob.py
├── caps.txt
├── sounds/
│   └── [various sound files]
├── bobbg.png
└── README.md
```

## Contribution

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.


## Acknowledgements

- UTBM for the inspiration of the Raoul concept.
- The Hatry-poté for the incredible colocation experience and support during the development of this project.
- Fice, Tumleu, Hackerman, DuQ, érosse, Kyrie, Nital, Marie, Lag, and all the other testers/players (apologies if anyone was missed) for their valuable feedback and contributions.
