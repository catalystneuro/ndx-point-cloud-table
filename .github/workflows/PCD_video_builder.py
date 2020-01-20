
##### Creating a movie using Point Cloud Data


from glob import glob
import os
from tqdm import tqdm
import numpy as np
import open3d as o3
import cv2


##### Methods


# For a given point cloud data, this function saves a .json file that includes pinhole camera parameters
#for a viewpoint specified by user in the clipboard
#The .json file is saved in filename
def save_view_point(pcd, filename):
    vis = o3.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()  # user changes the view and press "q" to terminate
    param = vis.get_view_control().convert_to_pinhole_camera_parameters()
    o3.io.write_pinhole_camera_parameters(filename, param)
    vis.destroy_window()


# For a given point cloud data, this function reads a .jason file corresponding
#to a spcecific viewpoint from filename directory and saves the .png image of
#that pcd at that viewpoint.
def load_view_point(pcd, filename, imagename):
    vis = o3.visualization.Visualizer()
    vis.create_window()
    ctr = vis.get_view_control()
    param = o3.io.read_pinhole_camera_parameters(filename)
    vis.add_geometry(pcd)
    ctr.convert_from_pinhole_camera_parameters(param)
    vis.run()
    vis.capture_screen_image(imagename)
    vis.destroy_window()


# This function builds and saves .png files corresponding to each pcd file at 
# specific viewpoints provided by the user on the clipboard
def png_view_point(FramePerPCD,ply_fpaths,image_folder):
    t = 0
    for fpath in tqdm(ply_fpaths):
        pcd = o3.io.read_point_cloud(fpath)
        for j in np.arange(FramePerPCD):
            save_view_point(pcd, "{}/viewpoint{}.json".format(image_folder,t))
            load_view_point(pcd, "{}/viewpoint{}.json".format(image_folder,t), "{}/image{}.png".format(image_folder,t))
            t += 1


# This function takes a folder that includes all the .png files to create a video
#and saves the created video in the current working directory with video_name.
def png_video_builder(image_folder,video_name):

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    
    video = cv2.VideoWriter(video_name, 0, 4, (width,height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    
    cv2.destroyAllWindows()
    video.release()


##### Main


# Determining the path for .ply point cloud files
data_dir = '/Users/Admin/Desktop/Ben Dichter/points/'
ply_dir = os.path.join(data_dir, 'points')
ply_fpaths = glob(ply_dir + '/*.ply')


# Build and save .png files at specific viewpoints
FramePerPCD = 2
image_folder = "Image_Folder"
png_view_point(FramePerPCD,ply_fpaths,image_folder)


#Creating movie
video_name = "Mouse_Video.avi"
image_folder = "Image_Folder"
png_video_builder(image_folder,video_name)

