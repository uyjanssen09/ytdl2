from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=H4gB4nIldBo')

# video title
print("Title: " + yt.title)

# video thumbnail
print("Thumbnail: " + yt.thumbnail_url)

# video streams
#for i in yt.streams:
	#print(i)

stream = yt.streams.get_by_itag(22)
stream.download()
