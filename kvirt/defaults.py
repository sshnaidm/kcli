# coding=utf-8
UBUNTUS = ['utopic', 'vivid', 'wily', 'xenial', 'yakkety', 'zesty', 'artful', 'bionic', 'cosmic', 'eoan', 'focal',
           'groovy', 'hirsute', 'impish', 'jammy', 'kinetic']
VERSION = "99.0"
NETS = ['default']
POOL = 'default'
IMAGE = None
CPUMODEL = 'host-model'
NUMCPUS = 2
CPUHOTPLUG = False
CPUFLAGS = []
MEMORY = 512
MEMORYHOTPLUG = False
DISKINTERFACE = 'virtio'
DISKTHIN = True
DISKSIZE = 10
DISKS = [{'size': DISKSIZE, 'default': True}]
GUESTID = 'guestrhel764'
VNC = True
CLOUDINIT = True
RESERVEIP = False
RESERVEDNS = False
RESERVEHOST = False
NESTED = True
START = True
AUTOSTART = False
TUNNEL = False
TUNNELHOST = None
TUNNELUSER = 'root'
TUNNELDIR = '/var/www/html'
TUNNELPORT = 22
VMUSER = None
VMPORT = None
OPENSHIFT_TAG = '4.12'
ALMA = 'http://repo.ifca.es/almalinux/'
BSD = "https://object-storage.public.mtl1.vexxhost.net/swift/v1/1dbafeefbd4f4c80864414a441e72dd2"
BSD += "/bsd-cloud-image.org/images/dragonflybsd/"
CENTOS = 'https://cloud.centos.org/centos/'
DEBIAN = "https://cdimage.debian.org/cdimage/"
FEDORA = "http://mirror.uv.es/mirror/fedora/linux/releases/"
FEDORA_ARCHIVE = "https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/"
GENTOO = "https://gentoo.osuosl.org/experimental/amd64/openstack/"
OPENSUSE = "https://download.opensuse.org/"
LEAP = OPENSUSE + "distribution/leap/"
LEAP_MIC = OPENSUSE + "distribution/leap-micro/"
RHCOS = "https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/"
ROCKY = 'https://dl.rockylinux.org/pub/rocky/'
UBUNTU = 'https://cloud-images.ubuntu.com/'
IMAGES = {'almalinux9': ALMA + '9.1/cloud/x86_64/images/AlmaLinux-9-GenericCloud-latest.x86_64.qcow2',
          'arch': 'https://linuximages.de/openstack/arch/arch-openstack-LATEST-image-bootstrap.qcow2',
          'centos7': CENTOS + '7/images/CentOS-7-x86_64-GenericCloud.qcow2',
          'centos8stream': CENTOS + '8-stream/x86_64/images/CentOS-Stream-GenericCloud-8-20210603.0.x86_64.qcow2',
          'centos9stream': CENTOS + '9-stream/x86_64/images/CentOS-Stream-GenericCloud-9-20211203.0.x86_64.qcow2',
          'cirros': 'http://download.cirros-cloud.net/0.5.2/cirros-0.5.2-x86_64-disk.img',
          'debian8': DEBIAN + 'openstack/archive/8.11.0/debian-8.11.0-openstack-amd64.qcow2',
          'debian9': DEBIAN + 'openstack/current-9/debian-9-openstack-amd64.qcow2',
          'debian10': DEBIAN + 'openstack/current-10/debian-10-openstack-amd64.qcow2',
          'debian11': DEBIAN + 'cloud/bullseye/latest/debian-11-generic-amd64.qcow2',
          'fcos': 'https://builds.coreos.fedoraproject.org/streams/stable.json',
          'fedora32': FEDORA_ARCHIVE + '32/Cloud/x86_64/images/Fedora-Cloud-Base-32-1.6.x86_64.qcow2',
          'fedora33': FEDORA_ARCHIVE + '33/Cloud/x86_64/images/Fedora-Cloud-Base-33-1.2.x86_64.qcow2',
          'fedora34': FEDORA_ARCHIVE + '34/Cloud/x86_64/images/Fedora-Cloud-Base-34-1.2.x86_64.qcow2',
          'fedora35': FEDORA_ARCHIVE + '35/Cloud/x86_64/images/Fedora-Cloud-Base-35-1.2.x86_64.qcow2',
          'fedora36': FEDORA_ARCHIVE + '36/Cloud/x86_64/images/Fedora-Cloud-Base-36-1.5.x86_64.qcow2',
          'fedora37': FEDORA + '37/Cloud/x86_64/images/Fedora-Cloud-Base-37-1.7.x86_64.qcow2',
          'fedoralatest': 'https://alt.fedoraproject.org/cloud',
          'freebsd122': BSD + "freebsd/12.2/freebsd-12.2.qcow2",
          'freebsd130': BSD + "freebsd/13.0/freebsd-13.0-zfs.qcow2",
          'netbsd82': BSD + "netbsd/8.2/netbsd-8.2.qcow2",
          'netbsd92': BSD + "netbsd/9.2/2021-12-11/netbsd-9.2.qcow2",
          'openbsd71': BSD + "openbsd/7.1/2022-06-27/ufs/openbsd-7.1-2022-06-27.qcow2",
          'openbsd72': BSD + "openbsd/7.2/2022-11-06/ufs/openbsd-7.2-2022-11-06.qcow2",
          'dragonflybsd601': BSD + "dragonflybsd/6.0.1/2021-12-11/dragonflybsd-6.0.1-hammer2.qcow2",
          'dragonflybsd622': BSD + 'dragonflybsd/6.2.2/2022-09-06/hammer2/dragonflybsd-6.2.2-hammer2-2022-09-06.qcow2',
          'gentoo': GENTOO + 'gentoo-openstack-amd64-default-latest.qcow2',
          'opensuse152': LEAP + '15.2/appliances/openSUSE-Leap-15.2-JeOS.x86_64-OpenStack-Cloud.qcow2',
          'opensuse153': LEAP + '15.3/appliances/openSUSE-Leap-15.3-JeOS.x86_64-OpenStack-Cloud.qcow2',
          'opensuse154': LEAP + '15.4/appliances/openSUSE-Leap-15.4-JeOS.x86_64-OpenStack-Cloud.qcow2',
          'tumbleweed': OPENSUSE + 'tumbleweed/appliances/openSUSE-Tumbleweed-JeOS.x86_64-OpenStack-Cloud.qcow2',
          'opensusemicro': OPENSUSE + 'tumbleweed/appliances/openSUSE-MicroOS.x86_64-OpenStack-Cloud.qcow2',
          'rhcos46': RHCOS + '4.6',
          'rhcos47': RHCOS + '4.7',
          'rhcos48': RHCOS + '4.8',
          'rhcos49': RHCOS + '4.9',
          'rhcos410': RHCOS + '4.10',
          'rhcos411': RHCOS + '4.11',
          'rhcos412': RHCOS + '4.12',
          'rhcos413': RHCOS + 'pre-release/latest-4.13/rhcos-4.13.0-ec.3-x86_64-openstack.x86_64.qcow2.gz',
          'rhcoslatest': RHCOS + 'pre-release/latest-4.13/rhcos-openstack.x86_64.qcow2.gz',
          'rhel7': 'https://access.redhat.com/downloads/content/69/ver=/rhel---7',
          'rhel8': 'https://access.redhat.com/downloads/content/479/ver=/rhel---8',
          'rhel9': 'https://access.redhat.com/downloads/content/479/ver=/rhel---9',
          'ubuntu1804': UBUNTU + 'releases/bionic/release/ubuntu-18.04-server-cloudimg-amd64.img',
          'ubuntu1810': UBUNTU + 'releases/cosmic/release/ubuntu-18.10-server-cloudimg-amd64.img',
          'ubuntu1904': UBUNTU + 'releases/19.04/release/ubuntu-19.04-server-cloudimg-amd64.img',
          'ubuntu1910': UBUNTU + 'releases/19.10/release/ubuntu-19.10-server-cloudimg-amd64.img',
          'ubuntu2004': UBUNTU + 'releases/20.04/release/ubuntu-20.04-server-cloudimg-amd64.img',
          'ubuntu2010': UBUNTU + 'releases/20.10/release/ubuntu-20.10-server-cloudimg-amd64.img',
          'ubuntu2104': UBUNTU + 'releases/21.04/release/ubuntu-21.04-server-cloudimg-amd64.img',
          'ubuntu2110': UBUNTU + 'releases/21.10/release/ubuntu-21.10-server-cloudimg-amd64.img',
          'ubuntu2204': UBUNTU + 'releases/22.04/release/ubuntu-22.04-server-cloudimg-amd64.img',
          'ubuntu2210': UBUNTU + 'releases/22.10/release/ubuntu-22.10-server-cloudimg-amd64.img',
          'rockylinux8': ROCKY + '8/images/Rocky-8-GenericCloud.latest.x86_64.qcow2',
          'rockylinux9': ROCKY + '9/images/x86_64/Rocky-9-GenericCloud.latest.x86_64.qcow2'}

