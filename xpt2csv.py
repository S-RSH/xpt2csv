import pyreadstat

# xpt 파일 읽기
filename_xpt = 'DR1IFF_H.xpt'
df, meta = pyreadstat.read_xport(filename_xpt)

# csv 파일로 저장
filename_csv = 'DR1IFF_H.csv'
df.to_csv(filename_csv, index=False)