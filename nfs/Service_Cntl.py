import subprocess

### NFS Service control
#restart nfs service
def NFS_Restart():
    subprocess.run(["systemctl", "restart", "nfs-server"])

