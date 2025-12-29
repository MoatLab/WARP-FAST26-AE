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
    
    #------------------------------------------------------------#
fig, ax = plt.subplots(2,3, figsize=(9,6), sharey=True)
plt.style.use('tableau-colorblind10')
#------------------------------------------------------------#
greedy_colors = {
    "fdp_share/":"#228B22",                    # Money green – deep and rich
    "nofdp/":"#8B0000",              # Power red – intense and dominant
    "nofdp_R256OP20/":"#D4AF37",              # Power red – intense and dominant
    #"#D4AF37",          # Greedy gold – luxurious, eye-catching
    "fdp/":"#00008B"  # DarkBlue – bold, assertive, and wealth-associated
}
cost_benefit_colors = {
    "fdp_share/":"#4ECDC4",  # Benefit – calm teal (gain, positive)
    "nofdp/":"#FF6B6B",  # Cost – soft red (warning, loss)
    #"#FFE66D",  # Neutral – yellow (decision, caution, balance point)
    "fdp/":"#1E90FF"                 # Dodger Blue – vivid, clear, optimistic
}
ae_greedy_colors = {
    "fdp_share/":        "#6BAF6B",  # softened green (derived from #228B22)
    "nofdp/":            "#C65A5A",  # muted red (derived from #8B0000)
    "fdp/":              "#5B6FAE",  # softened dark blue (derived from #00008B)
    
}
#--AE--AE--AE--AE--AE--AE--AE--AE--#

workload= ['zoned/']
subdirs=['fdp/']
data_dir = "./FIO-scripts/3stream/"
TEXT_FONT_SIZE = 24

# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload):
    for j,sdir in enumerate(subdirs):
        filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        dev_cap = 224/1024
        x_cut_lim = 7
        hbmw_list_TB = [ x /dev_cap for x in hbmw_list]
        
        assert (len(waf_list) == len(hbmw_list)) and (len(waf_list) > 0)
        #waf_log_to_waf_lists(data_dir+up+bs,filename )
        #    return [waf_list, hbmw_list , mbmw_list, erase_list]

        #ax2 = ax[i//2][i%2].twinx()
        ax2 = ax[0][2]
        #print(w, sdir, len(hbmw_list_TB))
        ax2.plot(hbmw_list_TB, waf_list, linewidth=5, linestyle='-', alpha=0.8, label="WARP_AE", color=ae_greedy_colors[sdir])
#--AE--AE--AE--AE--AE--AE--AE--AE--#

#------------------------------------------------------------#

workload= ['zipf_2.2/', 'zipf_1.2/', 'zoned/']
subdirs=['nofdp/','fdp_share/','fdp/']
#data_dir = "/data/inho/nvme_fio/Cylon-FDP/warmup_v4/GC_enbaled/PI-GCe/quick/"
data_dir = "./archive/result-FIO/cylon224-PI/GCe/3stream/"
TEXT_FONT_SIZE = 24

# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload):
    for j,sdir in enumerate(subdirs):
        filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        dev_cap = 224/1024
        x_cut_lim = 7
        hbmw_list_TB = [ x /dev_cap for x in hbmw_list]
        
        assert (len(waf_list) == len(hbmw_list)) and (len(waf_list) > 0)
        #waf_log_to_waf_lists(data_dir+up+bs,filename )
        #    return [waf_list, hbmw_list , mbmw_list, erase_list]

        #ax2 = ax[i//2][i%2].twinx()
        ax2 = ax[0][i]
        #print(w, sdir, len(hbmw_list_TB))
        ax2.plot(hbmw_list_TB, waf_list, linewidth=3, linestyle='--', alpha=0.8, label="Greedy_"+sdir.replace('/','').replace('_',' '), color=greedy_colors[sdir])
#------------------------------------------------------------#

