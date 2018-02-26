#Steps I've Used to create my own local repo on Ubuntu

For: Ubuntu, Debian, CentOS

*********************************************
                Preperation For Host
*********************************************

sudo apt install apache2 apt-mirror
sudo apt install -y createrepo yum-utils

# Choose a folder to host all data

sudo mkdir /data

# We will create two main folders, one for debian based tool apt-mirror, and the other for yum

sudo mkdir /data/apt-mirror
sudo mkdir /data/yum-mirror

# Create manually folders required for centOS repos, I'm including Cassandra 3.11 as well for all plateforms
sudo mkdir -p /data/yum-mirror/centos/7/os/x86_64/ /data/yum-mirror/centos/7/updates/x86_64/ /data/yum-mirror/centos/7/extras/x86_64/ /data/yum-mirror/apache/cassandra/redhat/311x/

# Edit the file sources.list in /etc/apt/mirror.list, use my example at: https://github.com/bodaay/MyNotes/blob/master/Files/mirror.list

sudo nano /etc/apt/mirror.list

# Create the file centos.repos in /etc/yum/repos.d/centos.repo, use my example at: https://github.com/bodaay/MyNotes/blob/master/Files/centos.repo

sudo nano /etc/yum/repos.d/centos.repo

