
# Get the current date and time in the São Paulo timezone
now = datetime.datetime.now(tz)
tempo = now.strftime('%m%d_%H%M%S')
tempo2 = now.strftime('-%Y')
filename = "BB" + tempo + tempo2 + ".ts"

[cli][info] Found matching plugin youtube for URL https://www.youtube.com/@TelemundoEntretenimiento/live
[cli][info] Available streams: 144p (worst), 240p, 360p, 480p, 720p, 1080p (best)
[cli][info] Opening stream: 1080p (hls)
error: The default player (VLC) does not seem to be installed. You must specify the path to a player executable with --player, a file path to save the stream with --output, or pipe the stream to another program with --stdout.


EOL 
