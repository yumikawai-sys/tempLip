import os
import cv2
import tempfile

# Create a temporary directory
p = tempfile.mkdtemp()

# Generate FFmpeg command
file_path = 'C:\\Users\\Yumi\\Documents\\code\\LipNet-PyTorch\\clip.mp4'
cmd = f'ffmpeg -i "{file_path}" -qscale:v 2 -r 25 "{p}/%d.jpg"'
os.system(cmd)
print('cmd:', cmd)

# Check if the directory exists
if os.path.exists(p):
    # List files in the directory
    files = os.listdir(p)
    print('files1:', files)
    
    # # Sort files based on filename
    # files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))
    # print('files2:', files)
    
    # # Read images using OpenCV
    # array = [cv2.imread(os.path.join(p, file)) for file in files]
    # print('array1:', array)
else:
    print(f"Directory {p} does not exist.")
