import re
import pandas as pd
import numpy as np
def preprocess(data):
    pattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s(?:am|pm) - '
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({'user_message':messages,'date':dates})
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p - ')
    df.head()
    users = []
    messages = []
    for i in df['user_message']:
        entry = re.split('([\w\W]+?):\s', i)
        if entry[1:]:   #username
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users 
    df['message'] = messages
    df.drop(columns = ['user_message'], inplace = True)  

    df['only_date'] = df['date'].dt.date
    df['Year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month  
    df['Month'] = df['date'].dt.month_name()
    df['Day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['Hour'] = df['date'].dt.hour
    df['Minute'] = df['date'].dt.minute 

    period = []
    for hour in df[['day_name','Hour']]['Hour']:
        if hour == 23:
            period.append(str(hour)+"-"+str("00"))
        elif hour == 0:
            period.append(str("00")+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))  

    df['Period'] = period
        
    return df