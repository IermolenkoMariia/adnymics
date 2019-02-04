#!/bin/bash

users=($(who | cut -d' ' -f1 | sort | uniq));

for user in ${users[*]}
do
    shell=$(finger $user | grep 'Shell:*' | cut -f3 -d ":");
    printf "%s %s\n" $shell $user;
done
