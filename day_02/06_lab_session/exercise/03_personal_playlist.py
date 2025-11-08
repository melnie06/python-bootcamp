def add(song, playlist):
    """TODO: Add song to playlist"""

def remove(song, playlist):
    """TODO: Remove song from playlist (if there)"""

def play(playlist):
    """TODO: Print the first song in the playlist (if any) and remove"""

def show_all(playlist):
    """TODO: Print all contents in the playlist"""

def save(playlist, filepath):
    """Challenge: TODO: Save current playlist to filepath"""

def load(filepath):
    """Challenge: TODO: Load a new playlist from filepath and return it"""

def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
        then do the task requested
    """

    playlist = []
    end = False

    while not end:
        user_choice = input("Select command: ")

        # Ask all inputs in the playlist_app() function to make functions simple
        if user_choice == "add":
            new_song = input("Enter song name: ")
            add(new_song, playlist)
        if user_choice == "exit":
            end = True

playlist_app()