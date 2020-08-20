import time
from threading import Thread
from pytube import YouTube, Playlist #Dokumentation: https://python-pytube.readthedocs.io/en/latest/

# ----------------------------------------------------- einzelnes Video herunterladen ---------------------------------------------------- #
def _download_video(url, quality):
	video = YouTube(url)
	
	print("Author:", video.author)
	print("Title:", video.title)
	print("Views:", video.views)
	print("Length:", video.length)
	print("Description:", video.description)
	print("Ratings:", video.rating)
	print("Age restricted:", video.age_restricted)

	print("Start printing:")
	print(video.streams)

	'''
	stream = video.streams.get_highest_resolution()
	stream.download("out.mp4")
	'''

def download_video(*args) -> Thread:
	thread = Thread(target = _download_video, args = args)
	thread.start()
	return thread

# -------------------------------------------------------- Playlist herunterladen -------------------------------------------------------- #
def download_playlist(url, quality):
	pl = Playlist(url)
	if pl.last_update != None:
		for url in pl.video_urls:
			download_video(url, quality)

# ------------------------------------------------------- auszuführender Startcode ------------------------------------------------------- #
print("Start!")

dl = download_video("https://www.youtube.com/watch?v=WtBTqGzErn8")
dl.join()
'''
while True:
	#read
	with open("config.json") as f:
		config = f.read()


		
	#wait
	time.sleep(3)
'''