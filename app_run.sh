#!/bin/bash

while true
do
    hypercorn app_async:app -b 0.0.0.0:5000 
    sleep 1
done
