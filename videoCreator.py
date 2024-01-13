import os
import glob
from natsort import natsorted
from moviepy.editor import *

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 
#UNCOMMENT ONCE FINISHED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import Script
import imageGetter


#UNCOMMENT ONCE FINISHED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
mytext, topics = imageGetter.main()
print(mytext)
print(mytext)
print(topics)
#mytext = "Hello, the top 10 dog breeds are golden retrievers, and puppies"
#topics = ['blogs', "rating"]

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 

base_dir = os.path.realpath("./simple_images/")
print(base_dir)

gif_name = 'pic'
fps = 24

file_list = glob.glob('simple_images/*.jpeg')  # Get all the pngs in the current directory
print(file_list)
for topic in topics:
    bucket = glob.glob('simple_images/' + topic.strip() +'/*jpeg')
    print('simple_images/' + topic.strip() + '/*jpeg')
    print(bucket)
    file_list.append(bucket)  
    
file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images

print(file_list)
print(file_list_sorted)

clips = [ImageClip(m).set_duration(3)
         for j in file_list_sorted
            for m in j]
print(clips)
concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=fps)

clip = VideoFileClip("test.mp4") 
  
# getting only first 5 seconds 
clip = clip.subclip() 
  
# loading audio file 
audioclip = AudioFileClip("welcome.mp3").subclip() 
  
# adding audio to the video clip 
videoclip = clip.set_audio(audioclip) 
videoclip.write_videofile("final.mp4", fps=fps) 

music = input("Is the theme of the video happy sad intresting or calm?\n")

if(music == "sad"):
    musicClip = AudioFileClip("sad.mp3").subclip(videoclip.duration)
    new_audioclip = CompositeAudioClip([videoclip.audio, musicClip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("finalMusic.mp4", fps=fps)
if(music == "happy"):
    musicClip = AudioFileClip("happy.mp3").subclip(videoclip.duration)
    new_audioclip = CompositeAudioClip([videoclip.audio, musicClip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("finalMusic.mp4", fps=fps)
if(music == "intresting"):
    musicClip = AudioFileClip("intresting.mp3").subclip(videoclip.duration)
    new_audioclip = CompositeAudioClip([videoclip.audio, musicClip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("finalMusic.mp4", fps=fps)
if(music == "calm"):
    musicClip = AudioFileClip("calm.mp3").subclip(videoclip.duration)
    new_audioclip = CompositeAudioClip([videoclip.audio, musicClip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("finalMusic.mp4", fps=fps)
else:
    pass