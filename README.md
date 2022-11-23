## 🎥 Video Editor (Made Easy)
> A fully working one-file video editor, originally made for the purpose to automate short videos.

## 🔧 Cloning
```
$ git clone https://github.com/c3th/video-editor
$ cd video-editor
```

## ⚙ Usage
### Importing video
```py
ed = Editor(
  dist='path/to/video.mp4',
  cut=(30, 5),
  width=460,
  height=720
)

# ...
```
Name   | Type   | Description
-------|--------|---------------------------------------------------
dist   | String | Specify the video path, only tested with MP4
cut    | List   | Skip 30 seconds, then cuts 5 seconds video footage
width  | Number | Specify video width
height | Number | Specify video height

### Adding text to video
```py
text_logo = ed.vf.drawtext(
  content="Spoopy".upper(),
  fontcolor="#7a0200",
  fontsize=25,
  font="Creepster-Regular",
  opacity=0.5,
  shadow_y=2,
  text_y="(h-th)/2+80"
)

# ...
```
Name   | Type   | Description
-------|--------|---------------------------------------------------
