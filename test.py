####################################
# Crated:       Look at the stars  #
# Date:         2022/02/15         #
# Last edit:    2022/02/18         #
####################################

from bandApi import *

# 测试token，若token过期，则重新获取token
#######################################
userid = '346187'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJMb2dpbkluZm8iOnsiVXNlcklkIjozNDYxODcsIlVzZXJUeXBlIjoxMDAsIkFwcElkIjoyNTYsIk5hbWUiOiJhZG1pbiIsIlRpbWVPZmZzZXQiOjguMH0sImV4cCI6MTY0NTE5MzYyMC4wfQ.CD05X2vt5IRvRfiPbRbys6CbFDydVC0g96XdZQsRxQw'
#######################################
# ***使用时，将userid和token赋值 => 'null'
#######################################


# AppId:    '256'
# Appkey:   'CAA42412-E845-459E-879C-6993771157AD'

if userid == 'null' or token == 'null':
    print('get new token...')
    veri = verify('256', 'CAA42412-E845-459E-879C-6993771157AD')
    userid = veri.get_userid()
    token = veri.get_token()

health = get_health(userid, token)
loca = get_location(userid,token,'baidu')
print("今日步数 = %d" %(health.step()))
print("维度 = %f, 经度 = %f" %(loca.Lng(),loca.Lat()))