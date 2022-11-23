

class Vf:
  def __init__(self, editor):
    self.params = []
    self.command = []

    self.editor = editor
    self.crop(self.editor.width, self.editor.height)

  def drawtext(self, content=None, start_at=0, duration=0, shadowcolor="black", shadow_x=0, shadow_y=0, shadow_opacity=None, opacity=None, font="TitanOne-Regular", fontcolor="white", fontsize=40, text_x="(w-tw)/2", text_y="(h-th)/2"):
    if duration == 0: duration = self.editor.video.duration

    transparency = lambda x: '@{}'.format(opacity) if not x == None else ''
    params = [
      "drawtext=fontfile=fonts/{}.ttf".format(font),
      ":text={}".format(content),
      ":enable='between(t,{},{})'".format(start_at, duration),
      ":fontcolor={}".format(fontcolor),
      transparency(opacity),
      ":fontsize={}".format(fontsize),
      ":shadowcolor={}".format(shadowcolor),
      transparency(shadow_opacity),
      ":shadowx={}".format(shadow_x),
      ":shadowy={}".format(shadow_y),
      ":x={}".format(text_x),
      ":y={}".format(text_y),
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
    video_length = (video_start + video_duration)
    video_subtitles = []
    start_at = 0
    for script in subtitles:
      start = script['start']
      if round(start) >= video_start and round(start) <= video_length:
#        print(start, script['duration'], script['text'])
        video_subtitles.append(script)
    return video_subtitles
