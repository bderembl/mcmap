#/usr/bin/env python

#import numpy as np
#import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#http://stackoverflow.com/questions/3279560/invert-colormap-in-matplotlib
def reverse_colourmap(cmap, name = 'my_cmap_r'):
    """
    In: 
    cmap, name 
    Out:
    my_cmap_r

    Explanation:
    t[0] goes from 0 to 1
    row i:   x  y0  y1 -> t[0] t[1] t[2]
                   /
                  /
    row i+1: x  y0  y1 -> t[n] t[1] t[2]

    so the inverse should do the same:
    row i+1: x  y1  y0 -> 1-t[0] t[2] t[1]
                   /
                  /
    row i:   x  y1  y0 -> 1-t[n] t[2] t[1]
    """        
    reverse = []
    k = []   

    for key in cmap._segmentdata:    
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []

        for t in channel:                    
            data.append((1-t[0],t[2],t[1]))            
        reverse.append(sorted(data))    

    LinearL = dict(zip(k,reverse))
    my_cmap_r = LinearSegmentedColormap(name, LinearL) 
    return my_cmap_r


#http://cresspahl.blogspot.com/2012/03/expanded-control-of-octaves-colormap.html
#http://nbviewer.jupyter.org/github/kwinkunks/notebooks/blob/master/Matteo_colourmaps.ipynb

# MR=[0,0; 
#     0.02,0.3; %this is the important extra point
#     0.3,1;
#     1,1];
# MG=[0,0;
#     0.3,0; 
#     0.7,1;
#     1,1];
# MB=[0,0; 
#     0.7,0;
#     1,1];

def cool():
  
  cdict1 = {'blue':   ((0.0, 0.0, 0.0),
                      (0.02, 0.3, 0.3),
                      (0.3, 1.0, 1.0),
                      (1.0, 1.0, 1.0)),
  
           'green': ((0.0, 0.0, 0.0),
                     (0.3, 0.0, 0.0),
                     (0.7, 1.0, 1.0),
                     (1.0, 1.0, 1.0)),
  
           'red':  ((0.0, 0.0, 0.0),
                     (0.7, 0.0, 0.0),
                     (1.0, 1.0, 1.0))
          }
  
  
  blue_red1 = LinearSegmentedColormap('cool', cdict1)

  return blue_red1


def cool_r():
  
  cdict1 = {'blue':   ((0.0, 1.0, 1.0),
                       (0.7, 1.0, 1.0),
                       (0.98, 0.3, 0.3),
                      (1.0, 0.0, 0.0)),
  
           'green': ((0.0, 1.0, 1.0),
                     (0.3, 1.0, 1.0),
                     (0.7, 0.0, 0.0),
                     (1.0, 0.0, 0.0)),
  
           'red':  ((0.0, 1.0, 1.0),
                     (0.3, 0.0, 0.0),
                     (1.0, 0.0, 0.0))
          }
  
  blue_red1 = LinearSegmentedColormap('cool_r', cdict1)

  return blue_red1

# from Callies
def blues():

  cdict = {
    'red': ((0.0, 0.0, 0.0), 
            (0.5, 0.216, 0.216), 
            (1.0, 1.0, 1.0)),

    'green': ((0.0, 0.0, 0.0), 
              (0.5, 0.494, 0.494), 
              (1.0, 1.0, 1.0)),

    'blue': ((0.0, 0.0, 0.0), 
             (0.5, 0.722, 0.722), 
             (1.0, 1.0, 1.0))}
  cm_blues = LinearSegmentedColormap('blues', cdict, 256)

  return cm_blues


def blues_r():

  cdict = {
    'red': ((0.0, 1.0, 1.0), 
            (0.5, 0.216, 0.216), 
            (1.0, 0.0, 0.0)),

    'green': ((0.0, 1.0, 1.0), 
              (0.5, 0.494, 0.494), 
              (1.0, 0.0, 0.0)),

    'blue': ((0.0, 1.0, 1.0), 
             (0.5, 0.722, 0.722), 
             (1.0, 0.0, 0.0))}
  cm_blues = LinearSegmentedColormap('blues_r', cdict, 256)

  return cm_blues


# def cool_r():
#   return reverse_colourmap(cool)

#x = np.arange(0, np.pi, 0.1)
#y = np.arange(0, 2*np.pi, 0.1)
#X, Y = np.meshgrid(x, y)
#Z = np.cos(X) * np.sin(Y) * 10
  
#plt.imshow(Z, interpolation='nearest', cmap=blue_red1)
#plt.colorbar()
