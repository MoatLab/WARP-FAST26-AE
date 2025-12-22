import os
import re
import collections
import numpy as np
from colorama import Fore, Style

num_re=re.compile(r'[0-9]+')
rw_re=re.compile(r'[0-9]+')
total_bw_re=re.compile(r'[0-9]+')

# --------Latency:Simple---------- #
def get_latency_9999th(line):
    num_re=re.compile(r'[0-9]+')
    lat_re=re.compile(r'99.90th=[')

def get_latency_999th(line):
    num_re=re.compile(r'[0-9]+')
    lat_re=re.compile(r'99.99th=[')

# --------BW:Simple---------- #
def get_bandwidth_total(line):
    num_re=re.compile(r'[0-9]+')
    lat_re=re.compile(r'\bWRITE: bw=')
    l=[]
    if (lat_re.match(line)):
        l = num_re.findall(line)
        return int(l[0])

def output_interpreter(file):
    Lines = file.readlines()
    for line in Lines:
        num_re=re.compile(r'[0-9]+')
        total_bw_re=re.compile(r'.*WRITE: bw=')
        
        if (total_bw_re.match(line)):
            l=[]
            l = num_re.findall(line)
            #print(int(l[0]))
            return int(l[0])
        
# -------- log file parser ---------- #
def log_file_to_list(data_dir, file):
    file1 = open(data_dir+"/"+file, 'r')
    Lines = file1.readlines()
    num_re=re.compile(r'[0-9]+')
    l =[]
    ll = []
    for lines in Lines:
        num_re=re.compile(r'[0-9]+')
        ll = num_re.findall(lines)
        l.append(ll[1])
    return l
    
def log_file_devlist_bw(data_dir):
    #1threadQD1024_16Krandwrite_bw.1.log
    logbw_re=re.compile(r'([0-9]+threadQD[0-9]+_[0-9]+Kwrite_bw\.[0-9]+\.log|[0-9]+threadQD[0-9]+_[0-9]+Krandwrite_bw\.[0-9]+\.log)')
    #loglat_re=re.compile(r'\w+_r[0-9]_lat\.[0-9]+\.log')
    target_file_names=[]
    loglist = []
    datalist=[]
    L = os.listdir(data_dir)
    L.sort()
    for l in L: 
        if(logbw_re.match(l)):
            #n = num_re.findall(l)
            target_file_names.append(l)

    for f in target_file_names:
        print(f)
        datalist.append(log_file_to_list(data_dir,f))

    return datalist

def log_file_devlist_lat(data_dir):
    #1threadQD1024_16Krandwrite_bw.1.log
    logbw_re=re.compile(r'([0-9]+threadQD[0-9]+_[0-9]+Kwrite_bw\.[0-9]+\.log|[0-9]+threadQD[0-9]+_[0-9]+Krandwrite_bw\.[0-9]+\.log)')
    loglat_re=re.compile(r'([0-9]+threadQD[0-9]+_[0-9]+Kwrite_lat\.[0-9]+\.log|[0-9]+threadQD[0-9]+_[0-9]+Krandwrite_lat\.[0-9]+\.log)')

    target_file_names=[]
    loglist = []
    datalist=[]
    L = os.listdir(data_dir)
    L.sort()
    for l in L: 
        if(loglat_re.match(l)):
            #n = num_re.findall(l)
            #print(l)
            target_file_names.append(l)
    for f in target_file_names:
        datalist.append(log_file_to_list(data_dir,f))

    return datalist

# -------- output file parser ---------- #

