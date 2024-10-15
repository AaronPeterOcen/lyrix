# lyrix

This is a simple Python script that fetches song lyrics using the Genius API and saves them to a text file.

## Features

- Search for song lyrics by song name and artist.
- Save lyrics to a text file in the current directory.

## Prerequisites

Before you can use the script, make sure you have the following installed:

- Python 3.7 or higher
- A [Genius API key](https://genius.com/developers)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/lyrics-fetcher.git
cd lyrics-fetcher
```

## 2. Create a Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use myenv\Scripts\activate
```

## 3. Install the Required Python Package

```bash
pip install lyricsgenius
```

## Usage

1. Set your Genius API key in the script:

   Open main.py and replace 'your_genius_api_key_here' with your actual API key.

2. Run the script:

```bash

python main.py
```

3. Enter the song name and artist name when prompted.

4. If the lyrics are found, they will be saved as a text file in the current directory.

## Example

```bash
python main.py
Enter the song name: Lean On
Enter the artist name: Major Lazer

Lyrics saved to Lean_On_lyrics.txt
```

## Troubleshooting

If the script doesn't find the lyrics, make sure the song and artist names are spelled correctly.
Check your Genius API key if you encounter an authentication error.
