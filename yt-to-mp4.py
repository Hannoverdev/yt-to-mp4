from pytube import YouTube

link = input("Introduce el enlace que deseas descargar")
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()

print("iniciando Descarga")
stream.download()
print("Descarga completada")
