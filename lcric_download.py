from pytube import YouTube
from tqdm import tqdm
import pandas as pd
import os
import numpy as np


def download(csv_loc):
    all_vids = pd.read_csv(csv_loc)
    vids_arr = np.array(all_vids)

    if not os.path.exists('./videos'):
        os.mkdir('./videos/')

    for vid in tqdm(vids_arr[1:]):
        vid_name =  vid[0]
        vid_link = vid[1]

        try:
            yt = YouTube(vid_link)
        except:
            print("Video ", vid_name, " not present!!!")

        mp4files = yt.streams.filter(file_extension='mp4')
        stream = mp4files.get_by_resolution("360p")

        stream.download(filename='./videos/' + vid_name+'.mp4')


if __name__ == '__main__':
    csv_loc = 'lcric_video_links.csv'
    download(csv_loc)
