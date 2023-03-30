from ffmpeg_streaming import FFProbe
import os

ffprobe = FFProbe('video.mp4')
current_dir = os.path.dirname(os.path.abspath(__file__))
ffprobe.save_as_json(os.path.join(current_dir, 'probe.json'))

all_media = ffprobe.all()

video_format = ffprobe.format()

streams = ffprobe.streams().all()
videos = ffprobe.streams().videos()
audios = ffprobe.streams().audios()

first_stream = ffprobe.streams().first_stream()
first_video = ffprobe.streams().video()
first_audio = ffprobe.streams().audio()

print("all:")
print(all_media)

print("format:")
print(video_format)

print("streams:")
print(streams[0]['coded_height'])
print(streams[0]['coded_width'])