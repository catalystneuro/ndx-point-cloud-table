
##### Creating a movie using Point Cloud Data


from glob import glob
import os
from tqdm import tqdm
import numpy as np
import open3d as o3
import cv2


##### Methods


def save_view_point_png(pcd, imagename, scale_val, rotate_val):
    """The view point of camera after a certain rotation
    
    For a given point cloud data, this function saves a .png image
    at a specified viewpoint determined by the rotation value.
    
    Parameters
    ----------
    pcd : point cloud
        This parameter is a point cloud data that can be read 
        using open3.io.read_point_cloud function from a .ply file.
    imagename : str
        This string includes the name and path to the directory for 
        saving the .png file obtained from pcd at a given 
        rotate_val (rotation angle).
    scale_val : float
        Scale ratio which is higher for more distant view points.
    rotate_val : float
        Distance the mouse cursor has moved in x-axis.
    
    Returns
    ----------
    None
    
    """
    vis = o3.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.get_view_control().rotate(rotate_val, 0.0)
    vis.get_view_control().scale(scale_val)
    vis.run()  # user changes the view and press "q" to terminate
    vis.capture_screen_image(imagename)
    vis.destroy_window()


def all_pcd_view_point(FramePerPCD,SingleRotationAngle,scale_val,ply_fpaths,image_folder):
    """Generate and save all the .png images for creating a video 
    
    Given all the point cloud data, this function saves the .png files 
    corresponding to different viewpoints. The view points are determined by 
    feeding rotation_array values to save_view_point_png function.
    
    Parameters
    ----------
    FramePerPCD : int
        This parameter indicates the number of images captured for each 
        pcd file which is equal to the number of view point values for each pcd.
    SingleRotationAngle : float
        This parameter indicates the amount of rotation in view point in each 
        step in terms of the distance the mouse cursor has moved in x-axis.
    scale_val : float
        Scale ratio which is higher for more distant view points.
    ply_fpaths : str
        A list that includes all the .ply file paths.
    image_folder : str
        The name of folder in the current directory to save the .png files
    
    Returns
    ----------
    None
    
    """
    t = 0
    rotation_array = -np.arange(0,1000,SingleRotationAngle)
    for fpath in tqdm(ply_fpaths):
        pcd = o3.io.read_point_cloud(fpath)
        for j in np.arange(FramePerPCD):
            save_view_point_png(pcd, "{}/image{:02d}.png".format(image_folder,t), scale_val, rotation_array[t])
            t += 1


def png_video_builder(image_folder,video_name,FrameRate):
    """Building a video from the .png images 
    
    This function takes all the .png files to create a video and saves it in 
    the current working directory.
    
    Parameters
    ----------
    image_folder : str
        The name of folder in the current directory that includes the .png files.
    video_name : str
        The name of video file made of the .png images.
    FrameRate : float
        Framerate of the created video stream.
    
    Returns
    ----------
    None
    
    """
    images = glob(image_folder + '/*.png')
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    
    video = cv2.VideoWriter(video_name, 0, FrameRate, (width,height))
    
    for image in images:
        video.write(cv2.imread(image))
    
    cv2.destroyAllWindows()
    video.release()


##### Main


# Determining the path for .ply point cloud files
data_dir = '/Users/Admin/Desktop/Ben Dichter/points/'
ply_dir = os.path.join(data_dir, 'points')
ply_fpaths = glob(ply_dir + '/*.ply')


# Build and save .png files at specific viewpoints
FramePerPCD = 10
SingleRotationAngle = 10
scale_val = 15
image_folder = "Image_Folder"
all_pcd_view_point(FramePerPCD,SingleRotationAngle,scale_val,ply_fpaths,image_folder)


#Creating movie
video_name = "Mouse_Video.avi"
image_folder = "Image_Folder"
FrameRate = 18
png_video_builder(image_folder,video_name, FrameRate)

