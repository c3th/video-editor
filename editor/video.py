

import os

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
    self.command.insert(1, '-ss {}'.format(self.start_at))
    self.command.append('-t {}'.format(self.duration))
    return self.command
