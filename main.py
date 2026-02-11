import json
import random
import os

# 1. 安全攔截邏輯 (VCP 過濾器)
def safety_filter(user_input):
    danger_zone = ["想不開", "絕望", "沒意義", "終結"]
    if any(word in user_input for word in danger_zone):
        return True
    return False

# 2. 抽籤核心邏輯
def draw_poem(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
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
        print(f"發生錯誤了：{e}")

# 3. 程式進入點
if __name__ == "__main__":
    # 路徑設定
    base_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_path, 'data', 'guanyin.json')
    
    # 使用者互動
    print("【Sarumurloc 靈魂導引系統】")
    user_feeling = input("在尋求導引前，請簡述您現在的心情或困擾：")

    # 執行過濾邏輯
    if safety_filter(user_feeling):
        print("\n【Sarumurloc 溫馨提醒】")
        print("當風暴過大時，我們不急著尋找方向，先讓心靈在雨露中稍作休息。")
        print("現在的您需要的不是籤詩的指引，而是給自己一個擁抱。建議找信任的朋友聊聊。")
    else:
        draw_poem(json_path)
