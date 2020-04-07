import cephfs

#Conf_File = '/etc/ceph/ceph.conf'
cephfs_h = None

def setup_cephfs():
    ##与cephfs建立连接
    global cephfs_h
    cephfs_h = cephfs.LibCephFS(conffile='')
    cephfs_h.mount()

def unmount_cephfs():
    global cephfs_h
    cephfs_h.unmount()

def teardown_cephfs():
    global cephfs_h
    cephfs_h.shutdown()

def set_quota(path, value):
    global cephfs_h
    cephfs_h.setxattr(path, 'ceph.quota.max_bytes', value.encode('utf-8'), 1)



##对于新建共享，首先需要创建一个directory
def create_directory(path, perms):
    """
    :param path: 指定目录路径，从cephfs的根开始
    :param perms: 目录权限
    :return:
    """
    #当目录存在时，无法创建成功，需抛出异常信息
    global cephfs_h
    try:
        cephfs_h.mkdir(path, perms)
    except Exception:
        print("Error in mkdir. The directory %s Exists" %(path))






#setup_cephfs(Conf_File)
#创建一个文件夹， 在cephfs的root目录下，目录权限为777
#testcephfs.mkdir('/testpythonmake', 777)


##设置quota
##帮助文档中setxattr有3个参数，但实际会报错，最后一位参数不知道是什么，没有说明
##根据cephfs.pyx,最后一个参数为flags， "flags： set of option makes that control how the file is created/opened)
##如果flags为空，则cephfs_flags为readonly
"""
path = '/test0'
value = '1024000000'
testcephfs.setxattr(path, 'ceph.quota.max_bytes', value.encode('utf-8'), 1)
print(testcephfs.getxattr(path, 'ceph.quota.max_bytes'))

#获取子目录的容量quota
fsquota = testcephfs.getxattr(path, 'ceph.quota.max_bytes')
print(fsquota)
"""

###获取状态信息

#sstat = testcephfs.stat(path)
#print(fsstat)
"""
输出结果为：
StatResult(st_dev=18446744073709551614, st_ino=1099511627781, st_mode=17161, st_nlink=2, st_uid=0, st_gid=0,   24, 10, 26, 55), st_ctime=datetime.datetime(2020, 3, 24, 11, 28, 19))
st_dev
st_ino
st_mode
st
"""


