

import os

from .video import VideoClip
from .vf import Vf

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
