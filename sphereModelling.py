#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sphereModelling.py
#       
#       Copyright 2014 Supin P Surendran <supinps@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import numpy
from math import *
from visual import *

def pol2cart(R,r):
    th_step=(2*r)/(R+r)
    theta=numpy.arange(0,2*pi,th_step)
    phi=theta
    x=[]
    y=[]
    z=[]
    for i in theta:
        for j in phi:
            print i,j
            x.append(round(R*sin(i)*cos(j),5))
            y.append(round(R*sin(i)*sin(j),5))
            z.append(round(R*cos(j),5))
    return x,y,z

def write2file(x,y,z,r):
    fout=open("coordinates.txt",'w')
    ctr=0
    for i,j,k in zip(x,y,z):
        ctr=ctr+1
        fout.write("solid main%d = sphere(%d, %d, %d,  %d)_maxh=3.0 ;\n" % (ctr, i, j, k, r))
    fout.close()

def plotSpheres(x,y,z,r,R):
    sphere(pos=(0,0,0),radius=R,color=color.green)
    for i,j,k in zip(x,y,z):
        sphere(pos=(i,j,k),radius=r,color=color.red)

def main():
    R=float(raw_input('Radius(Main Sphere) : '))
    r=float(raw_input('Radius(Small Sphere): '))
    x,y,z=pol2cart(R,r)
    for i,j,k in zip(x,y,z):
        print i,j,k
    write2file(x,y,z,r)
    plotSpheres(x,y,z,r,R)


if __name__ == '__main__':
    main()

