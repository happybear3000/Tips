import hashlib

server_ip_list = ["192.168.1.10", "192.168.2.20", "192.168.3.30","192.168.4.40"]
client_ip_list = ["113.88.97.173", "106.11.154.33", "207.46.13.149","42.156.137.120", "203.208.60.0", "119.39.47.182", "171.34.179.4", "111.175.58.52", "124.235.138.199","175.184.166.184","111.175.58.52", "124.235.18.119","175.144.163.124","175.14.166.114","111.175.8.152", "124.23.18.113","175.144.13.116"]

def get_md5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

def get_ip():
    virtual_nodes = 500
    node_dict = {}
    # 遍历服务器ip，生成对应的虚拟结点
    for serverip in server_ip_list:
        for i in range(virtual_nodes):
            # serverip加上一些动态参数生成md5值
            hash_key = get_md5(str('{0}VN{1}'.format(serverip,i)))
            node_dict[hash_key]=serverip
    # 将node_dict字典按key排序生成列表
    sorted_key_list = sorted(node_dict)
    # 将node_dict字典按key排序
    node_dict = sorted(node_dict.items(),key=lambda d:d[0],reverse=False)

    for clientip in client_ip_list:
        selected_key_list = []
        # clientip生成md5值
        hc = get_md5(str(clientip))
        #print(hc)
        switch = 0
        for key in sorted_key_list:
            #print(key)
            # clientip和sorted_key_list中的md5值做比较，clientip的md5值小于等于sorted_key_list中的md5值,switch=1
            if hc <= key:
                selected_key_list.append(key)
                switch=1
        if switch == 0:
            firstkey = sorted_key_list[0]
        else:
            firstkey = selected_key_list[0]
        print("{0}请求的服务器ip为:{1}".format(clientip,dict(node_dict)[firstkey]))

# for i in range(2):
get_ip()