workload= ['zipf_2.2/', 'zipf_1.2/', 'zoned/']
subdirs=['fdp/', 'nofdp/', 'fdp_share/']
#data_dir = "/data/inho/nvme_fio/Cylon-FDP/warmup_v4/GC_enbaled/PI-GCcb/quick/"
data_dir = "./archive/result-FIO/cylon224-PI/GCcb/"
#print(bbss)
# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload):
    for j,sdir in enumerate(subdirs):
        filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        dev_cap = 224/1024
        x_cut_lim = 5
        hbmw_list_TB = [ x/dev_cap for x in hbmw_list]
        
        assert (len(waf_list) == len(hbmw_list)) and (len(waf_list) > 0)
        #waf_log_to_waf_lists(data_dir+up+bs,filename )
        #    return [waf_list, hbmw_list , mbmw_list, erase_list]
        ax2 = ax[0][i]
        #print(w, sdir, len(hbmw_list_TB))
        ax2.plot(hbmw_list_TB, waf_list, linewidth=2,  label="CB_"+sdir.replace('/','').replace('_',' '), color=cost_benefit_colors[sdir])
        #ax2.set_title("{0}".format(w.replace('/', ' ')), fontsize=BIGGER_SIZE)

        hop=2
        a=0.8
        my_waf_text_index = get_waf_by_aligned_hbmw(data_dir+w+sdir, dev_cap, filename, x_cut_lim)

        if (re.match(sdir,"nofdp/") ) :
            #ax2.plot(range(0,len(waf_list)), waf_list, linewidth=0.1, color='red', marker='o', markersize=1, label=t_labels[j], alpha=0.5)
            #ax2.plot(hbmw_list_TB, waf_list, linewidth=1, marker='o', markersize=1, label=t_labels[j], alpha=0.5, color='red')
            for k, v in enumerate(my_waf_text_index[::hop]):
                if k>0:
                    ax2.text(k*hop, v, " " , ha="center", fontsize=0.1, bbox=dict(facecolor=cost_benefit_colors[sdir], alpha=0.8))
        
        elif (re.match(sdir,"fdp/") ) :
            for k, v in enumerate(my_waf_text_index[::hop]):
                # #Text
                # ax2.text(k*hop+a, v-0.05, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE)
                # #Box
                # ax2.text(k*hop, v, " " , ha="center", fontsize=0.1, bbox=dict(facecolor=cost_benefit_colors[sdir], alpha=0.8))
                ax2.text(k*hop, v, " " , ha="center", fontsize=0.1, bbox=dict( fc=cost_benefit_colors[sdir], ec="k", alpha=0.8))

        elif (re.match(sdir,"fdp_share/") ) :
            for k, v in enumerate(my_waf_text_index[::hop]):
                if k>0 :
                    #Text
                    #ax2.text(k*hop+a+0.1, v-0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE)
                    #Box
                    ax2.text(k*hop, v, " " , ha="center", fontsize=0.1, bbox=dict(facecolor=cost_benefit_colors[sdir], alpha=0.8))

#------------------------------------------------------------#
greedy_colors = {
    "fdp_share/":"#228B22",                    # Money green – deep and rich
    "nofdp/":"#8B0000",              # Power red – intense and dominant
    #"#D4AF37",          # Greedy gold – luxurious, eye-catching
    "fdp/":"#00008B"  # DarkBlue – bold, assertive, and wealth-associated
}
cost_benefit_colors = {
    "fdp_share/":"#4ECDC4",  # Benefit – calm teal (gain, positive)
    "nofdp/":"#FF6B6B",  # Cost – soft red (warning, loss)
    #"#FFE66D",  # Neutral – yellow (decision, caution, balance point)
    "fdp/":"#1E90FF"                 # Dodger Blue – vivid, clear, optimistic
}
workload= ['zipf_2.2/', 'zipf_1.2/', 'zoned/']
subdirs=['fdp/', 'nofdp/', 'fdp_share/']
#data_dir = "/data/inho/nvme_fio/Cylon-FDP/warmup_v4/GC_enbaled/PI-GCe/"
data_dir ="./archive/result-FIO/warpb-cylon224-PI/GCe/3stream/"

TEXT_FONT_SIZE = 24

# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload):
    for j,sdir in enumerate(subdirs):
        filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        dev_cap = 224/1024
        hbmw_list_TB = [ x /dev_cap for x in hbmw_list]
        
        assert (len(waf_list) == len(hbmw_list)) and (len(waf_list) > 0)

        ax2 = ax[1][i]
        #print(w, sdir, len(hbmw_list_TB))
        ax2.plot(hbmw_list_TB, waf_list, linewidth=3, linestyle='--', alpha=0.8, label="Greedy_"+sdir.replace('/','').replace('_',' '), color=greedy_colors[sdir])
        ax2.set_title("{0}".format(w.replace('/', ' ')), fontsize=BIGGER_SIZE)

        hop=2
        a=0.8
        my_waf_text_index = get_waf_by_aligned_hbmw(data_dir+w+sdir, dev_cap, filename, x_cut_lim)
