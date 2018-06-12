import pandas as pd 
import matplotlib.pyplot as plt

import numpy as np



# plotting Series


data=[100,120,140,150,180,201,215,300]

s=pd.Series(data)

s.index=["a","b","c","d","e","f","g","h"]



print(s.describe())

print("mean:",s.mean())

s.plot(kind="bar")





fruits =["apples","pears","cherries","bananas"]
series = pd.Series([10,30,50,60],index=fruits )


print(series)

series.plot.pie(figsize=(6,6))







# DataFrame



dict= {"country":["Brasile","Russia","India","China","South Africa"],
      "capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
      "area":[0.516,17.10,3.286,9.597,1.221],
      "population":[200.4,143.5,1252,1357,52.89]}

my_data=pd.DataFrame(dict)
print(my_data.describe())

my_data.index=["BR","RU","IN","CH","SA"] 

my_data.iloc[:, 3]+=1






names  = {"Bob","Jessica","Mary","John","Mel"}
births = {968,155,77,578,973}

concat = list(zip(names,births))

df= pd.DataFrame(data=concat ,columns=["Names","births"])

df=df.sort_values(["births"], ascending=False)

print(df.head(2))

print("Max Birth :", df["births"].max())









raw_data = {'student_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'test_score': [76, 88, 84, 67, 53, 96, 64, 91, 77, 73, 52, np.NaN]}
df1 = pd.DataFrame(raw_data, columns = ['student_name', 'test_score'])



# Create a list to store the data
grades = []


for row in df1['test_score']:
    
    if row > 95:
        # Append a letter grade
        grades.append('A')
    
    elif row > 90:
        
        grades.append('A-')
   
    elif row > 85:
     
        grades.append('B')
   
    elif row > 80:
      
        grades.append('B-')
   
    elif row > 75:
      
        grades.append('C')
    
    elif row > 70:
        
        grades.append('C-')
   
    elif row > 65:
       
        grades.append('D')
    
    elif row > 60:
       
        grades.append('D-')

    else:
        
        grades.append('Failed')
        
# Create a column from the list
df1['grades'] = grades



#print(df2)




# adding/deleting Columns 


d=[0,1,2,3,4,5,6,7,8,9]

df2=pd.DataFrame(d)

df2.columns=["Rev"]

df2["NewCol"]=5

del df2["NewCol"] 

df2["test"]=3

df2["col"]=df2["Rev"]

df2.index =["a","b","c","d","e","f","g","h","i","j"]
print(df2.iloc[0:3])
print(df2.tail(3))






# Export to Excel  Formats


df3= pd.DataFrame(d,columns = ["Numbers"])
#df3.to_excel("pandaExportTest.xlsx",sheet_name ="testing",index = True)



# read Excel file


xl = pd.ExcelFile("pandaExportTest.xlsx")

re=xl.parse(xl.sheet_names[0])

#print(re)






#Pollting DataFrame


da = {"one":[20,5,30,15,20,54,63,12,54,87],
      "tow":[52,69,32,45,4,64,34,78,13,90]}


df4=pd.DataFrame(da,columns=["one","tow"]) 

df4.plot()
plt.show()     











