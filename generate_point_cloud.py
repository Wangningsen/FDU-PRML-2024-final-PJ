import numpy as np
import open3d as o3d

def load_data(coord_path, color_path, pred_path):
    """加载坐标、颜色和预测标签数据"""
    coord = np.load(coord_path)
    color = np.load(color_path)
    pred = np.load(pred_path)
    
    # 检查加载的数据形状
    print(f"coord shape: {coord.shape}, color shape: {color.shape}, pred shape: {pred.shape}")
    return coord, color, pred

def map_labels_to_color(pred):
    """根据预测标签为每个点指定颜色"""
    # 定义每个类的颜色（从 Class_0 到 Class_19）
    label_to_color = {
        0: [178/255, 199/255, 231/255],  # wall
        1: [157/255, 224/255, 138/255],  # floor
        2: [53/255, 118/255, 179/255],   # cabinet
        3: [249/255, 190/255, 123/255],  # bed
        4: [187/255, 191/255, 44/255],   # chair
        5: [136/255, 87/255, 75/255],    # sofa
        6: [248/255, 153/255, 152/255],  # table
        7: [205/255, 43/255, 44/255],    # door
        8: [195/255, 176/255, 213/255],  # window
        9: [147/255, 101/255, 188/255],  # bookshelf
        10: [193/255, 156/255, 148/255], # picture
        11: [67/255, 189/255, 208/255],  # counter
        12: [244/255, 183/255, 210/255], # desk
        13: [218/255, 220/255, 143/255], # curtain
        14: [247/255, 129/255, 31/255],  # refrigerator
        15: [166/255, 219/255, 229/255], # shower curtain
        16: [60/255, 161/255, 48/255],   # toilet
        17: [114/255, 128/255, 145/255], # sink
        18: [221/255, 118/255, 194/255], # bathtub
        19: [85/255, 81/255, 162/255],   # otherfurniture
        -1: [0, 0, 0],
    }
    
    # 创建映射的颜色列表
    mapped_colors = np.array([label_to_color[label] for label in pred])
    
    return mapped_colors

def save_point_cloud(coord, color, file_path="output_point_cloud.ply"):
    """保存点云为PLY文件"""
    # 创建一个open3d点云对象
    pcd = o3d.geometry.PointCloud()
    
    # 设置点云的坐标和颜色
    pcd.points = o3d.utility.Vector3dVector(coord)
    pcd.colors = o3d.utility.Vector3dVector(color)
    
    # 保存为PLY文件
    o3d.io.write_point_cloud(file_path, pcd)
    print(f"Point cloud saved to {file_path}")

def generate_and_save_point_cloud(coord_path, color_path, pred_path, output_path="output_point_cloud.ply"):
    """根据coord, color和预测标签生成并保存点云"""
    # 加载数据
    coord, color, pred = load_data(coord_path, color_path, pred_path)
    
    # 根据预测标签修改颜色（如果需要）
    mapped_colors = map_labels_to_color(pred)
    
    # 保存点云
    save_point_cloud(coord, mapped_colors, output_path)

# 调用示例
coord_path = "./scene0011_00/coord.npy"  # 实际坐标文件路径
color_path = "./scene0011_00/color.npy"  # 实际颜色文件路径
pred_path = "./oacnn/scene0011_00_pred.npy"  # 预测标签文件路径
output_path = "oacnn_output_point_cloud.ply"  # 输出的点云文件路径

generate_and_save_point_cloud(coord_path, color_path, pred_path, output_path)


