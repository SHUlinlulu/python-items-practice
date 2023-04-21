"""
    测试使用cookie属性与session创建会话，会话期间cookie值保持
    session.post/session.get
    requests.post
    A(client)  -->  B(server)  带着：username, password
    B  -->  A  sever会给client创建一个人看不懂的cookie值,下次client再次访问sever时,带着cookie就能辨别身份
    A  -->  B
    A  -->  B  比如：session期间相当于创建了一连串的请求-连接,带着cookie值
    ...
# 案例：访问17k.com小说网，查看书架上的信息
# 登录 -> 得到cookie
# 带着cookie 去请求书架的url —> 书架上的内容

# 必须将上面的两个操作连起来才有意义
# solution:
# 1.session进行请求 -> session你可以看作是一连串的请求。在此过程中cookie不会丢失
"""
import requests
'''
    方式1: 通过session保存cookie的特性实现登录后方能完成的操作
'''
# session = requests.session()
# url = "https://passport.17k.com/ck/user/login"  # login的链接
# data = {
#     "loginName": "15055835469",
#     "password": "qq6666"
# }
# resp = session.post(url=url, data=data)
# # print(resp.json())
# # print(resp.cookies)  # 查看cookie
# # 拿书架上的数据
# # 刚刚的那个session中是有cookie的
# shelf_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
# shelf_resp = session.get(shelf_url)
# print(shelf_resp.text)

'''
    方式2: 通过headers中加入cookie属性,也可以访问登录后方能查看的页面信息
'''
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
headers = {
    "cookie": 'GUID=5d4c74ad-cfda-42a2-8b7a-e63a22ec3e5f; __bid_n=1879c4bce8aecb8ca84207; Hm_lvt_9793f42b498361373512'
              '340937deb2a0=1681954426,1682038458; c_channel=0; c_csc=web; FPTOKEN=Z8aTwpMRy3/466EpOBkLtpkAUYSUzcjMOQ'
              'HluO+Gq8OB1nB+NWh3ajpL7yre/EXcOnmglHhQKwYzDmlu6jnDlH1SpBCHASWMlGPY+FL4r7j7MUE2dV9Ppw1WPe5A/V5dt3Y+tr6M'
              'AlBJeTIkQ4aZ8aVvb0RhQdp3/FQLWo1geLKZlNNQdlxBTvNlCg2TwC/sUiAdIGkck05067SbCEVRcYM2VPS4sMEVJZQn4OsZ0kY3ZT'
              'CP+PLHeDB9qfrDigWwe68z3cldk5Y4PVgEN0WQqNd4G6mfzBuCaKgXgYExBj9q1PfLDRj6Mpzi+5/O9gBGfl4ViZWGuFjAeU1pTqjT'
              'qV6DSV5zd/+xcX2vbP2QhjHcmU1UMPoBd3BMPvE94GQEOwvhP8PQugiyrQYYKqKGRg==|EwuCPVmrBW5CZv1vWDviBLUK4pXyO9BK7'
              '4892gaMzAM=|10|74494279c2e192a0b53c511a36f6336c; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.stati'
              'c.17k.com%252Fuser%252Favatar%252F13%252F33%252F78%252F100167833.jpg-88x88%253Fv%253D1682038578000%26i'
              'd%3D100167833%26nickname%3Dlin_small_cat%26e%3D1697596639%26s%3Dd7b93ead1e424042; sensorsdata2015jssdk'
              'cross=%7B%22distinct_id%22%3A%22100167833%22%2C%22%24device_id%22%3A%221879c4bcdff513-0a076b682db2c5-2'
              '6031b51-921600-1879c4bce001b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%'
              'E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%2'
              '2%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%'
              '89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%225d4c74ad-cfda-42a2-8b7a-e63a22ec3e5f%22%7D; Hm_lpvt_9793f42'
              'b498361373512340937deb2a0=1682045160'
}
resp = requests.get(url=url, headers=headers)
print(resp.json())
