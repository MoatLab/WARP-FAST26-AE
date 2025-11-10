import os
import sys
num="64"
num=int(num)
rw="randwrite"
#ZNS_type="FU"

#size_t=2048
#size_s="4G"
offset_t=0
#ioengine="psync"
#ioengine="io_uring"
#ioengine="libaio"
ioengine="io_uring_cmd"
log_avg_msec=100
log_hist_msec=1


thread_rws=[["write","write"]]
#thread_rws.append(["randwrite","randwrite","write","write"])
#thread_rws.append(["randwrite","write","write","write"])
#thread_rws.append(["write","write","write","write"])
#thread_rws.append(["randwrite","randwrite","randwrite","write"])

#ioengine="io_uring_cmd"     #nvme_passthru
#zipf_alpha=0.9
for q in range(1): #1(0) 2 4 ... 2048(11)
    for k in range(len(thread_rws)):  #4(0) 8(1) 16(2) ... 1024(8)
        bs="4K"
        #qd=(2**q)
        qd=4
        #size=10*(k+1)
        ini="./py_{0}files_bs{1}_QD{2}_t{3}".format(rw,bs,qd,k)
        if os.path.exists(ini):
                os.remove(ini)
        f=open("py_{0}files_bs{1}_QD{2}_t{3}".format(rw,bs,qd,k), "a")
        f.write("[global]\n")
        f.write("ioengine={0}\n".format(ioengine))
        f.write("cmd_type=nvme\n")
        f.write("filename=/dev/ng0n1\n")
        f.write("group_reporting=1\n")
        #f.write("filename=/dev/nvme1n1\n")
        f.write("fdp=1\n")
        #size=7864 #G
        #size=round( size * ((10*(k+1)) / 100) )
        #log="{0}threadQD{3}_{1}{2}".format(1,bs,rw,qd)
    
        for t in range(2):
            # == worker 1 == #
            log="{0}threadQD{3}_{1}{2}".format(1,bs,thread_rws[k][t],qd)
            f.write("\n[worker{0}]\n".format(t))
            f.write("rw={0}\n".format(thread_rws[k][t]))
            #f.write("random_distribution=zipf:{0}\n".format(zipf_alpha))
            #f.write("rw_sequencer=sequential\n")
            #f.write("blockalign=16K\n")
            f.write("numjobs={0}\n".format(1))
            #f.write("cpus_allowed={0}\n".format(2+t))
            #f.write("size={0}G\n".format(size))
            #f.write("offset=0M\n")
            #f.write("offset_increment={0}M\n".format(size_t))
            f.write("bs={0}\n".format(bs))
            f.write("offset={0}%\n".format(50*t))
            f.write("size=50%\n")
            f.write("time_based=1\n")
            #f.write("direct=1\n")
            #f.write("overwrite=1\n")
            f.write("norandommap\n")
            #f.write("fdp_pli=0\n")
            f.write("iodepth={0}\n".format(qd))
            f.write("numjobs={0}\n".format(1))
            f.write("runtime=12000\n")
            f.write("fdp_pli={0}\n".format(t))
            #f.write("zonemode=zbd\n")
            #for i in range(k+1):
            #        f.write("offset_increment={0}M\n".format(size_t*i))

            #f.write("log_hist_msec={0}\n".format(log_hist_msec))
            f.write("log_avg_msec={0}\n".format(log_avg_msec))
            f.write("write_bw_log={0}\n".format(log))
            f.write("write_lat_log={0}\n".format(log))
            f.write("write_iops_log={0}\n".format(log))
            #f.write("write_iolog={0}\n".format(log))
            if(rw=="write"):
                    f.write("stonewall\n")

            


        f.close()

