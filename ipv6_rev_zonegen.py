# Script for forming the DNS list in BIND 9.x.x

#BASH Portion:
"""
for i in $(host -t axfr domain.tld ns1.localnet | grep -i "sshfp" | grep "1 1" | cut -f1 | grep -v nas | grep -v xen); do ssh -4 $i "hostname; ip -6 a show eth0 | grep -v fe80 | grep inet6 | cut -d \" \" -f6 | cut -d \"/\" -f1 | xargs host"; done | grep NXDOMAIN -B1 | egrep -e ezlink -e ip6 | cut -d "." -f1-6 >> ipv6_hosts.txt
"""
#0.1.0

a = list()
b = list()
ipv6list_edited = open("ipv6_hosts_edited.txt", "a")
ipv6list = open("ipv6_hosts.txt", "r")
for line in ipv6list.readlines():

    if line.startswith("Host"):
        a.append(line.rstrip().strip("Host "))
    else:
        b.append(line)

for i in range(len(a)):
    #z=a[i]," PTR ",b[i]
    #print z
    ipv6list_edited.write(a[i] + "   PTR   " + b[i])

#print len(a)
#print len(b)
