


from youtube_transcript_api import YouTubeTranscriptApi as ytt
from pytube import YouTube

from moviepy.editor import *
from moviepy.video.fx.all import crop

from io import BytesIO

import requests
import os



class Creator:
  def __init__(self, video_url):
    self.dist_path = os.path.join(os.getcwd(), 'dist')
    self.build_path = os.path.join(os.getcwd(), 'build')

    self.video = YouTube(video_url)
    self.transcript = Transcript(self)
#    self.editor = Editor(self)

  def video_stream(self):
    video = self.video.streams.get_highest_resolution()
    return video.url

  def save_to_dist(self, video_stream, filename=None):
    if not filename:
      filename = self.video.title + '.mp4'

    self.dist_path = os.path.join(self.dist_path, filename)
    with open(self.dist_path, 'wb') as f:
      f.write(video_stream)

  def download(self):
    video_stream = self.video_stream()
    video_stream = requests.get(video_stream)
    self.save_to_dist(video_stream.content, f'{self.video.video_id}.mp4')


class Transcript:
  def __init__(self, base):
    self.video = base.video
    self.dist_path = base.dist_path

  def save(self, transcript=None):
    filename = f'{self.video.title}.transcript.txt'
    f = open(os.path.join(self.dist_path, filename), 'a')
    for line in list(transcript):
      f.write(line['text'] + '\r')

  def get(self):
    video_id = self.video.video_id
    transcript_list = ytt.list_transcripts(video_id)
    transcript = transcript_list.find_generated_transcript(['en'])
    return transcript.fetch()


class Editor:
  def __init__(self, ext):
    dist = os.listdir(ext.dist_path)
    video_path = None
    for tmp in dist:
      if tmp.endswith('.mp4') and not tmp.startswith('cropped-'):
        video_path = os.path.join(ext.dist_path, tmp)
        file = tmp

    v_w, v_h = 460, 720
    v_x, v_y = v_w / 2 + (1 * 200), v_h

    clip = VideoFileClip(video_path).subclip(3, 6)
    clip = crop(clip, x1=v_x, x2=v_y, width=v_w, height=v_h)

    video = CompositeVideoClip([clip])
    video.write_videofile(
      os.path.join(ext.dist_path, f'cropped-{file}')
    )

if __name__ == "__main__":
  creator = Creator(
    'https://www.youtube.com/watch?v=0omEQq3N96M&ab_channel=PowerfulJRE'
  )

  script = creator.transcript.get()

  print(script)

#  creator.transcript.save(script)

#  transcript = creator.transcript.get()
#  creator.transcript.save(transcript)
