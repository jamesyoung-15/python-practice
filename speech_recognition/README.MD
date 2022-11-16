# Speech to Text Using OPENAI Whisper
Simple speech to text using [OpenAI Whisper](https://github.com/openai/whisper).
## Installation and Usage
### Preqs:
- OpenAI Whisper
- FFMPEG
``` bash
pip install git+https://github.com/openai/whisper.git
# on Arch Linux
sudo pacman -S ffmpeg 
```
### Useful FFMPEG commands:
MP4 to MP3:

`ffmpeg -i video.mp4 sound.mp3`

Trimming:

`ffmpeg -i input_video -ss start_seconds -to end_seconds output.mp3`

Using this script:
``` bash
git clone thisrep
cd thisrepo
python thisrepo
```
Then enter input from audio files you want to transcript.