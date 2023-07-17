import pandas as pd
import random
import math

def extract_data(input_file, output_file, num_records):
    df = pd.read_csv(input_file)  # 读取CSV文件

    # 抽取指定数量的记录
    extracted_data = df.sample(n=num_records)

    extracted_data.to_csv(output_file, index=False)  # 保存提取的数据到新文件

    print(f"成功提取并保存 {num_records} 条数据到 {output_file} 文件。")


def simulation_data(input_file, output_file):
    df = pd.read_csv(input_file)

    for index, raw in df.iterrows():
        # 获取经纬度
        latitude = raw[2]
        longitude = raw[1]


        angle = random.uniform(0, 2 * math.pi)  # 获取角度

        r = random.uniform(0, 0.0032) # 获取半径

        # 将极坐标转换为直角坐标
        modified_latitude = latitude + r * math.cos(angle)
        modified_longitude = longitude + r * math.sin(angle)

        # 写回模拟数据
        df.at[index, df.columns[5]] = modified_latitude
        df.at[index, df.columns[6]] = modified_longitude
        # print(raw)
    df.to_csv(output_file, index=False)


def deviation_distance(input_file, output_file):
    df = pd.read_csv(input_file)
    print(1)
    for index, raw in df.iterrows():
        modified_latitude  = raw[5]
        modified_longitude = raw[6]

        raw_latitude  = raw[2]
        raw_longitude = raw[1]

        # 将经纬度转换为弧度
        raw_lat_rad = math.radians(raw_latitude)
        raw_lon_rad = math.radians(raw_longitude)

        modified_lat_rad = math.radians(modified_latitude)
        modified_lon_rad = math.radians(modified_longitude)

        # 使用 Haversine 公式计算两点间的距离
        dlon = modified_lon_rad - raw_lon_rad
        dlat = modified_lat_rad - raw_lat_rad
        a = math.sin(dlat / 2) ** 2 + math.cos(raw_lat_rad) * math.cos(modified_lat_rad) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = 6371 * c * 1000  # 乘以半径 6371km，转换为米
        df.at[index, 'distance'] = distance
    df.to_csv(output_file, index=False)



# extract_data('E:\desktop\guang.csv', 'E:\desktop\data_new.csv', 500)
# simulation_data("E:\desktop\guang.csv","E:\desktop\data_simulation_final.csv")
deviation_distance("E:\desktop\data_simulation_final.csv","E:\desktop\data_simulation_distance_final.csv")