def add(song, playlist):
    """Add song to playlist"""
    playlist.append(song)


def remove(song, playlist):
    """Remove song from playlist (if there)"""
    if song in playlist:
        playlist.remove(song)
    else:
        print(f"'{song}' not in playlist.")


def play(playlist):
    """Print the first song in the playlist (if any) and remove"""
    if playlist:
        song = playlist.pop(0)
        print(f"Now playing: {song}")
    else:
        print("Playlist is empty.")


def show_all(playlist):
    """Print all contents in the playlist"""
    if playlist:
        print("Playlist:")
        for index, song in enumerate(playlist, 1):
            print(f"{index}. {song}")
    else:
        print("Playlist is empty.")


def save(playlist, filepath):
    """Save current playlist to filepath"""
    try:
        with open(filepath, 'w') as f:
            for song in playlist:
                f.write(song + '\n')
        print(f"Playlist saved to {filepath}")
    except Exception as e:
        print(f"Error saving playlist: {e}")


def load(filepath):
    """Load a new playlist from filepath and return it"""
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []


def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
    then do the task requested
    """
    playlist = []
    while True:
        print("\nCommands: add, remove, play, show, save, load, quit")
        user_choice = input("Select command: ").strip().lower()

        if user_choice == "add":
            new_song = input("Enter song name: ").strip()
            add(new_song, playlist)

        elif user_choice == "remove":
            song = input("Enter song name to remove: ").strip()
            remove(song, playlist)

        elif user_choice == "play":
            play(playlist)

        elif user_choice == "show":
            show_all(playlist)

        elif user_choice == "save":
            filepath = input("Enter filename to save to: ").strip()
            save(playlist, filepath)

        elif user_choice == "load":
            filepath = input("Enter filename to load from: ").strip()
            playlist = load(filepath)

        elif user_choice == "quit":
            print("Exiting playlist app...")
            break

        else:
            print("Invalid command. Try again.")


# Run the app
playlist_app()
