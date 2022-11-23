


from youtube_transcript_api import YouTubeTranscriptApi as ytt
from pytube import YouTube as yt

import subprocess
import os


class Editor:
  def __init__(self, dist, cut, width, height):
    self.dist = dist
    self.cut = cut
    self.width = width
    self.height = height

    self.video = VideoClip(self)
    self.vf = Vf(self)

  def render(self):
    self.video.command.append(
      os.path.join(self.video.distpath, 'edited-' + self.video.filename)
    )
    print(' '.join(self.video.command))
    response = os.system(' '.join(self.video.command))



class VideoClip:
  def __init__(self, editor):
    self.prefix = 'ffmpeg'

    self.editor = editor
    self._cut = editor.cut
    self._width = editor.width
    self._height = editor.height
    self._dist = editor.dist
    self.duration = editor.cut[1]
    self.start_at = editor.cut[0]

    self.filename = os.path.basename(self._dist)
    self.distpath = os.path.join(os.getcwd(), 'dist')
    self.filepath = os.path.join(self.distpath, self.filename)

    self.command = [self.prefix, '-i', self.filepath]

    self.cut(self._cut)

  def cut(self, cut):
    self.command.insert(1, '-ss {}'.format(cut[0]))
    self.command.append('-t {}'.format(cut[1]))
    return self.command


class Vf:
  def __init__(self, editor):
    self.params = []
    self.command = []

    self.editor = editor
    self.crop(self.editor.width, self.editor.height)

  def drawtext(self, content=None, start_at=0, duration=0, shadowcolor="black", shadow_x=0, shadow_y=0, shadow_opacity=None, opacity=None, font="TitanOne-Regular", fontcolor="white", fontsize="40", text_x="(w-tw)/2", text_y="(h-th)/2"):
    if duration == 0: duration = self.editor.video.duration

    transparency = lambda x: '@{}'.format(opacity) if not x == None else ''
    between = lambda x,y: ":enable='between(t,{},{})'".format(x, y) if not x == 0 else ''

    params = [
      "drawtext=fontfile=fonts/{}.ttf".format(font),
      ':text={}'.format(content.replace('\'', '')),
      ":enable='between(t,{},{})'".format(start_at, duration),
      ':fontcolor={}'.format(fontcolor),
      transparency(opacity),
      ':fontsize={}'.format(fontsize),
      ':shadowcolor={}'.format(shadowcolor),
      transparency(shadow_opacity),
      ':shadowx={}'.format(shadow_x),
      ':shadowy={}'.format(shadow_y),
      ':x={}'.format(text_x),
      ':y={}'.format(text_y)
    ]

    if len(self.command) >= 0:
      self.command.append([*params])
      return self.command

  def crop(self, w, h, x=None, y=None):
    params = 'crop={}:{}'.format(w, h)

    if len(self.command) >= 0:
      self.command.append([params])
      return self.command

  def concatenate(self, video_command):
    vf = ['-vf']
    command = '"'
    n = 0
    for lst in self.command:
      if n == len(self.command) -1:
        command += '{}'.format(''.join(lst))
      else:
        command += '{},'.format(''.join(lst))
      n += 1

    command += '"'
    vf.append(command)
    video_command.insert(-1, ' '.join(vf))
    return video_command

  def subtitles(self, subtitles):
    video_start = self.editor.video.start_at
    video_duration = self.editor.video.duration
    video_length = (video_start+video_duration)
#    print(video_start, video_duration)
    video_subtitles = []
    start_at = 0
    for script in subtitles:
      start = script['start']
      if round(start) >= video_start and round(start) <= video_length:
        print(start, script['duration'], script['text'])
        video_subtitles.append(script)
    return video_subtitles

class Subtitles:
  def __init__(self, ext):
    self.video_id = ext.video.video_id

  def get(self):
    trans_lst = ytt.list_transcripts(self.video_id)
    transcript = trans_lst.find_generated_transcript(['en'])
    return transcript.fetch()


class Youtube:
  def __init__(self, video_url, editor):
    self.editor = editor

    self.video = yt(video_url)
    self.subtitles = Subtitles(self)

  def get_stream(self):
    video = yt(video_url)
    video = video.streams.get_highest_resolution()
    return video.url


if __name__ == "__main__":
  editor = Editor(
    dist="dist/0omEQq3N96M.mp4",
    cut=(30, 5),
    width=460,
    height=720
  )

  text_logo = editor.vf.drawtext(
    content="CREEPY DEEPY".upper(),
    fontcolor="#7a0200",
    fontsize="20",
    font='Creepster-Regular',
    opacity=0.5,
    shadow_y=2,
    text_y="(h-th)/2+80"
  )

  cat = editor.vf.concatenate(editor.video.command)
  editor.render()
