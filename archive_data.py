__author__ = 'johnp80'

from datetime import datetime as dt
import getData


x = getData.TwData("en70")
for file in x.data_files_new:
    x.data_files_new.append((file + str(dt.now())))






