import os
import matplotlib.pyplot as plt
from PIL import Image

def save_progress(save_dir, prefix, i):
    file = os.path.join(save_dir, prefix + "_%.6i.png"%(i+1))
    plt.savefig(file, bbox_inches='tight', pad_inches=0.1, dpi=100, facecolor="white")
    return file

def make_gif(imagefiles, output_path, fps=20):
    imgs = [Image.open(file) for file in imagefiles]
    imgs[0].save(fp=output_path, format='GIF', append_images=imgs[1:], save_all=True, duration=int(1000/fps), loop=True)

def reset_parameters(model):
    for layer in model.children():
        if hasattr(layer, 'reset_parameters'):
            layer.reset_parameters()