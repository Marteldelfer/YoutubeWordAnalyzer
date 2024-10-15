from pytubefix import Channel

def title_to_url(channelname : str) -> str:

    channelname = channelname.strip().replace(' ', '')

    try:
        url = f'https://www.youtube.com/@{channelname}'
        ch = Channel(url=url)
        return url
    except:
        try: 
            url = f'https://www.youtube.com/c/{channelname}'
            ch = Channel(url=url)
            return url
        except:
            raise ValueError('Could not find channel')


def save_captions(url : str, quantity : int = 300) -> None:
    channel = Channel(url)

    #Clear or create file if exists
    try:
        with open(f'./data/{channel.channel_name.replace(" ", "")}.txt', 'w') as file:
            file.write('')
    except:
        raise 'could not create file'
    
    #Get language
    lang = str(channel.videos[0].captions)[2:6]      

    for video in channel.videos[:quantity]:
        try:
            subtitles = video.captions[lang].generate_srt_captions().split('\n')
            subtitles = ' '.join(subtitles[2::4]).lower()

            with open(f'./data/{channel.channel_name.replace(" ", "")}.txt', 'a' ) as file:
                file.write(subtitles + '\n')
        except:
            print(f'could not save data from {video.title}')

if __name__ == "__main__":
    save_captions(input('Type channel url: \n>>> '))