#------------------------------------------------------------#
workload= ['zipf_2.2/', 'zipf_1.2/', 'zoned/']
subdirs=['fdp/', 'nofdp/', 'fdp_share/']
#data_dir = "/data/inho/nvme_fio/Cylon-FDP/warmup_v4/GC_enbaled/PI-GCcb/"
data_dir ="./archive/result-FIO/warpb-cylon224-PI/GCcb/3stream/"
#util = ['{0}/'.format(x*100) for x in np.arange(1,6) ]
#bbss = ['{0}K/'.format(4**x) for x in np.arange(1,5)]
#print(bbss)
# --------------------------- Figure ------------------------ # 
for i, w in enumerate(workload):
    for j,sdir in enumerate(subdirs):
        filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir+w+sdir,filename)
        if (ret == 0):
            continue
        info_list = waf_log_to_waf_lists(data_dir+w+sdir)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        mbmw_list= info_list[2] 
        erase_list= info_list[3] 
        dev_cap = 224/1024
        hbmw_list_TB = [ x/dev_cap for x in hbmw_list]
        
        assert (len(waf_list) == len(hbmw_list)) and (len(waf_list) > 0)
        #waf_log_to_waf_lists(data_dir+up+bs,filename )
        #    return [waf_list, hbmw_list , mbmw_list, erase_list]
        ax2 = ax[1][i]
        #print(w, sdir, len(hbmw_list_TB))
        ax2.plot(hbmw_list_TB, waf_list, linewidth=2,alpha=0.8, label="CB_"+sdir.replace('/','').replace('_',' '), color=cost_benefit_colors[sdir])

        my_waf_text_index = get_waf_by_aligned_hbmw(data_dir+w+sdir, dev_cap, filename, x_cut_lim)
        if (re.match(sdir,"nofdp/") ) :
            for k, v in enumerate(my_waf_text_index[::hop]):
                ax2.text(k*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor=cost_benefit_colors[sdir], alpha=0.8))
        
        elif (re.match(sdir,"fdp/") ) :
            for k, v in enumerate(my_waf_text_index[::hop]):
                #Text
                # if k> 0:
                #     ax2.text(k*hop+a+0.1, v-0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE)
                #Box
                ax2.text(k*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor=cost_benefit_colors[sdir], alpha=0.8))
                #ax2.text(k*hop, v, " " , ha="center",  fontsize=5, bbox=dict(boxstyle='circle', fc=cost_benefit_colors[sdir], ec="k", alpha=0.8))

        elif (re.match(sdir,"fdp_share/") ) :
            for k, v in enumerate(my_waf_text_index[::hop]):
                #Text
                # ax2.text(k*hop+a+0.1, v-0.1, "%.2f" %v, ha="center", fontsize=TEXT_FONT_SIZE)
                #Box
                ax2.text(k*hop, v, " " , ha="center", fontsize=0.01, bbox=dict(facecolor=cost_benefit_colors[sdir], alpha=0.8))

#------------------------------------------------------------#
MEDIUM_PLUS_SIZE=MEDIUM_SIZE+2

# Collect handles and labels from the full figure
handles, labels = ax[0][2].get_legend_handles_labels()

# Split into two groups (first 3 and last 3, adjust as needed)
handles1, labels1 = handles[:3], labels[:3]
handles2, labels2 = handles[3:], labels[3:]

# Rename labels (example)
labels1 = ["WARP_AE_FDP", "Greedy_NoFDP", "Greedy_mixedFDP", "Greedy_FDP"]
labels2 = ["CB_NoFDP", "CB_mixedFDP", "CB_FDP"]

# Place legends in different axes
ax[0][0].legend(handles2, labels2, loc="upper left", frameon=True, prop=helvetica_prop, fontsize=MEDIUM_SIZE , edgecolor='k' , fancybox=False)
ax[0][1].legend(handles1, labels1, loc="upper left", frameon=True, prop=helvetica_prop, fontsize=MEDIUM_SIZE , edgecolor='k' , fancybox=False)


ax[0][0].set_ylabel("WAF", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)
ax[1][0].set_ylabel("WAF", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)

#fig.text(0.34, 0.01,  r'Written Data Volume', fontsize=MEDIUM_SIZE+2)
ax[1][1].set_xlabel(r'Written Data Volume', fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)

ax[0][0].set_title(r"[a] WARP$_{A}$ zipf. 2.2", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)
ax[0][1].set_title(r"[b] WARP$_{A}$ zipf. 1.2", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)
ax[0][2].set_title(r"[c] WARP$_{A}$ 80/20", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)
ax[1][0].set_title(r"[d] WARP$_{B}$ zipf. 2.2", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)
ax[1][1].set_title(r"[e] WARP$_{B}$ zipf. 1.2", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)
ax[1][2].set_title(r"[f] WARP$_{B}$ 80/20", fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)


for i in range(2):
    for j in range(3):
        ax2 = ax[i][j]
        ax2.tick_params(axis='x', which='minor', direction='in')
        ax2.tick_params(axis='y', which='minor', direction='in')
        ax2.minorticks_on()
        ax2.set_xlim([0,5])
        ax2.set_ylim([0.9 , 4.0])
        ax2.set_xticks([0,2,4])
        labels = [label.get_text() for label in ax2.get_xticklabels()]
        ax2.set_xticklabels([f"x{t}" for t in labels], fontproperties=helvetica_prop, fontsize=MEDIUM_PLUS_SIZE)

ax[0][0].set_yticks([1, 2, 3, 4])
ax[1][0].set_yticks([1, 2, 3, 4])


fig.tight_layout(rect=[0, 0.02, 1, 1])

#------------------------#
isConference = True
if (isConference) :
    save_dir = "./"
    fig_name = "3stream_WARP_AE"
    #plt.savefig("{0}{1}.eps".format(save_dir,fig_name) ) #, dpi=100)
    plt.savefig("{0}{1}.pdf".format(save_dir,fig_name) ) #, dpi=100)
    plt.savefig("{0}{1}.png".format(save_dir,fig_name) ) #, dpi=100)
    plt.savefig("{0}{1}.jpeg".format(save_dir,fig_name)) #, dpi=100)
#------------------------#
plt.show()
