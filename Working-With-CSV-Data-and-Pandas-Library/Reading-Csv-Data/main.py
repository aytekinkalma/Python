import pandas as pandas

data=pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])
print(type(data['temp']))

data_dict=data.to_dict()
print(data_dict,'\n')

temp_list=data['temp'].to_list()
print(temp_list,'\n')

avarge_temp=sum(temp_list)/len(temp_list)
print("Avarage Temp={}".format(avarge_temp))

avr=(data['temp']).mean()
print("Avarage Temp={}".format(avr))

max_temp=max(temp_list)
print(max_temp)

#get data in columns
print(data['condition'])
print(data.condition)

#get data in rows

print(data[data.day=='Monday'])

print(data[data.temp==data.temp.max()])

monday=data[data.day=='Monday']
monday_temp=int(monday.temp)
monday_temp_F=monday_temp*9+32
print(monday_temp_F)


data_dict={'students':['Amy','James','Angela'],'scores':[76,56,65]}
data=pandas.DataFrame(data_dict)
print(data)
