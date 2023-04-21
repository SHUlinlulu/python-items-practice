"""
    防盗链(referer),简而言之就是当前访问链接的父链接,"溯源"得能找得到
    案例：梨视频的视频爬取
    solution:
    观察、仔细、规律、拼接--->Results
"""
# contId:1723776
# https://video.pearvideo.com/mp4/adshort/20210318/cont-1723776-15634489_adpkg-ad_hd.mp4
# systemTime:"1682059191418"
# https://video.pearvideo.com/mp4/adshort/20210318/1682059191418-15634489_adpkg-ad_hd.mp4
import requests
# 1. 拿到contId
domain = "https://www.pearvideo.com/video_1723776"
contId = domain.split("_")[1]  # 进行切片取元素
# 2. 访问视频资源链接
url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.24016403550226317"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like"
                  " Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Referer": domain
}
resp = requests.get(url=url, headers=headers)
# 加入了请求头信息，而结果显示文章仍是下架，通过浏览器明明访问得到---->表明该网站还有反扒措施
# 查看headers中可以利用的东西----referer是个不错的选择
# print(resp.json())  # {'resultCode': '5', 'resultMsg': '该文章已经下线！', 'systemTime': '1682060334941'}
dic = resp.json()
systemTime = dic['systemTime']
srcUrl = dic["videoInfo"]['videos']['srcUrl']
print(srcUrl)
src = srcUrl.replace(systemTime, f"cont-{contId}")
video_resp = requests.get(src)
video_name = src.split("_")[-1].replace("hd", contId)
with open("videos/" + video_name, mode="wb") as video_file:
    video_file.write(video_resp.content)

video_resp.close()
resp.close()
