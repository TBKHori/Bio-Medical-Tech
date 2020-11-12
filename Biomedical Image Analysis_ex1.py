# Sample Walk thru.
import imageio
import matplotlib.pyplot as plt
im = imageio.imread('body-001.dcm')
type(im)
im.meta 
im.meta['Modality']
im.meta.keys()
plt.imshow(im, cmap='gray')
plt axis('off')
plt.show()

# Actual Exercise
# Import ImageIO
import imageio

# Load "chest-220.dcm"
im =imageio.imread('chest-220.dcm')

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)
plt.imshow(im, cmap='gray')
plt axis('off')
plt.show()