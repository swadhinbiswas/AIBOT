from moviepy.editor import VideoFileClip
import os 

def video_to_gif(nameoffile):
  """Arguments:
  This function converts a video file to a gif file.
  nameoffile: str: The name of the video file to be converted to a gif file.
  return: str: The path to the gif file.
  
  """
  writeloc = os.path.join(os.path.dirname(__file__), "videos")
  clip = VideoFileClip(nameoffile)
  
  clip.write_gif(f"{writeloc}/output.gif")
  return f"{writeloc}/output.gif"