IMAGESCOMMANDS = {'debian8': 'echo datasource_list: [NoCloud, ConfigDrive, Openstack, Ec2] > /etc/cloud/cloud.cfg.d/'
                  '90_dpkg.cfg'}
INSECURE = True
KEYS = []
CMDS = []
SCRIPTS = []
FILES = []
DNS = None
DOMAIN = None
ISO = None
GATEWAY = None
NETMASKS = []
SHAREDKEY = False
ENABLEROOT = True
PLANVIEW = False
PRIVATEKEY = False
TEMPKEY = False
TAGS = []
NETWORKWAIT = 0
RHNREGISTER = True
RHNUNREGISTER = False
RHNSERVER = "https://subscription.rhsm.redhat.com"
RHNUSER = None
RHNPASSWORD = None
RHNAK = None
RHNORG = None
RHNPOOL = None
FLAVOR = None
KEEP_NETWORKS = False
DNSCLIENT = None
STORE_METADATA = False
NOTIFY = False
PUSHBULLETTOKEN = None
SLACKTOKEN = None
MAILSERVER = None
MAILFROM = None
MAILTO = []
NOTIFYCMD = None
NOTIFYSCRIPT = None
SLACKCHANNEL = None
NOTIFYMETHODS = ['pushbullet']
SHAREDFOLDERS = []
KERNEL = None
INITRD = None
CMDLINE = None
PLACEMENT = []
YAMLINVENTORY = False
CPUPINNING = []
NUMAMODE = None
NUMA = []
PCIDEVICES = []
TPM = False
RNG = False
JENKINSMODE = "podman"
FAKECERT = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5gvbJA3nzoIEF
5R+G3Vy1XwzKoGX7uoRPstBSgEQ967n7Y3WC3JT0r7Uq8Wyudm/8sEhK6PNFkarV
zsRZrszUF/qvLzIAg8wc7c2q3jlD1nYG8U6ngnSgcJxJdGKdYDraXwCPAbNjRd+8
KimOxGolOb57iWoZTwprNJ0B9gmfIo2i+f/rLlBJtOtITPypkt0GyRQaTD3zMEMd
azJcy3wCj1RfZ97oG9C2h6rcA0P+NEUqwwnKL/dIaJl+SJRp9GXrrVhIx+rN+lnN
dT6BzLEBGZ2IXG0Y6YxRDdMGMgVl2m78uMi0wxnOkAu7vg6jppqInNLakOexR0R4
qp7W+OCnAgMBAAECggEAKc5CsSAQbn/AM8Tjqu/dwZ3O8ybcdLMeuBsy6TSwrEeg
HO/X/oqZIt8p86h+dn6IVCih0gfXMtlV52L2SsOiszVIMAxxtz38VJSeoZ/8xbXh
2USuFf/HKpTWE5Of2ZljCe0Y4iFe/MM1XWEfBmZrCUKPE6Xu/A8c6PXtYBDDMFIl
puX8CtUDyvY3+mcprFM2z7bDLlwxAdBgfKAR84F3RazRB3KlgaqCR+KVrhVnFkBZ
ApWnkwGjxj8NrKj9JArGLwiTKeQg7w1jJGdPQwCDi14XZYFHsPEllQ3hBIJzOmAS
vHkr6DdyT6L25UY6mYfjyJy2ZIqvUObCTkTgJJ4pyQKBgQDpb3qiPpEpHipod2w+
vLmcGGnYX8K1ikplvUT1bPeRXZyzWEC3CHpK+8lktVNU3MRklyNaQJIR6P5iyP/c
C46IyPHszYnHFHGwx+hG2Ibqd1RcfjOTz04Y4WxJB5APTB24aWTy09T5k48X+iu9
Ifeqxd9cdmKiLf6CDRxvUE4r1QKBgQDLcZNRY08fpc/mAV/4H3toOkiCwng10KZ0
BZs2aM8i6CGbs7KAWy9Cm18sDW5Ffhy9oh7XnmVkaaULmrwdCrIGFLsR282c4izx
3HHhfHOl6xri2xq8XwjMruzjELiIw2A8iZZssQxzV/sRHXjf9VMdcYGXlK3HrZOw
ZIg7qxjEiwKBgQDEtIzZVPHLfUDtIN0VDME3eRcQHrmbcrn4e4I1cao4U3Ltacu2
sK0krIFrnKRo2VOhE/7VWZ38+6IJKij4isCEIRhDnHuiR2b6OapQsLsXrpBnFG1v
+3tq2eH+tCG/0jslH6LSQJCx8pbc9JGQ4aOqwuzSJGw/D5TskBHK9xe4NQKBgQCQ
FYUffDUaleWS4WBlq25MWBLowPBANODehOXzd/FTqJG841zFeU8UXlPeMDjr8LBM
QdiUHvNyVTv15wXZj6ybj+0ZbdHGjY0FUno5F1oUpVjqWAEsbiYeSLku67W17qFm
3o7xtca6nhILghMMkoPl83CzuTIGnFFf+SNfFwM4lwKBgFs5cPPw51YYwYDhhCqE
EewsK2jgc1ZqIbrGA5CbtfMIc5rhTuuJ9aWfpfF/kgUp9ruVklMrEcdTtUWn/EDA
erBsSfYdgXubBAajSxm3wFHk6bgGvKGT48++DnJWL+SFbmNhh5x9xRtMHR17K1nq
KpxLjDMW1gGkb22ggyP5MnJz
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDIDCCAggCCQC/KT3ImT8lHTANBgkqhkiG9w0BAQsFADBSMQswCQYDVQQGEwJF
UzEPMA0GA1UECAwGTWFkcmlkMQ8wDQYDVQQHDAZNYWRyaWQxEjAQBgNVBAoMCUth
cm1hbGFiczENMAsGA1UEAwwEa2NsaTAeFw0xOTA5MzAxMzM2MTBaFw0yOTA5Mjcx
MzM2MTBaMFIxCzAJBgNVBAYTAkVTMQ8wDQYDVQQIDAZNYWRyaWQxDzANBgNVBAcM
Bk1hZHJpZDESMBAGA1UECgwJS2FybWFsYWJzMQ0wCwYDVQQDDARrY2xpMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuYL2yQN586CBBeUfht1ctV8MyqBl
+7qET7LQUoBEPeu5+2N1gtyU9K+1KvFsrnZv/LBISujzRZGq1c7EWa7M1Bf6ry8y
AIPMHO3Nqt45Q9Z2BvFOp4J0oHCcSXRinWA62l8AjwGzY0XfvCopjsRqJTm+e4lq
GU8KazSdAfYJnyKNovn/6y5QSbTrSEz8qZLdBskUGkw98zBDHWsyXMt8Ao9UX2fe
6BvQtoeq3AND/jRFKsMJyi/3SGiZfkiUafRl661YSMfqzfpZzXU+gcyxARmdiFxt
GOmMUQ3TBjIFZdpu/LjItMMZzpALu74Oo6aaiJzS2pDnsUdEeKqe1vjgpwIDAQAB
MA0GCSqGSIb3DQEBCwUAA4IBAQAs7eRc4sJ2qYPY/M8+Lb2lMh+qo6FAi34kJYbv
xhnq61/dnBCPmk8JzOwBoPVREDBGmXktOwZb88t8agT/k+OKCCh8OOVa5+FafJ5j
kShh+IkztEZr+rE6gnxdcvSzUhbfet97nPo/n5ZqtoqdSm7ajnI2iiTI+AXOJAeN
0Y29Dubv9f0Vg4c0H1+qZl0uzLk3mooxyRD4qkhgtQJ8kElRCIjmceBkk+wKOnt/
oEO8BRcXIiXiQqW9KnF99fXOiQ/cKYh3kWBBPnuEOhC77Ke5aMlqMNOPULf3PMix
2bqeJlbpLt7PkZBSawXeu6sAhRsqlpEmiPGn8ujH/oKwIAgm
-----END CERTIFICATE-----"""
VIRTTYPE = None
ZEROTIER_NETS = []
ZEROTIER_KUBELET = False
METADATA_FIELDS = ['dnsclient', 'domain', 'image', 'kube', 'kubetype', 'loadbalancer', 'owner', 'plan', 'profile',
                   'user']
VMRULES = []
VMRULES_STRICT = False
CACHE = False
SECURITYGROUPS = []
LOCAL_OPENSHIFT_APPS = ['argocd', 'istio', 'users', 'autolabeller', 'nfs']
SSH_PUB_LOCATIONS = ['id_ed25519.pub', 'id_ecdsa.pub', 'id_dsa.pub', 'id_rsa.pub']
ROOTPASSWORD = None
WAIT = False
WAIT = False
WAITTIMEOUT = 0
WAITCOMMAND = None
BMC_USER = None
BMC_PASSWORD = None
BMC_MODEL = None

KSUSHYSERVICE = """[Unit]
Description=Ksushy emulator service
After=syslog.target
[Service]
Environment=HOME={home}
Environment=PYTHONUNBUFFERED=true
{ipv6}
{ssl}
{user}
{password}
Type=simple
ExecStart=/usr/bin/ksushy
StandardOutput=syslog
StandardError=syslog"""

WEBSERVICE = """[Unit]
Description=Kweb service
After=syslog.target
[Service]
Environment=HOME={home}
Environment=PYTHONUNBUFFERED=true
{ipv6}
Type=simple
ExecStart=/usr/bin/kweb
StandardOutput=syslog
StandardError=syslog"""

PLANTYPES = ['ansible', 'bucket', 'cluster', 'container', 'disk', 'dns', 'image', 'kube', 'loadbalancer', 'network',
             'plan', 'pool', 'profile', 'securitygroup', 'vm', 'workflow']
