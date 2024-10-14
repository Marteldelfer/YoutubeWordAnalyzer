from pytubefix import Channel

def save_captions(url) -> None:
    channel = Channel(url)

    #Clear or create file if exists
    try:
        with open(f'./data/{channel.channel_name.replace(" ", "")}.txt', 'w') as file:
            file.write('')
    except:
        raise 'could not create file'
        

    for video in channel.videos:
        try:
            subtitles = video.captions['a.pt'].generate_srt_captions().split('\n')
            subtitles = ' '.join(subtitles[2::4]).lower()

            with open(f'./data/{channel.channel_name.replace(" ", "")}.txt', 'a' ) as file:
                file.write(subtitles + '\n')
        except:
            print(f'could not save data from {video.title}')

if __name__ == "__main__":
    save_captions('https://www.youtube.com/c/CursoemV%C3%ADdeo')