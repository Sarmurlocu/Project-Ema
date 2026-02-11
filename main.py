import json
import random

def draw_poem(file_path):
    try:
        # 讀取你辛苦建立的資料庫
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 隨機抽取一則
        selected = random.choice(data)
        
        print("-" * 30)
        print(f"【Sarumurloc 實驗室 - 抽籤測試】")
        print(f"籤詩編號：第 {selected['id']} 籤")
        print(f"原文內容：{selected['poem']}")
        print("-" * 30)
        print(f"智慧導引：\n{selected['interpretation']}")
        print(f"\n風險提示 (Risk)：\n{selected['risk']}")
        print(f"\n內在價值 (VCP)：\n{selected['vcp']}")
        print("-" * 30)
        
    except Exception as e:
        print(f"發生錯誤了，可能是路徑不對：{e}")

# 執行抽籤
if __name__ == "__main__":
    # 確保你的路徑指向剛才建立的 json
    draw_poem('data/guanyin.json')
