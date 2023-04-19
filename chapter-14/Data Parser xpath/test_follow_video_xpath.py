"""
    学习一些xpath的简单语法，为具体解析处理抓取的页面源代码做准备
    xpath是一门语言----在xml文件内搜索内容
    html是xml语言的一个子集
    <标签></标签>  ---- 在xml中都是一个个节点
        绝对路径
        /[html]  ---- 根节点
        父节点
        子节点
        相对路径
        ./
    xpath解析
        通过xml的节点之间的父子关系定位内容并予以输出
"""
# 安装lxml module
# pip install lxml
# xpath解析
from lxml import etree
# etree.XML().xpath(内容)
html = '''
    <!DOCTYPE html>
<html>
    <head>
        <title>My Website</title>
    </head>
    <body>
        <header>
          <h1>Welcome to my website!</h1>
          <nav>
            <ul>
              <li><a href="#about">About</a></li>
              <li><a href="#services">Services</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </nav>
        </header>
        <main>
          <section id="about">
            <h2>About Me</h2>
            <p>I am a web developer with 5 years of experience.</p>
          </section>
          <section id="services">
            <h2>My Services</h2>
            <ul>
              <li>Web design</li>
              <li>Web development</li>
              <li>SEO</li>
            </ul>
          </section>
          <section id="contact">
            <h2>Contact Me</h2>
            <form>
              <label for="name">Name:</label>
              <input type="text" id="name" name="name"><br><br>
              <label for="email">Email:</label>
              <input type="email" id="email" name="email"><br><br>
              <label for="message">Message:</label>
              <textarea id="message" name="message"></textarea><br><br>
              <input type="submit" value="Submit">
            </form>
          </section>
        </main>
        <footer>
          <p>&copy; 2021 My Website</p>
        </footer>
    </body>
</html>
'''
# etree.parser("文件名")  -- tree = etree.parser("index.html")
# etree.HTML(html : str)  --一定不能驴唇不对马嘴
# etree.XML(xml : str)
tree = etree.HTML(html)
# 定位节点title中的内容
result_1 = tree.xpath("/html/head/title/text()")  # /text()输出指定节点(<>内</>)内的文本
# 定位header节点下的所有li节点所在的行
result_2 = tree.xpath("/html/body/header//li")  # // 表示后代
# for li in result_2:
#     # 拿到每个li节点下a节点内的内容
#     result_3 = li.xpath("./a/text()")  # ./ 表示相对路径
#     print(result_3)

# 拿到body节点下id属性值为href="#about"的a节点并输出其中的文本
result_4 = tree.xpath("/html/body//a[@href='#about']/text()")  # 节点名[@属性名='属性值'] 输出特定属性值的节点信息
# print(result_4)

# 定位body节点下后代节点form下的所有label节点所在的行，然后根据[index] index从1开始输出特定序号下的节点信息
result_5 = tree.xpath("/html/body//form/label/text()")
result_6 = tree.xpath("/html/body//form/label[2]/text()")
# 输出特点节点的特定属性的属性值
result_7 = tree.xpath("/html/body//form/label/@for")  # /@属性名 输出特定节点下的特定属性名的属性值
print(result_5)
print(result_6)
print(result_7)
