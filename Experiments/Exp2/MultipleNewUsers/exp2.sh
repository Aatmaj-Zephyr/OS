#!/bin/bash
for (( i=1; i<=2; i++ )); do
   echo "please enter name:"
   read name
   adduser $name
   passwd $name
 done
