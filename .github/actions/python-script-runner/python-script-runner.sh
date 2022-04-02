#!/bin/sh -l

python3 -m pip freeze
echo "Started: $0"
cmd1="$1 $2 $3 $4 $5 $6 $7 $8 $9"
echo "Begin executing $cmd1"
echo "-----------------------------------------------------------------------------------------------------------"
eval $cmd1
ret=$?
echo "-----------------------------------------------------------------------------------------------------------"
echo "End executing $cmd1"
if [ $ret -ne 0 ] ; then
    echo "Execution failed."
    exit 1
fi
