#!/bin/bash


sbin/hadoop-daemon.sh stop namenode
sbin/hadoop-daemon.sh stop datanode
sbin/yarn-daemon.sh stop nodemanager
sbin/yarn-daemon.sh stop resourcemanager
sbin/mr-jobhistory-daemon.sh stop historyserver

jps
