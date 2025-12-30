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
import numpy as np
import re
import os

data_dir = "./archive//ops-log/"
workloads = [
    'log-gc-zoned-fdp',            # PI RU256 OP10
    'log-gc-zoned-RU256OP5',        # PI RU256 OP5
    'log-gc-zoned-RU256OP7',        # PI RU256 OP7
    'log-gc-zoned-RU256OP14',        # PI RU256 OP14

    'log-gc-zoned-RU128OP5',       # PI RU128 OP5
    'log-gc-zoned-RU128OP7',       # PI RU128 OP7
    'log-gc-zoned-RU128OP10',      # PI RU128 OP10
    'log-gc-zoned-RU128OP14',      # PI RU128 OP14

    'log-ii-zoned-RU256OP5',       # II RU256 OP5
    'log-ii-zoned-RU256OP7',
    'log-ii-zoned-RU256OP10',      # II RU256 OP10
    'log-ii-zoned-RU256OP14',      # II RU256 OP10

    'log-ii-zoned-RU128OP5',       # II RU128 OP5
    'log-ii-zoned-RU128OP7',       # II RU128 OP7
    'log-ii-zoned-RU128OP10',      # II RU128 OP10
    'log-ii-zoned-RU128OP14',      # II RU128 OP14
    
    'log-ii-zoned-RU256OP10-AE',      # II RU256 OP10
    'log-ii-zoned-RU256OP14-AE',      # II RU256 OP14
    'log-pi-zoned-RU256OP10-AE',      # PI RU256 OP10
    'log-pi-zoned-RU256OP14-AE',      # PI RU256 OP14
]

# Mapping workload to (op, type, ru)
workload_info = {
    'log-gc-zoned-fdp': ('PI', 256, 10),
    'log-gc-zoned-RU256OP5': ('PI', 256, 5),
    'log-gc-zoned-RU256OP7': ('PI', 256, 7),
    'log-gc-zoned-RU256OP14': ('PI', 256, 14),

    'log-gc-zoned-RU128OP5': ('PI', 128, 5),    
    'log-gc-zoned-RU128OP7': ('PI', 128, 7),
    'log-gc-zoned-RU128OP10': ('PI', 128, 10),
    'log-gc-zoned-RU128OP14': ('PI', 128, 14),

    'log-ii-zoned-RU256OP5': ('II', 256, 5),
    'log-ii-zoned-RU256OP7': ('II', 256, 7),
    'log-ii-zoned-RU256OP10': ('II', 256, 10),
    'log-ii-zoned-RU256OP14': ('II', 256, 14),

    'log-ii-zoned-RU128OP5': ('II', 128, 5),
    'log-ii-zoned-RU128OP7': ('II', 128, 7),
    'log-ii-zoned-RU128OP10': ('II', 128, 10),
    'log-ii-zoned-RU128OP14': ('II', 128, 14),

    'log-ii-zoned-RU256OP10-AE':('II-AE', 256, 10),
    'log-ii-zoned-RU256OP14-AE':('II-AE', 256, 14),
    'log-pi-zoned-RU256OP10-AE': ('PI-AE', 256, 10),
    'log-pi-zoned-RU256OP14-AE': ('PI-AE', 256, 14),
    
}

# Result containers
results = {'PI': {5: [], 7: [], 10: [],14: []}, 'II': {5: [],7: [], 10: [], 14: []}, 'II-AE': {5: [],7: [], 10: [], 14: []}, 'PI-AE': {5: [],7: [], 10: [], 14: []}}

data_field_cnt = 3
this_dev_cap = 224 * (2**30)  # adjust device capacity
this_dev_cap_GB = this_dev_cap / (2**30)

def check_file_existence(data_dir, fname):
    return os.path.exists(os.path.join(data_dir, fname))

#=======
# Initialize data containers
hbmw_data = {}
mbmw_data = {}

x_point = 5

for w in workloads:
    is_ii = 'ii' in w.lower()
    ruhs = [0, 1, 2, 7] if is_ii else [0, 1, 2]
    nruh = len(ruhs)

    hbmw_data[w] = [[-1] for _ in range(nruh)]
    mbmw_data[w] = [[-1] for _ in range(nruh)]

    if not check_file_existence(data_dir, w):
        print(f"File not found: {w}")
        continue

    print(f"Processing: {w}")
    file_path = os.path.join(data_dir, w)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    local_ruh_hbmw = [[] for _ in ruhs]
    local_ruh_mbmw = [[] for _ in ruhs]
    anchor_index = 0
    cnt = 0

    for line in lines:
        line = line.strip().replace(",", "")
        l = re.findall(r'[0-9]+', line)
        l = [int(x) for x in l]
        if len(l) < 3:
            continue

        base = 6
        base_2nd = base + (data_field_cnt * nruh)
        value_hbmw_total = 0

        for idx in range(nruh):
            value_ruh_hbmw = l[base_2nd + idx * data_field_cnt + 1]
            value_hbmw_total += value_ruh_hbmw

        rHMW = value_hbmw_total / this_dev_cap

        if (x_point * (anchor_index + 1) - 0.1 < rHMW <= x_point * (anchor_index + 1) + 0.1):
            for idx in range(nruh):
                value_ruh_hbmw = l[base_2nd + idx * data_field_cnt + 1]
                value_ruh_mbmw = l[base_2nd + idx * data_field_cnt + 2]
                local_ruh_hbmw[idx].append(value_ruh_hbmw)
                local_ruh_mbmw[idx].append(value_ruh_mbmw)
            cnt += 1
        else:
            if cnt >= 1:
                for idx in range(nruh):
                    try:
                        hbmw_val = np.mean(local_ruh_hbmw[idx]) / 2**30
                        mbmw_val = np.mean(local_ruh_mbmw[idx]) / 2**30

                        if ruhs[idx] == 7:
                            hbmw_val = 0  # GC has no host writes

                        hbmw_data[w][idx][anchor_index] = hbmw_val
                        mbmw_data[w][idx][anchor_index] = mbmw_val
                    except IndexError:
                        print("IndexError at workload:", w, "index:", idx)

                cnt = 0
                local_ruh_hbmw = [[] for _ in ruhs]
                local_ruh_mbmw = [[] for _ in ruhs]
                anchor_index += 1

        if anchor_index >= 1:
            break

