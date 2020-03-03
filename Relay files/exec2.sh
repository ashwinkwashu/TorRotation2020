#!/bin/bash
grep rw-p /proc/"$(pgrep '^tor')"/maps | grep "heap" | sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' | while read start stop; do gdb --batch --pid "$(pgrep '^tor')" -ex "dump memory $(date +%F+%T).dump 0x$start 0x$stop" &> /dev/null; done;
#mv 557e97c6f000* files/new/$(date +%F+%T)

