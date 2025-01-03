# FDU-PRML-2024-final-PJ
This is the repo that provides our train/test logs and visualization code for FDU PRML 2024 final PJ: CV, 3D point cloud semantic segmentation on ScanNet v2 dataset.

## What we have

The folders below each represents a model's result, they are:
- cac_ptv2_lovasz
- cac_spunet
- oacnn
- octformer
- ptv2_base
- ptv2_lovazs
- ptv3
- spunet

For each model, we contain the files below, two predicted scenes and train/test log:

- scene0011_00_pred.npy
- scene0011_01_pred.npy
- test.log
- train.log

Also we include two scenes' files, including the input .ply file and the ground truth .ply file.

## Quick start

The setup is easy, just make sure the environment contains numpy and open3d.

To generate the corresponding point cloud .ply for predicted output .npy, please run `generate_point_cloud.py`. You need to modify the lines below to the correct folder path, and we can take OA-CNNs results as an example:

```py
coord_path = "./scene0011_00/coord.npy"  # 实际坐标文件路径
color_path = "./scene0011_00/color.npy"  # 实际颜色文件路径
pred_path = "./oacnn/scene0011_00_pred.npy"  # 预测标签文件路径
output_path = "oacnn_output_point_cloud.ply"  # 输出的点云文件路径
```
To visualize the point cloud, you need to modify the lines in `paint_point_cloud.py` to visualize the result you want:


```py
# input
pcd = o3d.io.read_point_cloud('./scene0011_00/scene0011_00_vh_clean_2.ply')
o3d.visualization.draw_geometries([pcd])
# ground truth
pcd = o3d.io.read_point_cloud('./scene0011_00/scene0011_00_vh_clean_2.labels.ply')
o3d.visualization.draw_geometries([pcd])
# segment result
pcd = o3d.io.read_point_cloud('oacnn_output_point_cloud.ply')
o3d.visualization.draw_geometries([pcd])
```
