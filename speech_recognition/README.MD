# Speech to Text Using OPENAI Whisper
Simple speech to text using [OpenAI Whisper](https://github.com/openai/whisper) in Python. Uses Whisper to transcribe audio file and writes it to text file.
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
git clone https://github.com/jamesyoung-15/python-practice
cd ./python-practice/speech_recognition
python audio_transcript.py
```
Then script will prompt some inputs:
``` bash
Enter file name: # enter the full audio file name including file extension, eg. test.mp3
Enter output name: # enter the output name, example test.txt
```

## Notes
Currently using base as training model since it is fast. Seems base and small are good for speed and okay accuracy. Other models:



|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

Refer to: https://github.com/openai/whisper