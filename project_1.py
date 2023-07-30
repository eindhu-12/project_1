import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.song_list = []
        self.current_song = 0
        self.paused = False

        pygame.init()

        self.song_label = tk.Label(root, text="No song selected")
        self.song_label.pack(pady=20)

        self.btn_load = tk.Button(root, text="Load Songs", command=self.load_songs)
        self.btn_load.pack(pady=5)

        self.btn_play = tk.Button(root, text="Play", command=self.play_pause)
        self.btn_play.pack(pady=5)

        self.btn_stop = tk.Button(root, text="Stop", command=self.stop)
        self.btn_stop.pack(pady=5)

    def load_songs(self):
        song_paths = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for path in song_paths:
            song = os.path.basename(path)
            self.song_list.append((path, song))
        if self.song_list:
            self.current_song = 0
            self.song_label.config(text=f"Now Playing: {self.song_list[self.current_song][1]}")

    def play_pause(self):
        if self.song_list:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                self.paused = True
                self.btn_play.config(text="Resume")
            elif self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
                self.btn_play.config(text="Pause")
            else:
                self.play_song()

    def play_song(self):
        if self.song_list:
            pygame.mixer.music.load(self.song_list[self.current_song][0])
            pygame.mixer.music.play()
            self.song_label.config(text=f"Now Playing: {self.song_list[self.current_song][1]}")

    def stop(self):
        if self.song_list:
            pygame.mixer.music.stop()
            self.song_label.config(text="Music Stopped")
            self.btn_play.config(text="Play")
            self.paused = False

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
