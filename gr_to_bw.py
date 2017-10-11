from PIL import Image
import numpy as np

UserInput = input("請將檔案放置於專案內並且輸入檔案名稱:\r\n")
# 開啟圖檔
try:
    im = Image.open(UserInput)
except FileNotFoundError:
    print("找不到此檔案請重新輸入!")
    exit(0)

# 轉成灰階
im = im.convert("L")
# 轉成矩陣
b_and_w_jobs = np.asarray(im).copy()

for i, bt in enumerate(b_and_w_jobs):
    for j, b in enumerate(bt):
        # < 128 設成黑色
        if(b < 128):
            b_and_w_jobs[i][j] = 0
        # 其他設成白色
        else:
            b_and_w_jobs[i][j] = 255
#Debug 用
print(im.format, im.size, im.mode)
print(b_and_w_jobs)

# 從陣列讀成Image Object
bw_jobs = Image.fromarray(b_and_w_jobs)
# 存檔
bw_jobs.save("bw_" + UserInput)






