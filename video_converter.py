import moviepy.editor

from tkinter.filedialog import *

video = askopenfilename()
clip = moviepy.editor.VideoFileClip(video)

audio=clip.audio
audio.write_audiofile("converted.mp3")

print('    ______END_____')