from collections import defaultdict
import pandas as pd
import wordReader as wr

def compare(channel_name1 : str, channel_name2 : str):

    try:
        with open(f'./data/{channel_name1}.txt', 'r') as file:
            print('File founded!!!')
    except:
        print('Could not find data... \nDownloading captions...')
        try:
            url = wr.title_to_url(channel_name1)
            wr.save_captions(url)
        except:
            raise ValueError('Could save captions')
    
    #Again for channel 2
    try:
        with open(f'./data/{channel_name2}.txt', 'r') as file:
            print('File founded!!!')
    except:
        print('Could not find data... \nDownloading captions...')
        try:
            url = wr.title_to_url(channel_name2)
            wr.save_captions(url)
        except:
            raise ValueError('Could save captions')

    with open(f'./data/{channel_name1}.txt', 'r') as file:
        
        text = file.read().replace('\n', '').split(' ')
        words = defaultdict(int)

        for word in text:
            words[word] += 1

    sr = pd.Series(words, name = f"{channel_name1}").sort_values(ascending=False)
    df = pd.DataFrame(sr)
    df[f'{channel_name1}Ratios'] = df[f'{channel_name1}'] / (df[f'{channel_name1}'].sum())

    with open(f'./data/{channel_name2}.txt', 'r') as file:

        text = file.read().replace('\n', '').split(' ')
        words = defaultdict(int)

        for word in text:
            words[word] += 1

    sr = pd.Series(words, name = f"{channel_name2}").sort_values(ascending=False)
    df[f'{channel_name2}'] = sr
    df[f'{channel_name2}Ratios'] = df[f'{channel_name2}'] / df[f'{channel_name2}'].sum()
    df['Diference'] = df[f'{channel_name1}Ratios'] / df[f'{channel_name2}Ratios']
    return (df['Diference'].sort_values(ascending = False))

print(compare('viniccius13', 'JovemNerd').head(50))