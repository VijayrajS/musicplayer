'''
Main interface for any song object
'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import time as pytime
from pygame import mixer as pymixer

from tinytag import TinyTag as tag_importer

# tag.album         # album as string
# tag.albumartist   # album artist as string
# tag.artist        # artist name as string
# tag.audio_offset  # number of bytes before audio data begins
# tag.bitrate       # bitrate in kBits/s
# tag.comment       # file comment as string
# tag.composer      # composer as string 
# tag.disc          # disc number
# tag.disc_total    # the total number of discs
# tag.duration      # duration of the song in seconds
# tag.filesize      # file size in bytes
# tag.genre         # genre as string
# tag.samplerate    # samples per second
# tag.title         # title of the song
# tag.track         # track number as string
# tag.track_total   # total number of tracks as string
# tag.year          # year or data as string

class AudioObj:
    def __init__(self, SONG_PATH):

        self.time_pt = 0
        self.song_path = SONG_PATH
        self.metadata, self.img  = self.load_meta()
    
    def load_song(self):
        pass

    def load_meta(self):
        if tag_importer.is_supported(self.song_path):
            song_tag = tag_importer.get(self.song_path, image=True)
            return song_tag, song_tag.get_image()
        else:
            print('Error: file format not supported')

    def play_song(self):
        pass
    
    def seek(self, time):
        pass

class MP3Obj(AudioObj):
    def __init__(self, SONG_PATH):
        super().__init__(SONG_PATH)
        self.load_song()

    def load_song(self):
        pymixer.init(44100, -16, 1, 1024)
        pymixer.music.load(self.song_path)

    def play_song(self):
        pymixer.music.play()
        while pymixer.music.get_busy():
            pytime.Clock().tick(10)

    def seek(self, time):
        pass

a = MP3Obj('/home/vijayraj/Desktop/Music/CrossOff.mp3')
print(a.metadata)
a.load_song()
a.play_song()
