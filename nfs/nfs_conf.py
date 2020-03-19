#!/usr/bin/env python

import threading
import os
import shutil
import subprocess
import shlex

"""基本配置信息"""
NFSEXPORT_FILE = '/etc/exports'
NFSEXPORT_FILE_TMP = '/etc/exports.tmp'
NFSEXPORT_FILE_BAK = '/etc/exports.bak'

class Exportconfig():
    """
    NFS export entry对象，对象格式为：
    {
          share_path: share的路径
          share_clients: {
               share_ip1: share_options,
               share_ip2: share_options,
               ...
    }
           share_options包含permission，security，sync/async，fsid等，share_options以list定义

    """
    def __init__(self):
        """
        配置具有shares属性，是一个dictionary，shares的格式见以上
        """
        self.shares = {}

    def load(self):
        """
        获取当前NFS Export配置，并转换为dictionary
        :return:返回export文件的字典类型数据
        """
        Exportconfig_tmp(NFSEXPORT_FILE, NFSEXPORT_FILE_TMP)

        with open(NFSEXPORT_FILE_TMP, 'r') as nfsexport_fh:
            for line in nfsexport_fh.readlines():
                if line == "\n":
                    continue
                temp_fh = line.split()
                share_path = temp_fh[0]
                share = {}
                for share_info in temp_fh[1:]:
                    start_opt = share_info.find('(')
                    end_opt = share_info.find(')')
                    share_client = share_info[:start_opt]
                    share_opt = share_info[start_opt + 1 : end_opt]
                    share[share_client] = share_opt.split(',')
                self.shares[share_path] = share
        return self.shares

    def add_share(self, share):
        """
        将一个共享添加到shares共享变量中
        :param share:包含字段{share_path, share_clients:{permission, auth, fsid}}
        """
        share_path = share[share_path]
        #根据share path是否存在决定如何修改或增加
        #如果共享已经存在，则判断共享client是否存在，如果存在，则不做任何
        if share_path in self.shares:
            for share_host, share_opt in self.shares[share_path].items():
                if share_host not in share[share_clients]:
                    share[share_client][share_host] = share_opt

        else:
            self.shares[share_path] = share[share_clients]


    def remove_share(self, share_path):
        """
        在shares中找到对应的共享路径，删除
        :param share:
        :return:
        """
        #先检查共享是否存在
        if share_path in shares:
            del shares[share_path]
        else:
            print('The share path %s not exist', share_path)

    def modify_share(selfs, share):
        """

        :param share:
        :return:包含字段{share_path, share_clients:{permission, auth, fsid}}
        """
        share_path = share[share_path]
        #检查共享是否存在，如果存在则修改对应权限，如果不存在，则返回报错
        if share_path in self.shares:
            shares[share_path] = share[share_clients]
        else:
            print('The share path %s not exist', share_path)



    def update_nfs_exports():
        """备份nfs export配置文件"""
        Exportonfig_bak(NFSEXPORT_FILE, NFSEXPORT_FILE_BAK)

        """将shares转换为NFS export的文件格式"""
        configparse(NFSEXPORT_FILE_TMP)

        """如何确保修改的文件没有问题"""

        """替换当前NFS export文件并重启NFS service"""
        shutil.mv(NFSEXPORT_FILE_TMP, NFSEXPORT_FILE)
        subprocess.Popen(shlex.split("systemctl restart nfs"))

        """确认返回状态，即命令运行状态"""


    def configparse(self, tmp_file_path):
        """将shares转换为nfs export文件格式"""
        tmp_file = open(tmp_file_path, 'a')
        for share_path, share_opts in self.shares.items():
            share_entry = share_path
            for share_client in share_opts.keys():
                share_opt = share_opts[share_client]
                share_entry = "{} {}({})".format(share_entry, share_client, ','.join(share_opt) )
            share_entry += '\n'
            tmp_file.write(share_entry)
        tmp_file.close()


def Exportonfig_bak(nfsexport_file, nfsexport_file_bak):
    """备份配置文件，备份前确认文件是否存在"""
    if os.path.isfile(nfsexport_file):
        shutil.copy(nfsexport_file, nfsexport_file_bak)

def Exportconfig_tmp(nfsexport_file, nfsexport_file_tmp):
    """复制NFS export文件，复制前确认文件是否存在"""
    if os.path.isfile(nfsexport_file):
        shutil.copy(nfsexport_file, nfsexport_file_tmp)

def encap_share():
    """将界面或命令行输入的参数封装为share dictionary"""
    share = {}

    returen share

##test code
testshare = Exportconfig()
print(testshare.load())
print(testshare.shares)

print('/tmp' in testshare.shares)
