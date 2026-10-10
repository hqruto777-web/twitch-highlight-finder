import json
import pandas as pd
import matplotlib.pyplot as plt

# チャットログを読み込む
with open("data/chat.json", encoding="utf-8") as f:
    data = json.load(f)

# 各コメントの「配信開始から何秒後か」を取り出す
seconds = [c["content_offset_seconds"] for c in data["comments"]]

# 1分ごとのコメント数を数える
df = pd.DataFrame({"sec": seconds})
df["minute"] = df["sec"] // 60
per_minute = df.groupby("minute").size()

# グラフにして保存・表示
per_minute.plot(figsize=(14, 4))
plt.xlabel("minute")
plt.ylabel("comments")
plt.savefig("chat_volume.png")
plt.show()

# コメントが多かった上位10分
print(per_minute.sort_values(ascending=False).head(10))