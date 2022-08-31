from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter


#Methods for chart
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path:str):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def retrieve_colors(image, num_colors,show_chart):
    mod_img = cv2.resize(image, (600,400), interpolation = cv2.INTER_AREA)
    mod_img = mod_img.reshape(mod_img.shape[0]*mod_img.shape[1],3)
    clf = KMeans(n_clusters = num_colors)
    labels = clf.fit_predict(mod_img)
    counts = Counter(labels)

    center_colors = clf.cluster_centers_
# We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        plt.show()

    return rgb_colors

def main():
    retrieve_colors(get_image('Birthday picture.png'),8, True)

if __name__ == "__main__":
    main()
    

