import requests
from bs4 import BeautifulSoup

def get_shanghai_weather():
    url = 'http://www.weather.com.cn/weather/101020100.shtml'  # 上海天气页面

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 设置编码，防止中文乱码

    if response.status_code != 200:
        print(f'请求失败，状态码：{response.status_code}')
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # 未来7天天气信息在id="7d"的div中
    seven_day = soup.find('div', id='7d')
    if not seven_day:
        print('未找到7天天气信息')
        return

    ul = seven_day.find('ul')
    if not ul:
        print('未找到天气列表')
        return

    lis = ul.find_all('li')
    for li in lis:
        date = li.find('h1').text.strip()  # 日期
        weather = li.find('p', class_='wea').text.strip()  # 天气状况
        temp_high = li.find('span').text.strip() if li.find('span') else ''  # 最高温度
        temp_low = li.find('i').text.strip()  # 最低温度

        print(f'{date}：{weather}，最高温度：{temp_high}，最低温度：{temp_low}')

if __name__ == '__main__':
    get_shanghai_weather()
