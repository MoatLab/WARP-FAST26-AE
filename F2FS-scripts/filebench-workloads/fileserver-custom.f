#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#
#
# Copyright 2008 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.
#
# 224*1000 *0.8* 1024 / 512 = 358400
# 482 * 0.8 *1000 *1024/ 512 = 771200



set $dir=/mnt/f2fs
set $nfiles=771200
set $meandirwidth=20
set $filesize=512k
set $nthreads=200
set $iosize=256k
set $overwritesize=256k


define fileset
name=withgc,path=$dir,size=$filesize,entries=$nfiles,dirwidth=$meandirwidth,prealloc,reuse


define process name=filereader,instances=1
{
  thread name=filereaderthread,instances=$nthreads
  {
    flowop openfile
name=openfile1,filesetname=withgc,fd=1,directio=0
    flowop write
name=writefile1,iosize=$overwritesize,random,fd=1,directio=0
    flowop closefile name=closefile2,fd=1
    flowop openfile
name=openfile3,filesetname=withgc,fd=1,directio=0
    flowop read name=readfile1,fd=1,iosize=$iosize,random,directio=0
    flowop closefile name=closefile4,fd=1
    flowop openfile
name=openfile4,filesetname=withgc,fd=1,directio=0
    flowop write
name=writefile2,iosize=$overwritesize,random,fd=1,directio=0
    flowop closefile name=closefile5,fd=1
    flowop openfile
name=openfile5,filesetname=withgc,fd=1,directio=0
    flowop write
name=writefile3,iosize=$overwritesize,random,fd=1,directio=0
    flowop closefile name=closefile6,fd=1
    flowop openfile
name=openfile7,filesetname=withgc,fd=1,directio=0
    flowop write
name=writefile4,iosize=$overwritesize,random,fd=1,directio=0
    flowop closefile name=closefile8,fd=1
  }
}


echo  "File-server Version 3.0 personality successfully loaded"


run 36000
