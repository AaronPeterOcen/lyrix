import requests
from bs4 import BeautifulSoup

def fetch_lyrics(song_name, artist_name):
    # Format the song and artist name for URL
    song_name = song_name.replace(" ", "+")
    artist_name = artist_name.replace(" ", "+")
    
    search_url = f"https://search.azlyrics.com/search.php?q={song_name}+{artist_name}"
    print(f"Searching for: {search_url}")  # Debugging line
    
    # Send a GET request to AZLyrics search page
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the response HTML for debugging
    print(soup.prettify())  # Debugging line
    
    # Find the first song result and extract its URL
    song_link = soup.find('a', href=True)
    if song_link:
        lyrics_page_url = f"https:{song_link['href']}"
        
        # Fetch the lyrics page
        response = requests.get(lyrics_page_url)
        lyrics_soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract lyrics
        divs = lyrics_soup.find_all('div')
        for div in divs:
            if div.attrs == {}:
                lyrics = div.get_text(separator="\n").strip()
                return lyrics
    return None

def save_lyrics_to_file(lyrics, song_name, artist_name):
    if lyrics:
        filename = f"{artist_name}_{song_name}.txt"
        with open(filename, 'w') as file:
            file.write(lyrics)
        print(f"Lyrics saved to {filename}")
    else:
        print("Lyrics not found!")

if __name__ == "__main__":
    # Input from the user
    song_name = input("Enter the song name: ")
    artist_name = input("Enter the artist name: ")
    
    lyrics = fetch_lyrics(song_name, artist_name)
    save_lyrics_to_file(lyrics, song_name, artist_name)
