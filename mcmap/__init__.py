#/usr/bin/env python

#import numpy as np
#import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

#http://cresspahl.blogspot.com/2012/03/expanded-control-of-octaves-colormap.html

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
  
  
  blue_red1 = LinearSegmentedColormap('BlueRed1', cdict1)

  return blue_red1

#x = np.arange(0, np.pi, 0.1)
#y = np.arange(0, 2*np.pi, 0.1)
#X, Y = np.meshgrid(x, y)
#Z = np.cos(X) * np.sin(Y) * 10
  
#plt.imshow(Z, interpolation='nearest', cmap=blue_red1)
#plt.colorbar()
