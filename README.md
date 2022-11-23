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
Name      | Type   | Description
----------|--------|---------------------------------------------------
content   | String | Text to be displayed
fontcolor | String | Color of text
fontsize  | Number | Size of text
font      | String | Change font of text
opacity   | Number | Opacity of text, 0.5 is 50%, 1 is 100%
shadow_y  | Wild   | While you could use numbers, FFmpeg allows you to use built-in variables, see [here]()
text_y    | Wild   | -- | --

### Positions
Position      | x:y                | With 10 px padding
--------------|-------------------------------|--------------------------------------------
Top left      | x=0:y=0                       | x=10:y=10
Top center    | x=(w-text_w)/2:y=0            | x=(w-text_w)/2:y=10
Top right	    | x=w-tw:y=0                    | x=w-tw-10:y=10
Centered	    | x=(w-text_w)/2:y=(h-text_h)/2 |
Bottom left	  | x=0:y=h-th	                  | x=10:y=h-th-10
Bottom center	| x=(w-text_w)/2:y=h-th         | x=(w-text_w)/2:y=h-th-10
Bottom right  | x=w-tw:y=h-th                 | x=w-tw-10:y=h-th-10

> Positions table taken from [here](https://stackoverflow.com/questions/17623676/text-on-video-ffmpeg)

## 🔈 Subtitles
> Subtitles is still in development, but if you'd like to download a transcript from a Youtube video, you can!

```py
tube = Youtube(
  video_url="https://www.youtube.com/watch?v=0omEQq3N96M",
  editor=ed
)

transcript = tube.subtitles.get()
print(transcript)

# ...
```

## 🎈 Todo (Self notes)
* [ ] Combine audio file with video
* [ ] Get transcript to automatically apply itself to video as voices go
* [ ] Add images to video
* [ ] Combine two video into one only changing Y positions
* [ ] ...
