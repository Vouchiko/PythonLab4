import pandas as pd


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
    return df3


if __name__ == '__main__':
    df = create_DataFrame()
