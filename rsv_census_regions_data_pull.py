import pandas as pd

urls = ['https://www.cdc.gov/surveillance/nrevss/images/trend_images/RSV124PP_Reg1.htm', # northeast
        'https://www.cdc.gov/surveillance/nrevss/images/trend_images/RSV124PP_Reg2.htm', # midwest
        'https://www.cdc.gov/surveillance/nrevss/images/trend_images/RSV124PP_Reg3.htm', # south
        'https://www.cdc.gov/surveillance/nrevss/images/trend_images/RSV124PP_Reg4.htm'] # west

frames = []
for table in urls:
    temp_df = pd.read_html(table)[0]
    temp_df = temp_df[['RepWeekDate', 'RegID', 'PCR Detection']]
    temp_df.drop('Unnamed: 0', axis = 1, inplace = True, errors = 'ignore')
    frames.append(temp_df)
df = pd.concat(frames)
df.to_csv('rsv_regional_data.csv', index = False)