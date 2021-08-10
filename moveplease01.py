#!/usr/bin/env python3

import shutil
import os


os.chdir("/home/student/mycode/")
# moves file to ceph_storage
shutil.move("raynor.obj", "ceph_storage/")
# getting new name for file from the user
xname = input("what is the new name for the kerrigan.obj? ")
# renames kerrigan file to what user input 
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