def output_to_dictionarylist_lat(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_nsec_lat_re=re.compile(r'    clat \(nsec')
    total_usec_lat_re=re.compile(r'    clat \(usec')
    total_msec_lat_re=re.compile(r'    clat \(msec')
    target_file_names={}
    d_min = {}
    d_max = {}
    d_avg = {}
    d_stdev={}
    
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            target_file_names[int(n[1])]=l
        
    #target_file_names
    #print(target_file_names)
    for key, file in target_file_names.items():
        #print(key, file)
        file1 = open(data_dir+file, 'r')
        Lines = file1.readlines()
        for line in Lines:
            #line = ''.join(line).strip()
            num_re=re.compile(r'[0-9]+')
            if (total_usec_lat_re.match(line)):
                #print(line)
                l = num_re.findall(line)
                if ((key not in d)):
                    d_min[key] = []
                    d_max[key] = []
                    d_avg[key] = []
                    d_stdev[key] = []
                #print(line)
                #print(l)
                d_min[key].append(int(l[0]))
                d_max[key].append(int(l[1]))
                d_avg[key].append(int(l[2]))
                d_stdev[key].append(int(l[4]))
            elif (total_nsec_lat_re.match(line)):
                l = num_re.findall(line)
                if ((key not in d)):
                    d_min[key] = []
                    d_max[key] = []
                    d_avg[key] = []
                    d_stdev[key] = []
                #print(line)
                #print(l)
                d_min[key].append(int(l[0])/1000)
                d_max[key].append(int(l[1])/1000)
                d_avg[key].append(int(l[2])/1000)
                d_stdev[key].append(int(l[4])/1000)
            elif (total_msec_lat_re.match(line)):
                l = num_re.findall(line)
                if ((key not in d)):
                    d_min[key] = []
                    d_max[key] = []
                    d_avg[key] = []
                    d_stdev[key] = []
                #print(line)
                #print(l)
                d_min[key].append(int(l[0])*1000)
                d_max[key].append(int(l[1])*1000)
                d_avg[key].append(int(l[2])*1000)
                d_stdev[key].append(int(l[4])*1000)
        
                
    orderlist=[]
    orderlist.append(collections.OrderedDict(sorted(d_min.items())))
    orderlist.append(collections.OrderedDict(sorted(d_max.items())))
    orderlist.append(collections.OrderedDict(sorted(d_avg.items())))
    orderlist.append(collections.OrderedDict(sorted(d_stdev.items())))
    
    return orderlist

def output_to_dictionary_iops(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_iops_re=re.compile(r'.*iops')   
    #iops        : min=360000, max=389000, avg=380481.28, stdev=3257.28, samples=548
    target_file_names={}
    d = {}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            target_file_names[int(n[2])]=l    # n[1] = iodpeth:1-1024, bs: 4+K,
    
    for key, file in target_file_names.items():
        #print(key, file)
        file1 = open(data_dir+file, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = ''.join(line).strip()
            num_re=re.compile(r'[0-9]+')
            if (total_iops_re.match(line)):
                l = num_re.findall(line)
                #print(l)
                if(key in d):
                    d[key].append(int(l[2]))
                else:
                    d[key] = []
                    d[key].append(int(l[2]))
    orderdict = collections.OrderedDict(sorted(d.items()))
    d = orderdict
    
    return d
    
def output_to_dictionary(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_bw_re=re.compile(r'.*WRITE: bw=')
    if 'read' in data_dir :
        total_bw_re=re.compile(r'.*READ: bw=')
    
    target_file_names={}
    d = {}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            target_file_names[int(n[2])]=l    
    
    #target_file_names
    for key, file in target_file_names.items():
        #print(key, file)
        file1 = open(data_dir+file, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = ''.join(line).strip()
            num_re=re.compile(r'[0-9]+')
            if (total_bw_re.match(line)):
                l = num_re.findall(line)
                if(key in d):
                    d[key].append(int(l[0]))
                else:
                    d[key] = []
                    d[key].append(int(l[0]))
    orderdict = collections.OrderedDict(sorted(d.items()))
    d = orderdict
    
    return d

def output_to_dictionary_bw(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_bw_re=re.compile(r'.*READ: bw=')
    if 'write' in data_dir :
        total_bw_re=re.compile(r'.*WRITE: bw=')
    
    target_file_names={}
    d = {}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            target_file_names[int(n[1])]=l    # n[1] = iodpeth:1-1024, bs: 4+K,
            #print(l, n[1], n[2])
    
    for key, file in target_file_names.items():
        #print(key, file)
        file1 = open(data_dir+file, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = ''.join(line).strip()
            num_re=re.compile(r'[0-9]+')
            if (total_bw_re.match(line)):
                l = num_re.findall(line)
                #print(l)
                if(key in d):
                    d[key].append(int(l[0]))
                else:
                    d[key] = []
                    d[key].append(int(l[0]))
    orderdict = collections.OrderedDict(sorted(d.items()))
    d = orderdict
    
    return d
    
def output_to_dictionary_iops(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_iops_re=re.compile(r'.*iops')   
    #iops        : min=360000, max=389000, avg=380481.28, stdev=3257.28, samples=548
    target_file_names={}
    d = {}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            target_file_names[int(n[2])]=l    # n[1] = iodpeth:1-1024, bs: 4+K,
    
    for key, file in target_file_names.items():
        #print(key, file)
        file1 = open(data_dir+file, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = ''.join(line).strip()
            num_re=re.compile(r'[0-9]+')
            if (total_iops_re.match(line)):
                l = num_re.findall(line)
                #print(l)
                if(key in d):
                    d[key].append(int(l[2]))
                else:
                    d[key] = []
                    d[key].append(int(l[2]))
    orderdict = collections.OrderedDict(sorted(d.items()))
    d = orderdict
    
    return d

def output_to_dictionary_iops(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_iops_re=re.compile(r'.*iops')   
    #iops        : min=360000, max=389000, avg=380481.28, stdev=3257.28, samples=548
    target_file_names={}
    d = {}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            target_file_names[int(n[2])]=l    # n[1] = iodpeth:1-1024, bs: 4+K,
    
    for key, file in target_file_names.items():
        #print(key, file)
        file1 = open(data_dir+file, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = ''.join(line).strip()
            num_re=re.compile(r'[0-9]+')
            if (total_iops_re.match(line)):
                l = num_re.findall(line)
                #print(l)
                if(key in d):
                    d[key].append(int(l[2]))
                else:
                    d[key] = []
                    d[key].append(int(l[2]))
    orderdict = collections.OrderedDict(sorted(d.items()))
    d = orderdict
    
    return d

def output_to_dictionarylist_bsqd(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_bw_re=re.compile(r'.*READ: bw=')
    if 'write' in data_dir :
        total_bw_re=re.compile(r'.*WRITE: bw=')
    
    d_bs = {}
    target_file_names={}
    namelist=[]
    name_dict={}
    orderlist=[]

    d = {}
    dd ={}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            key = int(n[2])
            if (key in d_bs ):
                d_bs[key].append(l)
            else :
                d_bs[key] = []
                d_bs[key].append(l)

    #print(d_bs)
    bs_orderdict = collections.OrderedDict(sorted(d_bs.items()))
    #for i, bs in enumerate(bs_orderdict):
        #print(i, bs, bs_orderdict[bs])
    
    for i, bs in enumerate(bs_orderdict):
        for l in bs_orderdict[bs]: 
            if(output_re.match(l)):
                n = num_re.findall(l)
                key = int(n[1])
                target_file_names[int(n[1])]=l    # n[1] = iodpeth:1-1024, n[2] bs: 4+K,
                #print(l, n[1], n[2])
            #fi
        #for end
        
        d = collections.OrderedDict(sorted(target_file_names.items()))
        if(bs in name_dict):
            name_dict[bs].append(d)
        else:
            name_dict[bs] = []
            name_dict[bs].append(d)            
    
    for i, bs in enumerate(name_dict.keys()):
        for j, f in enumerate(name_dict[bs]):
            print("{0}K".format(bs), j, f.keys())
            for k, key in enumerate(f):
                file = f[key]
                #print(key, data_dir+file)
                file1 = open(data_dir+file, 'r')
                Lines = file1.readlines()
                d={}
                for line in Lines:
                    line = ''.join(line).strip()
                    num_re=re.compile(r'[0-9]+')
                    if (total_bw_re.match(line)):
                        l = num_re.findall(line)
                        #print(l)
                        if(key in d):
                            d[key].append(int(l[0]))
                        else:
                            d[key] = []
                            d[key].append(int(l[0]))
                #for
                orderdict = collections.OrderedDict(sorted(d.items()))
                
                if(bs in dd):
                    dd[bs].append(orderdict)
                else:
                    dd[bs] = []
                    dd[bs].append(orderdict)
                
                orderlist.append(orderdict)
            #for
    od = collections.OrderedDict(sorted(dd.items()))
    #print("orderlist", orderlist)
    print("key:bs ", od.keys())    
    return od

def output_to_dictionarylist_bsqd_kiops(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    #total_bw_re=re.compile(r'.*READ: bw=')
    #if 'write' in data_dir :
        #total_bw_re=re.compile(r'.*WRITE: bw=')
    total_iops_re=re.compile(r'.*iops')   

    d_bs = {}
    target_file_names={}
    namelist=[]
    name_dict={}
    orderlist=[]

    d = {}
    dd ={}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            key = int(n[2])
            if (key in d_bs ):
                d_bs[key].append(l)
            else :
                d_bs[key] = []
                d_bs[key].append(l)

    #print(d_bs)
    bs_orderdict = collections.OrderedDict(sorted(d_bs.items()))
    #for i, bs in enumerate(bs_orderdict):
        #print(i, bs, bs_orderdict[bs])
    
    for i, bs in enumerate(bs_orderdict):
        for l in bs_orderdict[bs]: 
            if(output_re.match(l)):
                n = num_re.findall(l)
                key = int(n[1])
                target_file_names[int(n[1])]=l    # n[1] = iodpeth:1-1024, n[2] bs: 4+K,
                #print(l, n[1], n[2])
            #fi
        #for end
        
        d = collections.OrderedDict(sorted(target_file_names.items()))
        if(bs in name_dict):
            name_dict[bs].append(d)
        else:
            name_dict[bs] = []
            name_dict[bs].append(d)            
    
    for i, bs in enumerate(name_dict.keys()):
        for j, f in enumerate(name_dict[bs]):
            print("{0}K".format(bs), j, f.keys())
            for k, key in enumerate(f):
                file = f[key]
                #print(key, data_dir+file)
                file1 = open(data_dir+file, 'r')
                Lines = file1.readlines()
                d={}
                for line in Lines:
                    line = ''.join(line).strip()
                    num_re=re.compile(r'[0-9]+')
                    if (total_iops_re.match(line)):
                        l = num_re.findall(line)
                        #print(l)
                        if(key in d):
                            d[key].append(int(l[2])/1000)
                        else:
                            d[key] = []
                            d[key].append(int(l[2])/1000)
                #for
                orderdict = collections.OrderedDict(sorted(d.items()))
                
                if(bs in dd):
                    dd[bs].append(orderdict)
                else:
                    dd[bs] = []
                    dd[bs].append(orderdict)
                
                orderlist.append(orderdict)
            #for
    od = collections.OrderedDict(sorted(dd.items()))
    #print("orderlist", orderlist)
    print("key:bs ", od.keys())    
    return od

def output_to_dictionarylist_bsqd_iops(data_dir):
    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    #total_bw_re=re.compile(r'.*READ: bw=')
    #if 'write' in data_dir :
        #total_bw_re=re.compile(r'.*WRITE: bw=')
    total_iops_re=re.compile(r'.*iops')   

    d_bs = {}
    target_file_names={}
    namelist=[]
    name_dict={}
    orderlist=[]

    d = {}
    dd ={}
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            key = int(n[2])
            if (key in d_bs ):
                d_bs[key].append(l)
            else :
                d_bs[key] = []
                d_bs[key].append(l)

    #print(d_bs)
    bs_orderdict = collections.OrderedDict(sorted(d_bs.items()))
    #for i, bs in enumerate(bs_orderdict):
        #print(i, bs, bs_orderdict[bs])
    
    for i, bs in enumerate(bs_orderdict):
        for l in bs_orderdict[bs]: 
            if(output_re.match(l)):
                n = num_re.findall(l)
                key = int(n[1])
                target_file_names[int(n[1])]=l    # n[1] = iodpeth:1-1024, n[2] bs: 4+K,
                #print(l, n[1], n[2])
            #fi
        #for end
        
        d = collections.OrderedDict(sorted(target_file_names.items()))
        if(bs in name_dict):
            name_dict[bs].append(d)
        else:
            name_dict[bs] = []
            name_dict[bs].append(d)            
    
    for i, bs in enumerate(name_dict.keys()):
        for j, f in enumerate(name_dict[bs]):
            print("{0}K".format(bs), j, f.keys())
            for k, key in enumerate(f):
                file = f[key]
                #print(key, data_dir+file)
                file1 = open(data_dir+file, 'r')
                Lines = file1.readlines()
                d={}
                for line in Lines:
                    line = ''.join(line).strip()
                    num_re=re.compile(r'[0-9]+')
                    if (total_iops_re.match(line)):
                        l = num_re.findall(line)
                        #print(l)
                        if(key in d):
                            d[key].append(int(l[2]))
                        else:
                            d[key] = []
                            d[key].append(int(l[2]))
                #for
                orderdict = collections.OrderedDict(sorted(d.items()))
                
                if(bs in dd):
                    dd[bs].append(orderdict)
                else:
                    dd[bs] = []
                    dd[bs].append(orderdict)
                
                orderlist.append(orderdict)
            #for
    od = collections.OrderedDict(sorted(dd.items()))
    #print("orderlist", orderlist)
    print("key:bs ", od.keys())    
    return od

def output_to_dictionarylist_bsqd_lat(data_dir):

    output_re=re.compile(r'.*_output')
    num_re=re.compile(r'[0-9]+')
    total_nsec_lat_re=re.compile(r'    clat \(nsec')
    total_usec_lat_re=re.compile(r'    clat \(usec')
    total_msec_lat_re=re.compile(r'    clat \(msec')
    
    namelist=[]
    name_dict={}
    orderlist=[]
    target_file_names={}
    d_bs = {}
    d = {}
    d_min = {}
    d_max = {}
    d_avg = {}
    d_stdev={}
    
    dd ={}
    dd_min = {}
    dd_max = {}
    dd_avg = {}
    dd_stdev={}
    
    L = os.listdir(data_dir)
    
    for l in L: 
        if(output_re.match(l)):
            n = num_re.findall(l)
            key = int(n[2])
            if (key in d_bs ):
                d_bs[key].append(l)
            else :
                d_bs[key] = []
                d_bs[key].append(l)

    #print(d_bs)
    bs_orderdict = collections.OrderedDict(sorted(d_bs.items()))
    #for i, bs in enumerate(bs_orderdict):
        #print(i, bs, bs_orderdict[bs])
    
    for i, bs in enumerate(bs_orderdict):
        for l in bs_orderdict[bs]: 
            if(output_re.match(l)):
                n = num_re.findall(l)
                key = int(n[1])
                target_file_names[int(n[1])]=l    # n[1] = iodpeth:1-1024, n[2] bs: 4+K,
                print(l, n[1], n[2])
            #fi
        #for end
        d = collections.OrderedDict(sorted(target_file_names.items()))
        if(bs in name_dict):
            name_dict[bs].append(d)
        else:
            name_dict[bs] = []
            name_dict[bs].append(d)            
    #4K
    ### QD 1 2 4 8 16
    ### QD 1 2 4 8 16
    ### QD 1 2 4 8 16
    
    for i, bs in enumerate(name_dict.keys()):
        for j, f in enumerate(name_dict[bs]):
            print("{0}K".format(bs), j, f.keys())
            for key, file in target_file_names.items(): #for k, key in enumerate(f):
                #print(key, file)
                #file = f[key]
                file1 = open(data_dir+file, 'r')
                Lines = file1.readlines()
                for line in Lines:
                    #line = ''.join(line).strip()
                    num_re=re.compile(r'[0-9]+')
                    if (total_usec_lat_re.match(line)):
                        #print(line)
                        l = num_re.findall(line)
                        if ((key not in d)):
                            d_min[key] = []
                            d_max[key] = []
                            d_avg[key] = []
                            d_stdev[key] = []
                        #print(line)
                        #print(l)
                        d_min[key].append(int(l[0]))
                        d_max[key].append(int(l[1]))
                        d_avg[key].append(int(l[2]))
                        d_stdev[key].append(int(l[4]))
                    elif (total_nsec_lat_re.match(line)):
                        l = num_re.findall(line)
                        if ((key not in d)):
                            d_min[key] = []
                            d_max[key] = []
                            d_avg[key] = []
                            d_stdev[key] = []
                        #print(line)
                        #print(l)
                        d_min[key].append(int(l[0])/1000)
                        d_max[key].append(int(l[1])/1000)
                        d_avg[key].append(int(l[2])/1000)
                        d_stdev[key].append(int(l[4])/1000)
                    elif (total_msec_lat_re.match(line)):
                        l = num_re.findall(line)
                        if ((key not in d)):
                            d_min[key] = []
                            d_max[key] = []
                            d_avg[key] = []
                            d_stdev[key] = []
                        #print(line)
                        #print(l)
                        d_min[key].append(int(l[0])*1000)
                        d_max[key].append(int(l[1])*1000)
                        d_avg[key].append(int(l[2])*1000)
                        d_stdev[key].append(int(l[4])*1000)
                
                orderdict = collections.OrderedDict(sorted(d.items()))
                
                if(bs in dd):
                    dd[bs].append(orderdict)
                    dd_min[bs].append(collections.OrderedDict(sorted(d_min.items())))
                    dd_max[bs].append(collections.OrderedDict(sorted(d_max.items())))
                    dd_avg[bs].append(collections.OrderedDict(sorted(d_avg.items())))
                    dd_stdev[bs].append(collections.OrderedDict(sorted(d_stdev.items())))
                    
                else:
                    dd[bs] = []
                    dd_min[bs] = []
                    dd_max[bs] = []
                    dd_avg[bs] = []
                    dd_stdev[bs] = []
                    dd[bs].append(orderdict)
                    dd_min[bs].append(collections.OrderedDict(sorted(d_min.items())))
                    dd_max[bs].append(collections.OrderedDict(sorted(d_max.items())))
                    dd_avg[bs].append(collections.OrderedDict(sorted(d_avg.items())))
                    dd_stdev[bs].append(collections.OrderedDict(sorted(d_stdev.items())))
    #od = collections.OrderedDict(sorted(dd.items()))
    #print("orderlist", orderlist)
    #print("key:bs ", od.keys())    
    #return od
    return [dd_min,dd_max,dd_avg,dd_stdev]

# -------- queue depth x blocksize output file parser ---------- #
def data_parser (dev_list, workload, data_dirs):
    ax_xdata = []
    ax_ydata = []
    d={}
    d_dev={}
    for j,dev in enumerate(dev_list):
        print(dev)
        for i,wrkld in enumerate(workload):
            for p,dir in enumerate(data_dirs): 
                #data_dir = "/home/inhoinno/nvme_fio/FEMU/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                data_dir = "/Users/inhoinno/new_nvme_fio/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                #data_dir ='C:/Users/mearr/Downloads/nvme_fio-master/WDZNS_WZS4C8T4TDSP303/nvme_fio_bs/'+wrkld+'/'
                #data_dir += trial[i]+'/'
                #data_dir += "trialx20-psync/"
                data_dir += dir
                #print(data_dir) Check OK
                try :
                    print(data_dir)
                    #d = output_to_dictionary(data_dir)
                    d = output_to_dictionary_bw(data_dir)
                    #print(d)
                    ax_xdata.append(d.keys())
                    ax_ydata.append([np.mean(x) for x in d.values()])
                except FileNotFoundError:
                    print("!? [FILE NOT FOUND] {0}".format(data_dir))
    return [ax_xdata,ax_ydata]

def data_parser_qdbs (dev_list, workload, data_dirs):
    ax_xdata = []
    ax_ydata = []
    d={}
    d_dev={}
    #workload = 'stride_write'.
    for i,dev in enumerate(dev_list):
        print(dev)
        for j,wrkld in enumerate(workload):
            for p,dir in enumerate(data_dirs): 
                #data_dir = "/home/inhoinno/nvme_fio/FEMU/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                data_dir = "/Users/inhoinno/new_nvme_fio/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                #data_dir ='C:/Users/mearr/Downloads/nvme_fio-master/WDZNS_WZS4C8T4TDSP303/nvme_fio_bs/'+wrkld+'/'
                #data_dir += trial[i]+'/'
                #data_dir += "trialx20-psync/"
                #data_dir += "trialx20-io-uring/"
                #data_dir += "trialx20-ba4K-libaio/"
                data_dir += dir
                #print(data_dir) Check OK
                try :
                    print(data_dir)
                    #d = output_to_dictionary(data_dir)
                    d = output_to_dictionarylist_bsqd(data_dir)
                    #print(d)
                    #ax_xdata.append(d.keys())
                    #ax_ydata.append([np.mean(x) for x in d.values()])
                    
                except FileNotFoundError:
                    print(" [FILE NOT FOUND]!? {0}".format(data_dir))
                
        print(len(ax_ydata))
        blocksize = list(d.keys())
        #queuedepth = list(d.values())
        for i, bs in enumerate(blocksize):
            print(bs)
            x =[]
            y =[]
            for j, val in enumerate(d[bs]):
                q = list(val.keys())
                v =[np.mean(x) for x in val.values()]
                #print(bs,j,v[0],q[0])
                #print("q len{0}".format(len(q)), q)  #q = block size lists
                x.append(q[0])
                y.append(v[0])
            ax_xdata.append(x)
            ax_ydata.append(y)
        
    len(ax_ydata), len(ax_xdata)
    return [ax_xdata,ax_ydata]

def data_parser_qdbs_iops (dev_list, workload, data_dirs):
    ax_xdata = []
    ax_ydata = []
    d={}
    d_dev={}
    #workload = 'stride_write'.
    for i,dev in enumerate(dev_list):
        print(dev)
        for j,wrkld in enumerate(workload):
            for p,dir in enumerate(data_dirs): 
                #data_dir = "/home/inhoinno/nvme_fio/FEMU/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                data_dir = "/Users/inhoinno/new_nvme_fio/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                #data_dir ='C:/Users/mearr/Downloads/nvme_fio-master/WDZNS_WZS4C8T4TDSP303/nvme_fio_bs/'+wrkld+'/'
                #data_dir += trial[i]+'/'
                #data_dir += "trialx20-psync/"
                #data_dir += "trialx20-io-uring/"
                data_dir += dir
                #data_dir += "trialx20-ba4K-libaio/"
                #print(data_dir) Check OK
                try :
                    print(data_dir)
                    #d = output_to_dictionary(data_dir)
                    d = output_to_dictionarylist_bsqd_iops(data_dir)
                    #print(d)
                    #ax_xdata.append(d.keys())
                    #ax_ydata.append([np.mean(x) for x in d.values()])
                    
                except FileNotFoundError:
                    print(" [FILE NOT FOUND]!? {0}".format(data_dir))
                
        print(len(ax_ydata))
        blocksize = list(d.keys())
        #queuedepth = list(d.values())
        for i, bs in enumerate(blocksize):
            print(bs)
            x =[]
            y =[]
            for j, val in enumerate(d[bs]):
                q = list(val.keys())
                v =[np.mean(x) for x in val.values()]
                #print(bs,j,v[0],q[0])
                #print("q len{0}".format(len(q)), q)  #q = block size lists
                x.append(q[0])
                y.append(v[0])
            ax_xdata.append(x)
            ax_ydata.append(y)
        
    len(ax_ydata), len(ax_xdata)
    return [ax_xdata,ax_ydata]

def data_parser_qdbs_kiops (dev_list, workload, data_dirs):
    ax_xdata = []
    ax_ydata = []
    d={}
    d_dev={}
    #workload = 'stride_write'.
    for i,dev in enumerate(dev_list):
        print(dev)
        for j,wrkld in enumerate(workload):
            for p,dir in enumerate(data_dirs): 
                #data_dir = "/home/inhoinno/nvme_fio/FEMU/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                data_dir = "/Users/inhoinno/new_nvme_fio/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                #data_dir ='C:/Users/mearr/Downloads/nvme_fio-master/WDZNS_WZS4C8T4TDSP303/nvme_fio_bs/'+wrkld+'/'
                #data_dir += trial[i]+'/'
                #data_dir += "trialx20-psync/"
                data_dir += dir
                #data_dir += "trialx20-ba4K-libaio/"
                #print(data_dir) Check OK
                try :
                    print(data_dir)
                    #d = output_to_dictionary(data_dir)
                    d = output_to_dictionarylist_bsqd_iops(data_dir)
                    #print(d)
                    #ax_xdata.append(d.keys())
                    #ax_ydata.append([np.mean(x) for x in d.values()])
                    
                except FileNotFoundError:
                    print(" [FILE NOT FOUND]!? {0}".format(data_dir))
                
        #len(ax_ydata)
        blocksize = list(d.keys())
        #queuedepth = list(d.values())
        for i, bs in enumerate(blocksize):
            #print(bs, blocksize)
            x =[]
            y =[]
            for j, val in enumerate(d[bs]):
                q = list(val.keys())
                v =[np.mean(x)/1000 for x in val.values()]
                #print(bs,j,v[0],q[0])
                x.append(q[0])
                y.append(v[0])
            ax_xdata.append(x)
            ax_ydata.append(y)
        
    len(ax_ydata), len(ax_xdata)
    return [ax_xdata,ax_ydata]

def data_parser_qdbs_lat(dev_list, workload, data_dirs):
    ax_xdata = []
    ax_ydata = []
    d={}
    d_list=[]
    d_dev={}
    #workload = 'stride_write'.
    for i,dev in enumerate(dev_list):
        print(dev)
        for j,wrkld in enumerate(workload):
            for p,dir in enumerate(data_dirs): 
                #data_dir = "/home/inhoinno/nvme_fio/FEMU/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                data_dir = "/Users/inhoinno/new_nvme_fio/{0}/nvme_fio_bs/{1}/".format(dev, wrkld)
                #data_dir ='C:/Users/mearr/Downloads/nvme_fio-master/WDZNS_WZS4C8T4TDSP303/nvme_fio_bs/'+wrkld+'/'
                #data_dir += trial[i]+'/'
                #data_dir += "trialx20-psync/"
                #data_dir += "trialx20-io-uring/"
                #data_dir += "trialx20-ba4K-libaio/"
                #print(data_dir) Check OK
                try :
                    print(data_dir)
                    #d = output_to_dictionary(data_dir)
                    d_list = output_to_dictionarylist_bsqd_lat(data_dir)
                    #print(d)
                    #ax_xdata.append(d.keys())
                    #ax_ydata.append([np.mean(x) for x in d.values()])
                    
                except FileNotFoundError:
                    print(" [FILE NOT FOUND]!? {0}".format(data_dir))
                
    #len(ax_ydata)
    #blocksize = list(d.keys())
    blocksize = list(d_list[0].keys())
    #queuedepth = list(d.values())
    for i, bs in enumerate(blocksize):
        #print(bs, blocksize)
        x =[]
        y =[]
        for j, val in enumerate(d[bs]):
            q = list(val.keys())
            v =[np.mean(x)/1000 for x in val.values()]
            #print(bs,j,v[0],q[0])
            x.append(q[0])
            y.append(v[0])
        ax_xdata.append(x)
        ax_ydata.append(y)
    
    len(ax_ydata), len(ax_xdata)
    return [ax_xdata,ax_ydata]

# --------  waf parser in warmup ---------- #

def waf_log_to_waf_lists (data_dir, filename=None):
    # ----------------------- Regular Expr. ------------------------- #
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
    
    waf_list = []
    hbmw_list = []
    mbmw_list = []
    erase_list=[]
    
    #print (data_dir+t+filename)
    waf_data = data_dir+filename
    file1 = open(waf_data, 'r')
    Lines = file1.readlines()
    start_h = None
    start_d = None
    start_e = None
    for line in Lines:
        line = ''.join(line).strip().replace(",", '')
        if hbmw_re.match(line) or mbmw_re.match(line) or mbe_re.match(line):
            if hbmw_re.match(line):
                l = num_re.findall(line)
                if (start_h is None):
                    start_h = int(l[0])
                host_kb = (int(l[0]) - start_h)/1024
                host_mb = host_kb/1024
                #print('host(Mb)', host_mb)
            elif mbmw_re.match(line):
                l = num_re.findall(line)
                if (start_d is None):
                    start_d = int(l[0])
                dev_kb = (int(l[0]) - start_d)/1024 
                dev_mb = dev_kb/1024
                #print('dev(Mb)', dev_mb )
                
            elif mbe_re.match(line):
                l = num_re.findall(line)
                if (start_e is None):
                    start_e = int(l[0])
                erase_kb = (int(l[0]) - start_e) / 1024 
                erase_mb = erase_kb/1024 
                #print(erase_mb)

                if host_mb == 0.0:
                    waf_list.append(1.0)
                    hbmw_list.append(0)
                    mbmw_list.append(0)
                    erase_list.append(0)

                else:
                    #print(start_h,"start_h", start_d, "start_d")
                    waf_list.append( round(dev_mb/host_mb, 5) )
                    hbmw_list.append(host_mb/1024/1024)
                    mbmw_list.append(dev_mb/1024/1024)
                    erase_list.append(erase_mb/1024/1024)
    
    return [waf_list, hbmw_list , mbmw_list, erase_list]


def waf_log_to_waf_listlist(data_dir, subdir, filename=None):
    #fdev="Samsung-FDP-PM9D3a-MZWL67T6HBLC-7.68TB-PCIeGen5/"
    #workload= ['warmup_v2/multi_thread_kopernik']
    #data_dir = "/data/inho/nvme_fio/{0}/{1}/".format(fdev, workload[0])
    #subdir = ['t{0}/'.format(x) for x in np.arange(4) ]
    #subdir = ['{0}p/'.format(x) for x in np.arange(60,170,10) ]
    #t_labels=[ "3randwrites + 1write" , "2randwrites + 2write" , "1randwrites + 3write", "4write" ]
    #t_labels.append("4randwrites")

    # ----------------------- Regular Expr. ------------------------- #
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
    
    waf_list = []

    for i,t in enumerate(subdir):
        #print (data_dir+t+filename)
        waf_list.append(waf_log_to_waf_lists(data_dir+t, filename))

    return [subdir, waf_list]

#def waf_log_to_dictionary_list(data_dir):
def get_waf_by_aligned_hbmw(data_dir:str, scale:float, filename=None):
    waf_text_index = []
    try :
        print(data_dir)
        #d = output_to_dictionary(data_dir)
        #file1 = open(data_dir, 'r')
        #Lines = file1.readlines()
        if filename == None : 
            filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir,filename)
        info_list = waf_log_to_waf_lists(data_dir,filename)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        #mbmw_list= info_list[2] 
        #erase_list= info_list[3] 
        hbmw_list_TB = [ x /scale for x in hbmw_list]
        #ax_xdata.append(d.keys())
        #ax_ydata.append([np.mean(x) for x in d.values()])
        cnt=0
        waf_text_index.append( waf_list[0] )
        local_waf_index=[ ]
        next_fill_index=0
        for i,hb in enumerate(hbmw_list_TB) :
            if hb > (next_fill_index) + 0.999 and hb < (next_fill_index+1) + 0.001 : 
                #print(waf_list[i], i, hb)
                cnt+=1
                local_waf_index.append(waf_list[i])
                continue
            else:
                if cnt >= 1:
                    #print (local_waf_index)
                    waf_text_index.append( round(np.mean(local_waf_index),4) )
                    cnt=0
                    local_waf_index=[ ]
                    next_fill_index += 1
            
    except FileNotFoundError:
        print(" [FILE NOT FOUND]!? {0}".format(data_dir))

    return waf_text_index

def get_waf_by_aligned_hbmw(data_dir:str, scale:float, filename=None, x_cut=None):
    waf_text_index = []
    try :
        print(data_dir)
        #d = output_to_dictionary(data_dir)
        #file1 = open(data_dir, 'r')
        #Lines = file1.readlines()
        if filename == None : 
            filename="samsung_waf_1sec.txt"
        ret = check_file_existence(data_dir,filename)
        info_list = waf_log_to_waf_lists(data_dir,filename)
        waf_list = info_list[0]
        hbmw_list = info_list[1] 
        #mbmw_list= info_list[2] 
        #erase_list= info_list[3] 
        hbmw_list_TB = [ x / scale for x in hbmw_list]
        print("hbmw_list_TB", hbmw_list_TB[-1])
        #ax_xdata.append(d.keys())
        #ax_ydata.append([np.mean(x) for x in d.values()])
        cnt=0
        waf_text_index.append( waf_list[0] )
        local_waf_index=[ ]
        next_fill_index=0
        for i,hb in enumerate(hbmw_list_TB) :
            if hb > (next_fill_index) + 0.99 and hb < (next_fill_index+1) + 0.01 : 
                #print(waf_list[i], i, hb)
                cnt+=1
                local_waf_index.append(waf_list[i])
                continue
            else:
                if cnt >= 1:
                    #print (local_waf_index, next_fill_index+1)
                    waf_text_index.append( round(np.mean(local_waf_index),4) )
                    cnt=0
                    local_waf_index=[ ]
                    next_fill_index += 1
            
    except FileNotFoundError:
        print(" [FILE NOT FOUND]!? {0}".format(data_dir))


    if x_cut != None and x_cut > 0 :
        waf_text_index = waf_text_index[:x_cut]

    return waf_text_index


def get_per_ruh_waf_to_dict (data_dir, filename=None):
    # ----------------------- Regular Expr. ------------------------- #
    ruh_re=re.compile(r'^Reclaim Unit Handle.*')
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
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
            if (ruhid == 0) or (ruhid == 1) or (ruhid == 15):
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
    for key in ruh_waf.keys():
        print(key, ruh_waf[key][-1] )
        #ax[i].plot(range(len(ruh_waf[key])), ruh_waf[key] , label = key)
        #ax[i].set_ylim([0.99, 4.0])
        #ax[i].set_title(t)

    return ruh_waf

def get_per_ruh_everything_to_dict (data_dir, filename=None):
    # ----------------------- Regular Expr. ------------------------- #
    ruh_re=re.compile(r'^Reclaim Unit Handle.*')
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
    # ---------------------------------------------------------------- #

    ruh_waf = {} 
    ruh_mbmw= {}
    ruh_hbmw= {}

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
            if (ruhid == 0) or (ruhid == 1)  or (ruhid == 2) or (ruhid == 15):

                ##  ruh waf/hbmw/mbmw collect  ##
                if (hbmw == 0) or (mbmw == 0):
                    #print (ruhid , 1.0)
                    if not (ruhid in ruh_waf):
                        ruh_waf[ruhid] = [float(1.0)]
                        ruh_hbmw[ruhid] = [hbmw]
                        ruh_mbmw[ruhid] = [mbmw]
                    else:
                        ruh_waf[ruhid].append(float(1.0))
                        ruh_hbmw[ruhid].append(hbmw)
                        ruh_mbmw[ruhid].append(mbmw)

                else:
                    #print(ruhid, mbmw/hbmw)
                    if not (ruhid in ruh_waf):
                        ruh_waf[ruhid] = [mbmw/hbmw]
                        ruh_hbmw[ruhid] = [hbmw]
                        ruh_mbmw[ruhid] = [mbmw]
                    else:
                        ruh_waf[ruhid].append(float(mbmw/hbmw))
                        ruh_hbmw[ruhid].append(hbmw)
                        ruh_mbmw[ruhid].append(mbmw)


                

    for key in ruh_waf.keys():
        print(key, ruh_waf[key][-1] )
        #ax[i].plot(range(len(ruh_waf[key])), ruh_waf[key] , label = key)
        #ax[i].set_ylim([0.99, 4.0])
        #ax[i].set_title(t)

    return [ruh_waf,ruh_hbmw,ruh_mbmw]



def get_per_ruh_mb_to_list (data_dir, filename=None):
    # ----------------------- Regular Expr. ------------------------- #
    ruh_re=re.compile(r'^Reclaim Unit Handle.*')
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
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
            if (ruhid == 0) or (ruhid == 1) or (ruhid == 15):
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
                        ruh_hbmw[ruhid].append(hbmw)
                        ruh_mbmw[ruhid].append(mbmw)
                    else:
                        #ruh_waf[ruhid].append(float(mbmw/hbmw))
                        ruh_hbmw[ruhid].append(hbmw)
                        ruh_mbmw[ruhid].append(mbmw)

    for key in ruh_waf.keys():
        print(key, ruh_waf[key][-1] )
        #ax[i].plot(range(len(ruh_waf[key])), ruh_waf[key] , label = key)
        #ax[i].set_ylim([0.99, 4.0])
        #ax[i].set_title(t)

    return [ruh_hbmw,ruh_mbmw]

def get_per_ruh_waf_to_list (data_dir, subdir, filename=None):
    # ---------------------------------------------------------------- #
    if filename is None:
        filename = "samsung_waf_1sec.txt"
    # ---------------------------------------------------------------- #
    per_ruh_waf_list = []
    for i,t in enumerate(subdir):
        per_ruh_waf_list.append(get_per_ruh_waf_to_dict(data_dir+t, filename=None))
        print(t)
    return per_ruh_waf_list

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

# --------  iostat bw parser in warmup ---------- #
#def bw_log_to_bw_lists(data_dir, filename):   

def iostat_bw_parser_to_list(dev_nvme, data_dir, util):
    #fdev="Samsung-FDP-PM9D3a-MZWL67T6HBLC-7.68TB-PCIeGen5/"
    #workload= ['warmup/default'] 
    #data_dir = "/data/inho/nvme_fio/{0}/{1}/".format(fdev, workload[0])
    iostat_re = re.compile(r'{0}'.format(dev_nvme)) #nvme1n1 or nvme3n1
    num_float_re = re.compile(r'[0-9]+.[0-9]+')
    #util = ['{0}p/'.format(x) for x in np.arange(10,160,10) ]

    bw_list = []
    bw_iostat_data = data_dir+"samsung_bw_1sec.txt"
    #detect auto
    
    file2 = open(bw_iostat_data, 'r')
    Lines = file2.readlines()
    for line in Lines:
        line = ''.join(line).strip().replace(",", '')
        if iostat_re.match(line):
            l = num_re.findall(line)
            #print(l)
            l = num_float_re.findall(line)
            #print(float(l[3]))
            bw_list.append(float(l[3]))

    #print ( len (bw_list))
    return bw_list


# --------  waf parser in warmup ---------- #
def waf_log_to_list (data_dir, filename=None):
    # ----------------------- Regular Expr. ------------------------- #
    num_re=re.compile(r'[0-9]+')
    hbmw_re=re.compile(r'.*(HBMW)')
    mbmw_re=re.compile(r'.*(MBMW)')
    mbe_re=re.compile(r'.*(MBE)')
    # ---------------------------------------------------------------- #

    if filename is None:
        filename = "samsung_waf_1sec.txt"
    
    waf_list = []
    hbmw_list = []
    mbmw_list = []
    erase_list=[]
    
    #print (data_dir+t+filename)
    waf_data = data_dir+filename
    file1 = open(waf_data, 'r')
    Lines = file1.readlines()
    start_h = None
    start_d = None
    start_e = None
    for line in Lines:
        line = ''.join(line).strip().replace(",", '')
        if hbmw_re.match(line) or mbmw_re.match(line) or mbe_re.match(line):
            if hbmw_re.match(line):
                l = num_re.findall(line)
                if (start_h is None):
                    start_h = int(l[0])
                host_kb = (int(l[0]) - start_h)/1024
                host_mb = host_kb/1024
                #print('host(Mb)', host_mb)
            elif mbmw_re.match(line):
                l = num_re.findall(line)
                if (start_d is None):
                    start_d = int(l[0])
                dev_kb = (int(l[0]) - start_d)/1024 
                dev_mb = dev_kb/1024
                #print('dev(Mb)', dev_mb )
                
            elif mbe_re.match(line):
                l = num_re.findall(line)
                if (start_e is None):
                    start_e = int(l[0])
                erase_kb = (int(l[0]) - start_e) / 1024 
                erase_mb = erase_kb/1024 
                #print(erase_mb)

                if host_mb == 0.0:
                    waf_list.append(1.0)
                    hbmw_list.append(0)
                    mbmw_list.append(0)
                    erase_list.append(0)

                else:
                    #print(start_h,"start_h", start_d, "start_d")
                    waf_list.append( round(dev_mb/host_mb, 3) )
                    hbmw_list.append(host_mb/1024/1024)
                    mbmw_list.append(dev_mb/1024/1024)
                    erase_list.append(erase_mb/1024/1024)
    
    #return in terabytes
    return [waf_list, hbmw_list , mbmw_list, erase_list]
# -------- log file parser ---------- #