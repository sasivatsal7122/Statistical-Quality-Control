import pandas as pd 
import statistics
from statistics import mean,pstdev
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("data.xlsx")
table_df = pd.read_excel("table_values.xlsx")
print(df)
print(table_df)
count_row = df.shape[0]
count_col = df.shape[1]-1
print("No.of Observations: ",count_col)
A2 = table_df.iloc[count_col-2,1]
D3 = table_df.iloc[count_col-2,2]
D4 = table_df.iloc[count_col-2,3]
print("VALUE OF A2: ",A2)
print("VALUE OF D3: ",D3)
print("VALUE OF D4: ",D4)

mean_ls=[]
range_ls=[]
for i in range(count_row):
    row = df.iloc[i,1:]
    range_ls.append(row.max()-row.min())
    mean_ls.append(row.mean())
mean_str_rounded_ls = [ '%.5f' % elem for elem in mean_ls ]
integer_map = map(float,mean_str_rounded_ls)
mean_rounded_ls = list(integer_map)
range_str_rounded_ls = [ '%.5f' % elem for elem in range_ls ]
integer_mapp = map(float,range_str_rounded_ls)
range_rounded_ls = list(integer_mapp)
meanchart_control_limit = round(mean(mean_rounded_ls),5)
print("\nMEAN-CHART CONTROL LIMIT: ",meanchart_control_limit)
rangechart_control_limit = round(mean(range_rounded_ls),5)
print("\nRANGE-CHART CONTROL LIMIT: ",rangechart_control_limit)

m_sd = statistics.pstdev(mean_rounded_ls)
m_upper_control_limit = meanchart_control_limit + A2*rangechart_control_limit
m_lower_control_limit = meanchart_control_limit - A2*rangechart_control_limit
print("\nMEAN-CHART UPPER CONTROL LIMIT: ",m_upper_control_limit)
print("MEAN-CHART LOWER CONTROL LIMIT: ",m_lower_control_limit)

r_sd = statistics.pstdev(range_rounded_ls)
r_upper_control_limit = D4*rangechart_control_limit
r_lower_control_limit = D3*rangechart_control_limit
print("\nRANGE-CHART UPPER CONTROL LIMIT: ",r_upper_control_limit)
print("RANGE-CHART LOWER CONTROL LIMIT: ",r_lower_control_limit)

m_arr = np.array(mean_rounded_ls)
m_uc_arr = np.ones(len(mean_rounded_ls))*m_upper_control_limit
m_lc_arr = np.ones(len(mean_rounded_ls))*m_lower_control_limit
m_c_arr = np.ones(len(mean_rounded_ls))*meanchart_control_limit
plt.plot(m_arr, marker='o', linestyle='--', color='r', label='observations') 
plt.plot(m_uc_arr,linestyle='-',color='g', label='upper control limit') 
plt.plot(m_lc_arr,linestyle='-', color='b', label='lower control limit') 
plt.plot(m_c_arr,linestyle='-', color='black', label='control limit') 
plt.xlabel('x-axis')
plt.ylabel('y-axis') 
plt.title('MEAN CHART')
plt.legend() 
plt.show()
r_arr = np.array(range_rounded_ls)
r_uc_arr = np.ones(len(range_rounded_ls))*r_upper_control_limit
r_lc_arr = np.ones(len(range_rounded_ls))*r_lower_control_limit
r_c_arr = np.ones(len(range_rounded_ls))*rangechart_control_limit
plt.plot(r_arr, marker='o', linestyle='--', color='r', label='observations') 
plt.plot(r_uc_arr,linestyle='-',color='g', label='upper control limit') 
plt.plot(r_lc_arr,linestyle='-', color='b', label='lower control limit') 
plt.plot(r_c_arr,linestyle='-', color='black', label='control limit') 
plt.xlabel('x-axis')
plt.ylabel('y-axis') 
plt.title('RANGE CHART')
plt.legend() 
plt.show()
