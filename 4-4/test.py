# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:40:24 2018

@author: user
"""
from mpi4py import MPI
from numpy import *

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

#group = comm.Get_group()
#group = group.Excl([0,1,2])
#
#new_comm = comm.Create(group)
#
#if new_comm != MPI.COMM_NULL:
#    print (comm_rank, new_comm.Get_rank())

#color = comm_rank / (comm_size / 3)
#
#new_comm = comm.Split(color)
#
#new_comm_rank = new_comm.Get_rank()
#new_comm_size = new_comm.Get_size()
#
#if new_comm_rank == 0:
#    data = new_comm.bcast(color, root = 0)
#else:
#    data = new_comm.bcast(None, root = 0)
#    
#print ("old rank:%d new rank:%d data:%d"%(comm_rank, new_comm_rank, data))

#if comm_rank == 0:
#    a = array([[1,2],[3,4],[5, 6]])
#    b = array([[1,2,3], [4, 5, 6]])
#    b = b.transpose()
#else:
#    a = None
#    b = None
#    
#color_row = int(comm_rank / 3)
#color_col = comm_rank % 3
#
#comm_row = comm.Split(color_row)
#comm_col = comm.Split(color_col)
#
#row = comm_col.scatter(a, root = 0) if color_col == 0 else None
#row = comm_row.bcast(row, root = 0) 
#
#col = comm_row.scatter(b, root = 0) if color_row == 0 else None
##print (comm_rank, color_row,col)
#col = comm_col.bcast(col, root = 0)
#
##print(comm_rank, row, col)
#ret = sum([x * y for x, y in zip(row, col)])
#
#c =  comm.gather(ret, root = 0)
#
#if comm_rank == 0:
#    c = array(c).reshape(3,3)
#    print (c)

#if comm_rank == 0:
#    data = array([1,2,3], dtype=int)
##    request = comm.Isend([data, MPI.INT], dest = 1)
#    data = comm.sendrecv(data, dest = 1)
#else:
#    data = zeros(3, dtype = int)
##    request = comm.Irecv([data, MPI.INT], source = 0)
#    data = comm.recv(source=0)
#    cnt = 0
##    while not request.Test():
##        cnt += 1
##        if cnt % 1000 == 0:
##            print ('wait', cnt)
#    if data[1] == 0:
#        print ('wait')
#    print (data)

if comm_rank == 0:
    d = {'mama':1, 'papa':2}
    comm.send(d, dest = 1, tag = 1)
else:
    s = MPI.Status()
    cnt = 0
    while not comm.iprobe(source = 0, tag = 1, status = s):
        cnt+=1
        if cnt % 100 == 0:
            print (cnt)
    data = comm.recv(source=0, tag =1)
    print (data)





