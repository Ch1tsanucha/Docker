service ssh start

cd /root

mkdir -p ~/.ssh

cd .ssh

ssh-keygen -t rsa -f id_rsa -q -N ""

cat id_rsa.pub >> authorized_keys