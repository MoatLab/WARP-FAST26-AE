import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
import seaborn as sns 
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import re 
import sys
import os
import collections
from inho_parser import * 
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
import seaborn as sns 
from matplotlib import pyplot as plt
import matplotlib as mpl
import pandas as pd
import re 
import sys
import os
import collections
import inho_parser
from inho_parser import * 
from math import *
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 24

# ----------------------- Regular Expr. ------------------------- #
output_re=re.compile(r'.*_output')
num_re=re.compile(r'[0-9]+')
hbmw_re=re.compile(r'.*(HBMW)')
mbmw_re=re.compile(r'.*(MBMW)')
mbe_mre=re.compile(r'.*(MBE)')
mbe_re=re.compile(r'.*(MBE)')

total_bw_re=re.compile(r'.*READ: bw=')
nvme_iostat_re=re.compile(r'nvme1n1')
#write_bw_re=re.compile()
# ----------------------- Figure Expr. ------------------------- #

SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=MEDIUM_SIZE)  # fontsize of the figure title
mpl.rcParams['savefig.pad_inches'] = 0
isConference=True

dev_list = []
re_dev=re.compile(r'^FADU-FDP+|^Samsung+')
#%ls './FEMU/'

def first_available_font(candidates):
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name
    return None

def get_per_ruh_waf_to_dict (data_dir, filename=None, verbose=None):
    # ----------------------- Regular Expr. ------------------------- #
    ruh_re=re.compile(r'^Reclaim Unit Handle.*')
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
    if verbose is None : 
        verbose = False
    # ---------------------------------------------------------------- #

    ruh_waf = {} 
    waf_data = data_dir+filename
    file1 = open(waf_data, 'r')
    Lines = file1.readlines()
    start_h = None
    start_d = None
    start_e = None
    for line in Lines:
        line = ''.join(line).strip().replace(",", '')
        if ruh_re.match(line) :
            l = num_re.findall(line)
            ruhid = int(l[0])
            hbmw = int(l[3])
            mbmw = int(l[4])
            if (ruhid == 0) or (ruhid == 1) or (ruhid == 2) or (ruhid == 15)or (ruhid == 7):
                if (hbmw == 0) or (mbmw == 0):
                    #print (ruhid , 1.0)
                    if not (ruhid in ruh_waf):
                        ruh_waf[ruhid] = [float(1.0)]
                    else:
                        ruh_waf[ruhid].append(float(1.0))
                else:
                    #print(ruhid, mbmw/hbmw)
                    if not (ruhid in ruh_waf):
                        ruh_waf[ruhid] = [mbmw/hbmw]
                    else:
                        ruh_waf[ruhid].append(float(mbmw/hbmw))
    if not (verbose):
        for key in ruh_waf.keys():
            print(key, ruh_waf[key][-1] )
            #ax[i].plot(range(len(ruh_waf[key])), ruh_waf[key] , label = key)
            #ax[i].set_ylim([0.99, 4.0])
            #ax[i].set_title(t)

    return ruh_waf

