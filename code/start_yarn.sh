#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java-6-sun
export HADOOP_HOME=$HOME/yarn/hadoop
export HADOOP_MAPRED_HOME=$HOME/yarn/hadoop
export HADOOP_COMMON_HOME=$HOME/yarn/hadoop
export HADOOP_HDFS_HOME=$HOME/yarn/hadoop
export YARN_HOME=$HOME/yarn/hadoop
export HADOOP_CONF_DIR=$HOME/yarn/hadoop/etc/hadoop

sbin/hadoop-daemon.sh start namenode
sbin/hadoop-daemon.sh start datanode
sbin/yarn-daemon.sh start nodemanager
sbin/yarn-daemon.sh start resourcemanager
sbin/mr-jobhistory-daemon.sh start historyserver

jps



