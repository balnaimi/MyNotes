# Steps I've Used to create my own local repo on Ubuntu, For: Ubuntu 16.04 32 & 64, Raspberry Pi Stretch, Debian stretch 32 & 64, CentOS 7 64 only

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

# Change owner to local user

sudo chown -R aptmirror:aptmirror /data

# add apt-mirror use to same group as local user aptmirror, maybe you will need to relogin to make it take effect, I dont know

sudo usermod -a -G aptmirror apt-mirror

# We will create two main folders, one for debian based tool apt-mirror, and the other for yum

mkdir /data/apt-mirror

mkdir /data/yum-mirror

# Edit the file in /etc/apt/mirror.list, use my example at: https://github.com/bodaay/MyNotes/blob/master/Files/mirror.list

sudo nano /etc/apt/mirror.list

# Create the file centos.repos in /etc/yum/repos.d/centos.repo, use my example at: https://github.com/bodaay/MyNotes/blob/master/Files/centos.repo

sudo nano /etc/yum/repos.d/centos.repo

# Create update script for CentOS in home folder, and make it execute able, you can use my example code at: https://github.com/bodaay/MyNotes/blob/master/Files/UpdateCentOSRepos

cd ~
nano UpdateCentOSRepos

# Configure Apache, Create/edit the file /etc/apache2/sites-enabled/000-default.conf, use my example at https://github.com/bodaay/MyNotes/blob/master/Files/000-default.conf

sudo nano /etc/apache2/sites-enabled/000-default.conf

# Configure apache and create symbolic links for apt and yum

sudo ln -s /data/apt-mirror /var/www/apt
sudo ln -s /data/yum-mirror /var/www/yum


# In Clients Machines, Debian or Ubuntu, Change the sources.list to match the ip of the server hosting the files, For Repos with GPG key, you need to set [trusted=yes] in front of deb, to ignore GPG key check
example:


deb [trusted=yes]  http://192.168.100.56/apache/cassandra/debian 311x main

# you can download examples for sources file for client machine from: 
https://github.com/bodaay/MyNotes/tree/master/Files/ClientMachine

# if you are going to use mounted cifs share, use the following example, nobrl solve some issues with locked files

sudo mount.cifs -o username=aptmirror,password=aptmirror,nobrl,uid=$USER,gid=$USER,vers=3.0 //192.168.100.132/Repo /data

