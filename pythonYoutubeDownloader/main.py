from pytube import YouTube


def downloading_video_from_youtube(url):
    yt = YouTube(url)
    quality = yt.streams.get_highest_resolution().download("C:\\Users\Hp\Desktop")


def downloading_audio_from_youtube(url):
    yt = YouTube(url)
    quality = yt.streams.get_audio_only().download("C:\\Users\Hp\Desktop")


print("Welcome To Youtube Downloader,\nEnter \"v\" For Video or \"a\" For Audio")
v_or_a = input("\"v\" or \"a\" : ")
link = str(input("Enter The Youtube URL : "))
if v_or_a == 'v':
    downloading_video_from_youtube(link)
elif v_or_a == 'a':
    downloading_audio_from_youtube(link)
else:
    print("Invalid input, Try again")

print("Downloaded Successfully !!")
input()
