import lyricsgenius

# Replace with your actual Genius API key
GENIUS_API_KEY = 'your_genius_api_key'

# Create a Genius object
genius = lyricsgenius.Genius(GENIUS_API_KEY)

def fetch_lyrics(song_name, artist_name):
    try:
        song = genius.search_song(song_name, artist_name)
        if song:
            return song.lyrics
        else:
            return "Lyrics not found!"
    except Exception as e:
        return f"An error occurred: {e}"

def save_lyrics_to_file(lyrics, song_name):
    file_name = f"{song_name.replace(' ', '_')}_lyrics.txt"
    with open(file_name, 'w') as f:
        f.write(lyrics)
    print(f"Lyrics saved to {file_name}")

if __name__ == "__main__":
    song_name = input("Enter the song name: ")
    artist_name = input("Enter the artist name: ")

    lyrics = fetch_lyrics(song_name, artist_name)
    print(lyrics)

    if lyrics != "Lyrics not found!":
        save_lyrics_to_file(lyrics, song_name)
