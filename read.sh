#!/bin/bash
read filename

read permission

touch $filename
chmod $permission $filename
