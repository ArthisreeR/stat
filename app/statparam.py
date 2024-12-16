
import json
import pandas as pd
def stat(data_dict):
    
    data_r = data_dict["data"]
    total_sum=sum(data_r)
    count = len(data_r)
    meand = total_sum / count
    print("mean:",meand)
    sorted_data = sorted(data_r)
    n = len(sorted_data)
    mid = n // 2
    mid_left = sorted_data[mid - 1]
    mid_right = sorted_data[mid]
    mediandata=(mid_left + mid_right) / 2
    print("median:",mediandata)
    q1_index = 0.25 * (n + 1) - 1
    if q1_index.is_integer():
        q1 = sorted_data[int(q1_index)]
    else:
        lower = sorted_data[int(q1_index)]
        upper = sorted_data[int(q1_index) + 1]
        q1 = lower + (upper - lower) * (q1_index % 1)
    print("q1:",q1)
    q3_index = 0.75 * (n + 1) - 1
    if q3_index.is_integer():
        q3 = sorted_data[int(q3_index)]
    else:
        lower = sorted_data[int(q3_index)]
        upper = sorted_data[int(q3_index) + 1]
        q3 = lower + (upper - lower) * (q3_index % 1)
    print("q3:",q3)
    IQR = q3-q1
    lower_limit = q1 - 1.5 * IQR
    upper_limit = q3 + 1.5 * IQR
    print("ll:",lower_limit)
    print("UL:",upper_limit)
    variance = sum((x - meand) ** 2 for x in data_r) / len(data_r)
    std_dev = variance ** 0.5
    print("sd:",std_dev)
   
    std_limits = {
        "1_std_limits": (meand - std_dev, meand + std_dev),
        "2_std_limits": (meand - 2 * std_dev, meand + 2 * std_dev),
        "3_std_limits": (meand - 3 * std_dev, meand + 3 * std_dev)
    }
    print("stdlim:",std_limits )

    output= {
            "meanval":meand,
            "medianval":mediandata,
            "IQR":IQR,
            "Lowerlimit":lower_limit,
            "upperlimit":upper_limit,
            "stdlimits":std_limits
           }
    
    print("output:",output)
    
    
    
    return output


''''input_file=input(enter)
with open(input_file, "w") as file:
    json.dump(numbersdata,file, indent=4) '''



    

 
