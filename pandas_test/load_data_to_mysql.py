import pandas as pd
from sqlalchemy import create_engine

# -*- coding: utf-8 -*-

# 数据库1连接信息
dolphin1 = "mysql+pymysql://root:cestc%40mysql@10.255.135.154:3306/dolphin1"
engine = create_engine(dolphin1)

# 读取省的csv数据
province_path = "C:\develop\code\python_learn\csv\province.csv"

province_data = pd.read_csv(province_path)
# 省数据增加一列，pcode，默认为0
province_data["pcode"] = 0
# 增加level一列，默认为1
province_data["level"] = 1

# 将数据写入到数据库1中
province_data.to_sql("t_area", engine, if_exists="append", index=False)

# 读取市的csv数据
city_path = "C:\develop\code\python_learn\csv\city.csv"
city_data = pd.read_csv(city_path)
# 市数据列名p_code修改成pcode
city_data.rename(columns={"p_code": "pcode"}, inplace=True)
# 增加level一列，默认为2
city_data["level"] = 2

# 将数据写入到数据库1中
city_data.to_sql("t_area", engine, if_exists="append", index=False)

# 读取区的csv数据
area_path = "C:\develop\code\python_learn\csv\county.csv"
area_data = pd.read_csv(area_path)
# 区数据列名c_code修改成pcode
area_data.rename(columns={"c_code": "pcode"}, inplace=True)
# 增加level一列，默认为3
area_data["level"] = 3

# 将数据写入到数据库1中
area_data.to_sql("t_area", engine, if_exists="append", index=False)