def get_per_ruh_mb_to_list (data_dir, filename=None, verbose=None):
    # ----------------------- Regular Expr. ------------------------- #
    ruh_re=re.compile(r'^Reclaim Unit Handle.*')
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
    if verbose is None : 
        verbose = False
    # ---------------------------------------------------------------- #

    ruh_waf = {} 
    ruh_hbmw = {}
    ruh_mbmw = {}
    waf_data = data_dir+filename
    file1 = open(waf_data, 'r')
    Lines = file1.readlines()
    start_h = None
    start_d = None
    start_e = None
    for line in Lines:
        line = ''.join(line).strip().replace(",", '')
        if ruh_re.match(line) :
            l = num_re.findall(line)
            ruhid = int(l[0])
            hbmw = int(l[3])
            mbmw = int(l[4])
            if (ruhid == 0) or (ruhid == 1)or (ruhid == 2) or (ruhid == 15)or (ruhid == 7):
                if (hbmw == 0) or (mbmw == 0):
                    #print (ruhid , 1.0)
                    if not (ruhid in ruh_hbmw):
                        #ruh_waf[ruhid] = [float(1.0)]
                        ruh_hbmw[ruhid] = [int(0)]
                        ruh_mbmw[ruhid] = [int(0)]
                    else:
                        #ruh_waf[ruhid].append(float(1.0))
                        ruh_hbmw[ruhid].append(int(0))
                        ruh_mbmw[ruhid].append(int(0))
                else:
                    #print(ruhid, mbmw/hbmw)
                    if not (ruhid in ruh_hbmw):
                        #ruh_waf[ruhid] = [mbmw/hbmw]
                        ruh_hbmw[ruhid] = [int(0)]
                        ruh_mbmw[ruhid] = [int(0)]
                    else:
                        #ruh_waf[ruhid].append(float(mbmw/hbmw))
                        ruh_hbmw[ruhid].append(hbmw)
                        ruh_mbmw[ruhid].append(mbmw)
    if not (verbose):
        for key in ruh_waf.keys():
            print(key, ruh_waf[key][-1] )
            #ax[i].plot(range(len(ruh_waf[key])), ruh_waf[key] , label = key)
            #ax[i].set_ylim([0.99, 4.0])
            #ax[i].set_title(t)

    return [ruh_hbmw,ruh_mbmw]

def get_per_ruh_waf_to_list (data_dir, subdir, filename=None, verbose=None):
    # ---------------------------------------------------------------- #
    if filename is None:
        filename = "samsung_waf_1sec.txt"
    # ---------------------------------------------------------------- #
    per_ruh_waf_list = []

    for i,t in enumerate(subdir):
        per_ruh_waf_list.append(get_per_ruh_waf_to_dict(data_dir+t, filename=None))
        print(t)

    
    return per_ruh_waf_list


# Prefer Arial; otherwise use Liberation Sans, then Lato, then DejaVu Sans
math_family = first_available_font(['Arial', 'Liberation Sans', 'Lato', 'DejaVu Sans'])
if math_family is None:
    print("WTF DejaVu Sans")
    math_family = 'DejaVu Sans'  # last-resort

# Make mathtext use the chosen family (instead of DejaVu fallback)
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = math_family
mpl.rcParams['mathtext.it'] = f'{math_family}:italic'
mpl.rcParams['mathtext.bf'] = f'{math_family}:bold'

# Try to use Helvetica or fallback to similar fonts
# Step 1: Provide full path to Helvetica.ttc
# Load Helvetica.ttc manually
font_path = "./archive/Helvetica.ttc"
helvetica_prop = fm.FontProperties(fname=font_path)
# Step 1: Manually load Helvetica.ttc
font_path = './archive/Helvetica.ttc'
helvetica_font = fm.FontProperties(fname=font_path)
font_name = helvetica_font.get_name()

# Step 2: Add to font manager cache
fm.fontManager.addfont(font_path)

# Step 3: Now set as default
mpl.rcParams['font.family'] = font_name
mpl.rcParams['font.family'] = helvetica_prop.get_name()


#!pip3 install IPython
import IPython
from IPython.display import Image
import os
from colorama import Fore, Style

def check_file_existence(directory, filename=None):
    if(filename == None):
        filename = "samsung_waf_1sec.txt"
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        print(f"{Fore.GREEN}[Check!]{Style.RESET_ALL} {file_path}")
        return 1
    else:
        print(f"{Fore.RED}['No such file/dir']{Style.RESET_ALL} {file_path}")
        return 0 

from inho_parser import * 
#------------------------------------------------------------#
mpl.rcParams['savefig.pad_inches'] = 0
fig, ax = plt.subplots(1,4, figsize=(10,3), sharey=True)
plt.style.use('tableau-colorblind10')
#------------------------------------------------------------#

def first_available_font(candidates):
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name
    return None

# Prefer Arial; otherwise use Liberation Sans, then Lato, then DejaVu Sans
math_family = first_available_font(['Arial', 'Liberation Sans', 'Lato', 'DejaVu Sans'])
if math_family is None:
    print("WTF DejaVu Sans")
    math_family = 'DejaVu Sans'  # last-resort

