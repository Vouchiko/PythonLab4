import pandas as pd
import cv2

def img_height(path: str) -> int:
    img = cv2.imread(path)
    return img.shape[0]


def img_width(path: str) -> int:
    img = cv2.imread(path)
    return img.shape[1]


def img_channels(path: str) -> int:
    img = cv2.imread(path)
    return img.shape[2]



def create_DataFrame() -> pd.DataFrame:
    df1 = pd.read_csv('Brown bear annotation', header=None)
    df2 = pd.read_csv('Polar bear annotation', header=None)
    df3 = pd.concat([df1, df2], ignore_index=None)
    df3.drop(1, axis=1, inplace=True)
    df3.rename(columns={0: 'Path', 2: 'ClassName'}, inplace=True)

    data = []
    for i in df3['ClassName']:
        if i == 'brown bear':
            data.append(0)
        elif i == 'polar bear':
            data.append(1)
        df3['mark'] = data
        df3['height'] = df3['Path'].apply(img_height)
        df3['width'] = df3['Path'].apply(img_width)
        df3['channels'] = df3['Path'].apply(img_channels)

    return df3


if __name__ == '__main__':
    df = create_DataFrame()
