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

# Ex2
# Import ImageIO
import imageio
im = imageio.imread('chest-220.dcm')

# Print the available metadata fields
print(im.meta.keys())

print(im.meta['Modality'])
# Result: CT
print(im.meta['PatientSex'])
# Result: F
print(im.meta['StudyDate'])
# Result: 20040529

# Ex3
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

# Guide Sample
import imageio
import numpy as np

im1 = imageio.imread('chest-000.dcm')
im2 = imageio.imread('chest-001.dcm')
im3 = imageio.imread('chest-002.dcm')
im1.shape
# Result: (512, 512)

vol = np.stack([im1, im2, im3])
vol.shape
# Result: (3, 512, 512)

import os
os.listdir('chest-data')

# Result: ['chest-000.dcm', 'chest-001.dcm', 'chest-002.dcm', ..., 'chest-049.dcm']

import imageio
vol = imageio.volread('chest-data')
vol.shape
# Result: (50, 512, 512)

# Image Shape - Number of elements along each axis
import imageio
vol = imageio.volread(
            'chest-data')
# Image shape (in vowels)
n0, n1, n2 = vol.shape
n0, n1, n2
# Result: (50, 512, 512)

# Sampling rate - Physical space covered by each element

# Sampling rate (in mm)
d0, d1, d2 = vol.meta['sampling']
d0, d1, d2
# Result: (2, 0.5, 0.5)

# Field of view - Physical space covered along each axis

# Field of view( in mm)
n0 * d0, n1 * d1, n2 * d2
# Result: (100, 256, 256)

# Ex4
# Import ImageIO and NumPy
import imageio
import numpy as np

# Read in each 2D image
im1 = imageio.imread('chest-220.dcm')
im2 = imageio.imread('chest-221.dcm')
im3 = imageio.imread('chest-222.dcm')

# Stack images into a volume
vol = np.stack([im1, im2, im3])
print('Volume dimensions:', vol.shape)

# Ex5
# Import ImageIO
import imageio

# Load the "tcia-chest-ct" directory
vol = imageio.volread('tcia-chest-ct')

# Print image attributes
print('Available metadata:', vol.meta.keys())
print('Shape of image array:', vol.shape)

# Diving in the metadata

print (vol.meta['PatientWeight'])
# Result: 82.0
print (vol.meta['StudyDescription'])
# Result: PET CT with registered MR
print (vol.meta['PatientID'])
# Result: STS_007
print (vol.meta['StudyTime'])
# Result: 115208
print (vol.meta['Manufacturer'])
# Result: GE MEDICAL SYSTEMS

# EX6
print(vol.shape)
# Result: (25, 512, 512)

print(vol.meta['sampling'])
# Result: (3.270000000000001, 0.976562, 0.976562)

#Calculating Field of View in mm using Array shape & Sampling resolution
25 * 3.270000000000001, 512 * 0.976562, 512 * 0.976562
# Result: (81.75000000000003, 499.999744, 499.999744)
# Rounded off
(82, 500, 500)

#Sample Guide

# Plotting multiple images at once

# plt.subplots - creates a figure canvas with multiple AxesSubplots objects.

import imageio
vol = imageio.volread('chest-data')
fig, axes = plt.subplots(nrows=1, ncols=3)
axes[0].imshow(vol[0],cmap='gray')
axes[1].imshow(vol[10],cmap='gray')
axes[2].imshow(vol[20],cmap='gray')
for ax in axes:
    ax.axis('off')
plt.show()

# Non-standard views
import imageio

vol = imageio.volread('chest-data')
views_1v2 = vol[pln, :, :]
views_1v2 = vol[pln]
view_0v2 = vol[:, row, :]
view_0v1 = vol[:, :, col]

# Modifying the aspect ratio 
im = vol[:,:,100]
d0, d1, d2 = vol.meta['sampling']
d0, d1, d2
# Result: (2, 0.5, 0.5)

asp = d0 / d1
asp
# Result: 3

plt.imshow(im, cmap='gray', aspect=asp)
plt.show()

# Ex7
# Import PyPlot
import matplotlib.pyplot as plt

# Initialize figure and axes grid
fig, axes = plt.subplots(nrows=2, ncols=1)

# Draw an image on each subplot
axes[0].imshow(im1, cmap='gray')
axes[1].imshow(im2, cmap='gray')

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')
plt.show()

#Ex8
# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=1, ncols=4)

# Loop through subplots and draw image
for ii in range(4):
    im = vol[ii * 40, :, :]
    axes[ii].imshow(im, cmap='gray')
    axes[ii].axis('off')

# Render the figure
plt.show()

# Ex8
# Select frame from "vol"
im1 = vol[:, 256, :]
im2 = vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2 = vol.meta['sampling']
asp1 = d0 / d2
asp2 = d0 / d1

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].imshow(im1, cmap='gray', aspect=3.3484817144226335)
axes[1].imshow(im2, cmap='gray', aspect=3.3484817144226335)
plt.show()