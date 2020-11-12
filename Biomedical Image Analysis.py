# Sample Walk thru.
import imageio
import matplotlib.pyplot as plt

im = imageio.imread('body-001.dcm')
type(im)
im.meta 
im.meta['Modality']
im.meta.keys()

# Draw the image in grayscale
plt.imshow(im, cmap='gray')
plt.axis('off')

# Render the image
plt.show()

# Ex1
# Import ImageIO
import imageio

# Load "chest-220.dcm"
im =imageio.imread('chest-220.dcm')

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)

# Draw the image in grayscale
plt.imshow(im, cmap='gray')
plt.axis('off')

# Render the image
plt.show()

#Ex2
# Import ImageIO
import imageio
im = imageio.imread('chest-220.dcm')

# Print the available metadata fields
print(im.meta.keys())

print(im.meta['Modality'])
# Ans: CT
print(im.meta['PatientSex'])
# Ans: F
print(im.meta['StudyDate'])
# Ans; 20040529

#Ex 3
# Import ImageIO and PyPlot 
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread('chest-220.dcm')

# Draw the image in grayscale
plt.imshow(im, cmap='gray', vmin=-200, vmax=200)
plt.axis('off')

# Render the image
plt.show()