# Make mathtext use the chosen family (instead of DejaVu fallback)
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = math_family
mpl.rcParams['mathtext.it'] = f'{math_family}:italic'
mpl.rcParams['mathtext.bf'] = f'{math_family}:bold'

MEDIUM_PLUS_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_PLUS_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_PLUS_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=MEDIUM_SIZE)  # fontsize of the figure title

# Try to use Helvetica or fallback to similar fonts
# Step 1: Provide full path to Helvetica.ttc
# Load Helvetica.ttc manually
font_path = "./archive/Helvetica.ttc"
helvetica_prop = fm.FontProperties(fname=font_path)
# Step 1: Manually load Helvetica.ttc
font_path = './archive/Helvetica.ttc'
helvetica_font = fm.FontProperties(fname=font_path)
font_name = helvetica_font.get_name()

# Step 2: Add to font manager cache
fm.fontManager.addfont(font_path)

# Step 3: Now set as default
mpl.rcParams['font.family'] = font_name
mpl.rcParams['font.family'] = helvetica_prop.get_name()

#------------------------------------------------------------#


#fdev="Samsung-FDP-PM9D3a-MZWL67T6HBLC-7.68TB-PCIeGen5/"
#fdev=
workload4= ['zipf_2.2/', 'zipf_1.2/', 'zoned/' , 'uniform/']
subdirs=[ 'nofdp/','fdp_share/','fdp/' ] 
labeld =[ 'NoFDP', 'mixedFDP' ,'FDP' ]
data_dir = "./archive/result-FIO/cylon448-II/3syn/"
TEXT_FONT_SIZE = MEDIUM_SIZE

