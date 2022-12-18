import pandas as pd
import cv2
import matplotlib.pyplot as plt
from typing import List
import numpy as np

def img_height(path: str) -> int:
    img = cv2.imread(path)
    return img.shape[0]


def img_width(path: str) -> int:
    img = cv2.imread(path)
    return img.shape[1]


def img_channels(path: str) -> int:
    img = cv2.imread(path)
    return img.shape[2]


def img_pixels(path: str) -> int:
    img = cv2.imread(path)
    return img.size



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

def df_mark_filter(df: pd.DataFrame, class_mark: int) -> pd.DataFrame:
    return df[df['mark'] == class_mark]


def df_dimentions_filter(df: pd.DataFrame, m_Height: int, m_Weight: int, class_mark: int) -> pd.DataFrame:
    return df[(df.mark == class_mark) & (df.height <= m_Height) & (df.width <= m_Weight)]


def df_pixel_statistics(df: pd.DataFrame, class_mark: int) -> pd.DataFrame:
    df['pixel'] = df['Path'].apply(img_pixels)
    df = df_mark_filter(df, class_mark)
    df.groupby('pixel').count()
    print(df.pixel.describe())


def create_histogram(df: pd.DataFrame, class_mark: int) -> List[np.ndarray]:
    df = df_mark_filter(df, class_mark)
    df = df.sample()
    for item in df['Path']:
        path = item
    img = cv2.imread(path)
    color = ('b', 'g', 'r')
    result = [[], []]
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        result[0].append(histr)
        result[1].append(col)
    return result


def draw_histrogram(df: pd.DataFrame, class_mark: int) -> None:
    tmp = create_histogram(df, class_mark)
    for i in range(len(tmp[0])):
        plt.plot(tmp[0][i], color=tmp[1][i])
        plt.xlim([0, 256])
    plt.xlabel("Intensity")
    plt.ylabel("Number of pixels")
    plt.show()


if __name__ == '__main__':
    df = create_DataFrame()
