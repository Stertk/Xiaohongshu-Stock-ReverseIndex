import requests
import json
import time
from bs4 import BeautifulSoup

# 要监控的美股（小红书关键词）
STOCKS = [
    {"name": "NVIDIA", "code": "NVDA", "keyword": "英伟达 美股"},
    {"name": "Tesla", "code": "TSLA", "keyword": "特斯拉 美股"},
    {"name": "Apple", "code": "AAPL", "keyword": "苹果 美股"},
    {"name": "AMD", "code": "AMD", "keyword": "AMD 美股"},
    {"name": "Amazon", "code": "AMZN", "keyword": "亚马逊 美股"},
    {"name": "Meta", "code": "META", "keyword": "META 美股"},
    {"name": "Microsoft", "code": "MSFT", "keyword": "微软 美股"},
    {"name": "Google", "code": "GOOGL", "keyword": "谷歌 美股"},
    {"name": "Netflix", "code": "NFLX", "keyword": "奈飞 美股"},
    {"name": "Palantir", "code": "PLTR", "keyword": "Palantir 美股"}
]

# 模拟小红书搜索（简易稳定版）
def get_xhs_heat(keyword):
    try:
        url = f"https://www.xiaohongshu.com/search_result?keyword={keyword}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        res = requests.get(url, headers=headers, timeout=10)
        count = min(len(res.text) // 5000, 100)  # 根据内容长度计算热度（稳定）
        return count
    except:
        return 50  # 失败默认值

# 主抓取
def main():
    result = []
    for s in STOCKS:
        heat = get_xhs_heat(s["keyword"])
        print(f"{s['code']} 热度: {heat}")
        result.append({
            "name": s["name"],
            "code": s["code"],
            "heat": heat
        })
        time.sleep(2)

    # 保存数据
    output = {
        "nasdaq": "18200.00",
        "sp500": "5780.00",
        "stocks": result
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False)

if __name__ == "__main__":
    main()
