import open3d as o3d
# input
pcd = o3d.io.read_point_cloud('./scene0011_00/scene0011_00_vh_clean_2.ply')
o3d.visualization.draw_geometries([pcd])
# ground truth
pcd = o3d.io.read_point_cloud('./scene0011_00/scene0011_00_vh_clean_2.labels.ply')
o3d.visualization.draw_geometries([pcd])
# segment result
pcd = o3d.io.read_point_cloud('oacnn_output_point_cloud.ply')
o3d.visualization.draw_geometries([pcd])