#util = ['{0}/'.format(x*100) for x in np.arange(1,6) ]
#bbss = ['{0}K/'.format(4**x) for x in np.arange(1,5)]
#print(bbss)
# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload4):
    for j,sdir in enumerate(subdirs):
        # ------------------ Reading results -------------------#
        filename="samsung_waf_1sec.txt"

        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir,filename)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        this_dev_cap_TB= 448/1024
        hbmw_list_TB = [ x / this_dev_cap_TB for x in hbmw_list]
        # if (w == 'necsst02zipf_1.2/zipf_1.2/') and (sdir == 'fdp/'):
        #     l = len(hbmw_list_TB)
        #     cn = int(l/3)
        #     hbmw_list_TB = hbmw_list_TB[:cn]
        #     waf_list = waf_list[:cn]

        #print( len(waf_list), len(hbmw_list) )
        assert (len(waf_list) == len(hbmw_list_TB)) and (len(waf_list) > 0)
        x_cut_lim = 7
        lim=len(hbmw_list_TB)
        for k, hb in enumerate(hbmw_list_TB):
            if hb >= x_cut_lim:
                lim = k
                break
        hbmw_list_TB = hbmw_list_TB[:lim]
        waf_list = waf_list[:lim]
        # --------------------------------------------------- # 

        # ------------------ Plotting -------------------#
        ax2 = ax[i]
        if (sdir=='nofdp/'):
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2,  label=labeld[j], color='red')
        elif (sdir == 'fdp_share/'):
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2,  label=labeld[j], color='green')
        elif (sdir == 'fdp/'):
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2, label=labeld[j], color='blue')
        else:
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2, label=w+sdir)
        #ax2.set_title(" {0}".format(w))
        #ax2.set_ylim([0.9 , 4.0])

        ax2.set_ylim([0.9,4.2])
        # --------------------------------------------------- # 

        # ------------------ texting on fig -------------------#
        #ax2.legend()
        hop=4
        a=0.5
        my_waf_text_index = get_waf_by_aligned_hbmw(data_dir+w+sdir, this_dev_cap_TB, filename, x_cut_lim)
        if re.match(w, "zipf_2.2/") != None:
            if (re.match(sdir,"nofdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    if j > 0:
                        ax2.text(j*hop-a, v+0.1, "%.2f" %v, ha="center", rotation=-45,fontsize=TEXT_FONT_SIZE, color='red', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='red', alpha=0.8))
            elif (re.search(sdir,"fdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    ax2.text(j*hop+a, v+0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='blue', rotation=45, fontproperties=helvetica_prop)
                    #ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
            elif (re.search(sdir,"fdp_share/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #if j > 0:
                    #    ax2.text(j*hop+a, v-0.2, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='green', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='green', alpha=0.8))

        else:
            if (re.match(sdir,"nofdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    if j > 0:
                        ax2.text(j*hop- 2*a, v+0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='red', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='red', alpha=0.8))
            elif (re.search(sdir,"fdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    ax2.text(j*hop+a, v+0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='blue', rotation=45, fontproperties=helvetica_prop)
                    #ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
            elif (re.search(sdir,"fdp_share/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #if j > 0:
                    #    ax2.text(j*hop+a, v-0.2, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='green', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='green', alpha=0.8))

        # for j, v in enumerate(waf_list[::20000]):
        #     ax2.text(hbmw_list_TB[j*20000], v+0.01, "%.2f" %v, ha="center", fontsize=12, rotation=45)
        # --------------------------------------------------- # 
        # ------------------ adjusting each fig -------------------#
        #ax2.grid(which='major', axis='both', linestyle='--')
        # --------------------------------------------------------- # 

#------------------------------------------------------------#


#fdev="Samsung-FDP-PM9D3a-MZWL67T6HBLC-7.68TB-PCIeGen5/"
#fdev=
workload4= ['zipf_2.2/', 'zipf_1.2/', 'zoned/' , 'uniform/']
subdirs=[ 'fdp/' ] 
labeld =[ 'FDP' ]
data_dir = "./FIO-scripts/WARP_A2/3stream/"
TEXT_FONT_SIZE = MEDIUM_SIZE

#util = ['{0}/'.format(x*100) for x in np.arange(1,6) ]
#bbss = ['{0}K/'.format(4**x) for x in np.arange(1,5)]
#print(bbss)
# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload4):
    for j,sdir in enumerate(subdirs):
        # ------------------ Reading results -------------------#
        filename="samsung_waf_1sec.txt"

        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir,filename)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        this_dev_cap_TB= 448/1024
        hbmw_list_TB = [ x / this_dev_cap_TB for x in hbmw_list]

        #print( len(waf_list), len(hbmw_list) )
        assert (len(waf_list) == len(hbmw_list_TB)) and (len(waf_list) > 0)
        x_cut_lim = 7
        lim=len(hbmw_list_TB)
        for k, hb in enumerate(hbmw_list_TB):
            if hb >= x_cut_lim:
                lim = k
                break
        hbmw_list_TB = hbmw_list_TB[:lim]
        waf_list = waf_list[:lim]
        # --------------------------------------------------- # 

        # ------------------ Plotting -------------------#
        ax2 = ax[i]
        if (sdir=='nofdp/'):
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2,  label=labeld[j], color='red')
        elif (sdir == 'fdp_share/'):
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2,  label=labeld[j], color='green')
        elif (sdir == 'fdp/'):
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2, label='WARP_A2-AE', color='k')
        else:
            ax2.plot(hbmw_list_TB, waf_list, linewidth=2, label=w+sdir)
        #ax2.set_title(" {0}".format(w))
        #ax2.set_ylim([0.9 , 4.0])

        ax2.set_ylim([0.9,4.2])
        # --------------------------------------------------- # 

        # ------------------ texting on fig -------------------#
        #ax2.legend()
        hop=4
        a=0.5
        my_waf_text_index = get_waf_by_aligned_hbmw(data_dir+w+sdir, this_dev_cap_TB, filename, x_cut_lim)
        if re.match(w, "zipf_2.2/") != None:
            if (re.match(sdir,"nofdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    if j > 0:
                        ax2.text(j*hop-a, v+0.1, "%.2f" %v, ha="center", rotation=-45,fontsize=TEXT_FONT_SIZE, color='red', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='red', alpha=0.8))
            elif (re.search(sdir,"fdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    ax2.text(j*hop+a, v+0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='k', rotation=45, fontproperties=helvetica_prop)
                    #ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
            elif (re.search(sdir,"fdp_share/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #if j > 0:
                    #    ax2.text(j*hop+a, v-0.2, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='green', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='green', alpha=0.8))

        else:
            if (re.match(sdir,"nofdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    if j > 0:
                        ax2.text(j*hop- 2*a, v+0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='red', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='red', alpha=0.8))
            elif (re.search(sdir,"fdp/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12, rotation=45)
                    #ax2.text(j, v+0.1, "%.2f" %v, ha="center", fontsize=12)
                    ax2.text(j*hop+a, v+0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='blue', rotation=45, fontproperties=helvetica_prop)
                    #ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='blue', alpha=0.8))
            elif (re.search(sdir,"fdp_share/")!=None) :
                for j, v in enumerate(my_waf_text_index[::hop]):
                    #if j > 0:
                    #    ax2.text(j*hop+a, v-0.2, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE, color='green', fontproperties=helvetica_prop)
                    ax2.text(j*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor='green', alpha=0.8))



# --------------------------------------------------- # 
ax[0].set_ylabel("WAF", fontproperties=helvetica_prop , fontsize=MEDIUM_SIZE+2)

# Collect handles and labels from the full figure
handles, labels = ax[2].get_legend_handles_labels()

# Split into two groups (first 3 and last 3, adjust as needed)
handles1, labels1 = handles[:1], labels[:1]
handles2, labels2 = handles[1:2], labels[1:2]
handles3, labels3 = handles[2:], labels[2:]

# Rename labels (example)
#labels1 = ["Greedy_noFDP", "Greedy_FDPshare", "Greedy_FDP"]
#labels2 = ["CB_noFDP", "CB_FDPshare", "CB_FDP"]

# Place legends in different axes
ax[0].legend(handles1, labels1, prop=helvetica_prop, loc="upper left", frameon=True, fontsize=MEDIUM_SIZE ,fancybox=False, edgecolor='k')
ax[1].legend(handles2, labels2, prop=helvetica_prop, loc="upper left", frameon=True, fontsize=MEDIUM_SIZE ,fancybox=False, edgecolor='k')
ax[2].legend(handles3, labels3, prop=helvetica_prop, loc="upper left", frameon=True, fontsize=MEDIUM_SIZE ,fancybox=False, edgecolor='k')
#ax[3].legend(handles3, labels3, prop=helvetica_prop, loc="upper left", frameon=True, fontsize=MEDIUM_SIZE ,fancybox=False, edgecolor='k')


# Example: append 'x' to each
ax[0].set_title("[a] zipf2.2", fontproperties=helvetica_prop , fontsize=MEDIUM_SIZE)
ax[1].set_title("[b] zipf1.2", fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)
ax[2].set_title("[c] 8020", fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)
ax[3].set_title("[d] uniform", fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)

fig.text(0.403, 0.05, 'Written Data Volume', fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE+2)

for i in range(4):
    ax2= ax[i]
    ax2.set_xlim([0,5])
    ax2.set_ylim([0.9,4])
    ax2.set_xticks([0,2,4])
    labels = [label.get_text() for label in ax2.get_xticklabels()]
    ax2.set_xticklabels([f"x{t}" for t in labels], fontproperties=helvetica_prop , fontsize = MEDIUM_SIZE+2 )

ax2.set_yticks([1,2,3,4])

#fig.suptitle("sLFS uniform: vendorA", fontsize=MEDIUM_SIZE)
#fig.suptitle(r'X-axis : $\mathrm{Relative HMW} = \frac{\mathrm{Host\ Media\ Written}}{ Dev. Cap.(=7.68\ \mathrm{TiB})}$', fontsize=MEDIUM_SIZE, va='bottom')

fig.tight_layout(rect=[0, 0.1, 1, 1])

# ------------------- #
save_dir = "./"
fig_name = "3Syn_CylonA2"
plt.savefig("{0}{1}.eps".format(save_dir,fig_name)  ) #, dpi=100)
plt.savefig("{0}{1}.pdf".format(save_dir,fig_name)  ) #, dpi=100)
plt.savefig("{0}{1}.png".format(save_dir,fig_name)  ) #, dpi=100)
plt.savefig("{0}{1}.jpeg".format(save_dir,fig_name) ) #, dpi=100)
# ------------------- #
