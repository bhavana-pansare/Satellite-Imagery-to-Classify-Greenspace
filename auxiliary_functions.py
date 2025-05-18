import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from matplotlib.colors import ListedColormap

def save_image(image_array, image_path):
    image = Image.fromarray(image_array)
    image.save(image_path, 'PNG', quality=100)

def open_image(image_path):
    return np.array(Image.open(image_path))

def reclassify_worldcover_map():
    esa_class_dict = {
    10: (0, 100, 0),        # Tree Cover
    20: (255,187,34),       # Shrubland
    30: (255, 255, 76),     # Grassland
    40: (240, 150, 255),    # Cropland
    50: (250, 0, 0),        # Builtup
    60: (180, 180, 180),    # Bare/sparse vegetation
    70: (240, 240, 240),    # Snow and Ice
    80: (0, 100, 200),      # Permanent water bodies
    90: (0, 150, 160),      # Heraceous wetland
    95: (0, 207, 117),      # Heraceous wetland
    100: (250, 230, 160),   # Moss and lichen
    }

    esa_landcover = np.array(Image.open("./Worldcover_Map/2020_ESA_WorldCover_Map.png"))

    # Create a new numpy array with the same shape as the original
    class_label = np.zeros((esa_landcover.shape[0], esa_landcover.shape[1]), dtype=np.uint8)

    # Re-assign the values based on the given dictionary
    for key, value in esa_class_dict.items():
        class_label[np.where(np.all(esa_landcover == value, axis=-1))] = key

    # Assign each value in class_label a value of 0, 1, or 2 based on the original RGB values
    class_label[np.where(np.isin(class_label, [40, 80]))] = 0  # Background
    class_label[np.where(np.isin(class_label, [50, 60]))] = 0  # Urban
    class_label[np.where(np.isin(class_label, [10, 30, 90]))] = 200  # Greenspace

    # Create a colourmap with 2 colours
    greenspace_urban_cmap = ListedColormap(['white', 'green'])

    # Display the original and the result
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    ax[0].imshow(esa_landcover)
    ax[0].set_title("2020 ESA WorldCover Map")
    ax[1].imshow(class_label, cmap=greenspace_urban_cmap)
    ax[1].set_title("Binary Label Interpretation")

    plt.show()

    save_image(class_label, f"./Worldcover_Map/2020_ESA_WorldCover_Map_Reclassified.png")

def generate_image_paths(df, feature_dir="./S2_chips", label_dir=None, images=["True_Colour", "False_Colour", "Scene_Mask"]):
    """
    Given dataframe with a column for chip_id, returns a dataframe with a column
    added indicating the path to each PNG image as "{im}_path", eg "True_Colour_path".
    A column is also added to the dataframe with paths to the label PNG, if the
    path to the labels directory is provided.
    """
    df = df.copy()
    if feature_dir is not None:
        for im in images:
            df[f"{im}_path"] = str(feature_dir) +"/"+ df["chip_id"] +"/"+ f"{im}.png"
    
    if label_dir is not None:
        df["Label_path"] = str(label_dir) +"/2020_ESA_WorldCover_Map_Reclassified.png"

    return df

def generate_masking_paths(df):
    df = df.copy()
    true_colour_masked_dir = "./S2_True_Colour_Masked"
    false_colour_masked_dir = "./S2_False_Colour_Masked"

    # Create the target directory if it doesn't exist
    if not os.path.exists(true_colour_masked_dir):
        os.makedirs(true_colour_masked_dir)

    if not os.path.exists(false_colour_masked_dir):
        os.makedirs(false_colour_masked_dir)

    if true_colour_masked_dir is not None:
        df["True_Colour_M_path"] = str(true_colour_masked_dir) +"/True_Colour_M_"+ df["chip_id"]+".png"
        df["True_Colour_M_label_path"] = str(true_colour_masked_dir) +"/True_Colour_M_"+ df["chip_id"]+"_label.png"

    if false_colour_masked_dir is not None:
        df["False_Colour_M_path"] = str(false_colour_masked_dir) +"/False_Colour_M_"+ df["chip_id"]+".png"
        df["False_Colour_M_label_path"] = str(false_colour_masked_dir) +"/False_Colour_M_"+ df["chip_id"]+"_label.png"

    return df