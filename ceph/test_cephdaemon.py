import ceph_daemon

##测试通过python操作ceph daemon
##ceph的admin socket是daemon的asok文件，通常在/var/run/ceph目录下

"""
[root@node0 group_vars]# ll /var/run/ceph/ceph-*
srwxr-xr-x 1 ceph ceph 0 Mar 25 12:30 /var/run/ceph/ceph-client.rgw.node0.rgw0.2794.93862144803448.asok
srwxr-xr-x 1 ceph ceph 0 Mar 25 12:05 /var/run/ceph/ceph-mds.node0.asok
srwxr-xr-x 1 ceph ceph 0 Mar 25 12:05 /var/run/ceph/ceph-mgr.node0.asok
srwxr-xr-x 1 ceph ceph 0 Mar 25 12:05 /var/run/ceph/ceph-mon.node0.asok
srwxr-xr-x 1 ceph ceph 0 Mar 25 12:05 /var/run/ceph/ceph-osd.0.asok
srwxr-xr-x 1 ceph ceph 0 Mar 25 12:05 /var/run/ceph/ceph-osd.3.asok
"""
