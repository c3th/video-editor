

from editor import Editor

if __name__ == "__main__":
  editor = Editor(
    dist="dist/0omEQq3N96M.mp4",
    cut=(30, 5),
    width=460,
    height=720
  )

  text_logo = editor.vf.drawtext(
    content="Spoopy".upper(),
    fontcolor="#7a0200",
    fontsize="20",
    font='Creepster-Regular',
    opacity=0.5,
    shadow_y=2,
    text_y="(h-th)/2+80"
  )

  cat = editor.vf.concatenate(editor.video.command)
  editor.render()
