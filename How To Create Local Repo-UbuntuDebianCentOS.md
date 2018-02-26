# Steps I've Used to create my own local repo on Ubuntu, For: Ubuntu 16.04 32 & 64, Debian strech 32 & 64, CentOS 7 64 only

References:
First: 
https://blog.programster.org/set-up-a-local-ubuntu-mirror-with-apt-mirror

Second:
https://estl.tech/host-your-own-yum-and-apt-repository-4ba8350eeda1
*********************************************
                Preperation For Host
*********************************************

sudo apt install -y apache2 apt-mirror


sudo apt install -y createrepo yum-utils

# Choose a folder to host all data

sudo mkdir /data

# We will create two main folders, one for debian based tool apt-mirror, and the other for yum

sudo mkdir /data/apt-mirror

sudo mkdir /data/yum-mirror

# Create manually folders required for centOS repos, I'm including Cassandra 3.11 as well for all plateforms


sudo mkdir -p /data/yum-mirror/centos/7/os/x86_64/ /data/yum-mirror/centos/7/updates/x86_64/ /data/yum-mirror/centos/7/extras/x86_64/ /data/yum-mirror/apache/cassandra/redhat/311x/

# Edit the file in /etc/apt/mirror.list, use my example at: https://github.com/bodaay/MyNotes/blob/master/Files/mirror.list

sudo nano /etc/apt/mirror.list

# Create the file centos.repos in /etc/yum/repos.d/centos.repo, use my example at: https://github.com/bodaay/MyNotes/blob/master/Files/centos.repo

sudo nano /etc/yum/repos.d/centos.repo

# Create update script for CentOS in home folder, and make it execute able, you can use my example code at: https://github.com/bodaay/MyNotes/blob/master/Files/UpdateCentOSRepos

cd ~
nano UpdateCentOSRepos

# Configure Apache, Create/edit the file /etc/apache2/sites-enabled/000-default.conf, use my example at https://github.com/bodaay/MyNotes/blob/master/Files/000-default.conf

sudo nano /etc/apache2/sites-enabled/000-default.conf

# Change the ownership of main data folder and give it for apt-mirror user,

sudo chown -R apt-mirror:apt-mirror /data/

# Run apt-mirror, 
sudo su apt-mirror


apt-mirror



# then run the UpdateCentOSRepos script, again with same user apt-mirror


sudo su apt-mirror


./UpdateCentOSRepos

# In Clients Machines, Debian or Ubuntu, Change the sources.list to match the ip of the server hosting the files, For Repos with GPG key, you need to set [trusted=yes] in front of deb, to ignore GPG key check
example:


deb [trusted=yes]  http://192.168.100.56/apache/cassandra/debian 311x main

