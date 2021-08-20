from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from pytube import YouTube

def valid_link(thelink):
	print(thelink)
	return YouTube(thelink)

def get_video_details(vid):
	global video_title
	global thumbnail_link
	global stream

	video_title = vid.title
	thumbnail_link = vid.thumbnail_url
	stream = vid.streams.get_by_itag(22)

	print(video_title)
	print(thumbnail_link)

"""class Video_details:

	def __init__(self,vid=yt):
		self.video_title = vid.title
		self.thumbnail_link = vid.thumbnail_url"""


class BoxLO(BoxLayout):
	download = ObjectProperty(None)
	title = ObjectProperty(None)
	url = ObjectProperty(None)
	dlInput = ObjectProperty(None)

	def checkk(self):
		video = valid_link(self.dlInput.text)
		get_video_details(video)
		self.title.text = video_title
		self.url.text = thumbnail_link
		

	def downloadd(self):
		print('Downloading')
		stream.download()
		print('Download done!')
		

class YoutubeDownloaderApp(App):
	pass

YoutubeDownloaderApp().run()