# hbmw_data and mbmw_data now contain the 5rHMW snapshot for all workloads

#==== 
import matplotlib.pyplot as plt
import numpy as np

plt.rc('xtick', labelsize=MEDIUM_SIZE)
plt.rc('ytick', labelsize=MEDIUM_SIZE)

device_capacity = 224 * 1024 * 1024 * 1024  # bytes
device_capacity_gib = device_capacity / 2**30

for w in workloads:
    config_type, ru, op = workload_info[w]

    ruh_mbmw = []
    ruh_hbmw = []
    is_ii = 'ii' in w.lower()
    ruhs = [0, 1, 2, 7] if is_ii else [0, 1, 2]
    nruh = len(ruhs)
    
    for ruh in range(nruh):
        try:
            val_mbmw = mbmw_data[w][ruh][0]  # at x5 rHMW
            val_hbmw = hbmw_data[w][ruh][0]
        except (IndexError, KeyError):
            continue
        ruh_mbmw.append(val_mbmw)
        ruh_hbmw.append(val_hbmw)

    total_mbmw = sum(ruh_mbmw)
    total_hbmw = sum(ruh_hbmw)
    dlwa_total = total_mbmw / total_hbmw if total_hbmw > 0 else 0

    results[config_type][op].append((ru, dlwa_total))

# Plotting
fig, ax = plt.subplots(1,2 , figsize=(9, 4), sharey=True)

#for config_type, marker, color in zip(['PI', 'II'], ['o', 's'], ['blue', 'green']):
for config_type, marker in zip(['PI', 'II'], ['o', 's']):
    op_list = sorted(results[config_type].keys())
    for ru_size in [256]:
        x_op = []
        y_dlwas = []
        for op in op_list:
            matched = [dlwa for ru, dlwa in results[config_type][op] if ru == ru_size]
            if matched:
                x_op.append(op)
                y_dlwas.append(matched[0])
        if x_op:
            ax[0].plot(x_op, y_dlwas, marker=marker, linestyle='-',
                    label=f'{config_type}, RU{ru_size}')
    for ru_size in [128]:
        x_op = []
        y_dlwas = []
        for op in op_list:
            matched = [dlwa for ru, dlwa in results[config_type][op] if ru == ru_size]
            if matched:
                x_op.append(op)
                y_dlwas.append(matched[0])
        if x_op:
            ax[1].plot(x_op, y_dlwas, marker=marker, linestyle='-',
                    label=f'{config_type}, RU{ru_size}')

#==AE==AE==AE==AE==AE==AE==AE==AE==AE==AE#
#for config_type, marker, color in zip(['PI', 'II'], ['o', 's'], ['blue', 'green']):
for config_type, marker in zip(['PI-AE', 'II-AE'], ['o', 's']):
    op_list = sorted(results[config_type].keys())
    for ru_size in [256]:
        x_op = []
        y_dlwas = []
        for op in op_list:
            matched = [dlwa for ru, dlwa in results[config_type][op] if ru == ru_size]
            if matched:
                x_op.append(op)
                y_dlwas.append(matched[0])
        if x_op:
            ax[0].plot(x_op, y_dlwas, marker=marker, linestyle='-',
                    label=f'{config_type}, RU{ru_size}', color='k')
#==AE==AE==AE==AE==AE==AE==AE==AE==AE==AE#

# Labels and grid
#ax[0].set_title('DLWA vs Overprovisioning % (x5 rHMW)', fontsize=BIGGER_SIZE)
ax[0].set_title('[a] IIvsPI RU256MiB', fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)
ax[1].set_title('[b] IIvsPI RU128MiB', fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)

ax[0].set_xlabel('OP (%)', fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)
ax[1].set_xlabel('OP (%)', fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)

ax[0].set_ylabel('WAF ', fontproperties=helvetica_prop, fontsize=MEDIUM_SIZE)
ax[0].set_ylim([0.9, 2.5])
ax[0].set_xticks([5, 7, 10,14])
ax[0].set_yticks([1, 1.5, 2, 2.5])

ax[0].grid(True, linestyle='--', alpha=0.6)
ax[1].set_xticks([5, 7, 10,14])
ax[1].grid(True, linestyle='--', alpha=0.6)

ax[0].legend(loc = 'upper center', prop=helvetica_prop, edgecolor='k', fancybox=False ,fontsize=MEDIUM_SIZE+4, ncol=2)
ax[1].legend(loc = 'upper center', prop=helvetica_prop, edgecolor='k', fancybox=False ,fontsize=MEDIUM_SIZE+4, ncol=2)

plt.tight_layout()

# Save
#------------------- #
isConference=True
if isConference:
    save_dir = "./"
    fig_name = "fdp_8020_IIvsPI-OPSplot2"
    plt.savefig("{0}{1}.eps".format(save_dir,fig_name))
    plt.savefig("{0}{1}.pdf".format(save_dir,fig_name))
    plt.savefig("{0}{1}.png".format(save_dir,fig_name))
    plt.savefig("{0}{1}.jpeg".format(save_dir,fig_name))
#------------------- #