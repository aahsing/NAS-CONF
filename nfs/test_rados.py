import rados

##设置ceph集群配置文件
Conf_File = '/etc/ceph/ceph.conf'

##与ceph rados建立连接

##方法一
"""
with rados.Rados(conffile=Conf_File) as cluster:
    ##获取ceph集群pool信息
    pools = cluster.list_pools()
    print(pools)

"""

##方法二
cluster = rados.Rados(conffile=Conf_File)
cluster.connect()
##获取ceph集群pool信息
pools = cluster.list_pools()
print(pools)
"""output: ['cephfs_data', 'cephfs_metadata', '.rgw.root', 'default.rgw.control', 'default.rgw.meta', 'default.rgw.log', 
'cephfs.cephfs_vol.meta', 'cephfs.cephfs_vol.data', 'cephfs.testvol.meta', 'cephfs.testvol.data']
"""
#获取cephfs metadata pool
meta_pool = [p for p in pools if 'metadata' in p][0]

"""
ioctx：input/output context，对ceph storage cluster进行读取和写入操作时需要一个ioctx。
ioctx可以通过open_ioctx或者open_ioctx2创建。
open_ioctx的ioctx name为pool name
open_ioctx2里面参数为pool id

"""
"""
with cluster.open_ioctx(meta_pool) as ioctx:
    with rados.ReadOpCtx(ioctx) as read_op:
        ret = ioctx.get_omap_keys(read_op, "", 2)
    print(ret)
"""

ioctx = cluster.open_ioctx('cephfs_metadata')
#cephfs_metadata pool里面创建一个key为hw，内容为hello world的对象
ioctx.write_full("hw", b"Hello World")
print(ioctx.read("hw"))

#ioctx = cluster.open_ioctx2(2)

##对象创建完成，可对对象进行扩展属性进行设置或获取
ioctx.set_xattr("hw", "lang", b"en_US")
print(ioctx.get_xattr("hw", "lang"))

##list object
object_iterator = ioctx.list_objects()
for i in object_iterator:
    print(i.key)
    print(i.nspace)
    print(ioctx.read(i.key))

##删除之前创建的对象hw
ioctx.remove_object("hw")
ioctx.close()

##获取集群状态信息
#print(cluster.get_cluster_stats())
"""output: {'kb': 100638720, 'kb_used': 6425472, 'kb_avail': 94213248, 'num_objects': 212}"""


##结束前断开连接
cluster.shutdown()

