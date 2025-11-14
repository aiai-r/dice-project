import tkinter as tk
import random

# こんにちは 
# --- メインとなる処理 ---

def roll_dice():
    """サイコロを振って結果をラベルに表示する"""
    result = random.randint(1, 6)
    result_label.config(text=f"{result}")

def reset_display():
    """表示を '?' に戻す (リセット機能)"""
    result_label.config(text="?")

# --- 画面（GUI）の作成 ---

# 1. メインウィンドウの作成
window = tk.Tk()
window.title("サイコロツール")
window.geometry("300x250")

# 2. 結果を表示するラベル
result_label = tk.Label(
    window,
    text="?",
    font=("Helvetica", 60, "bold"),
    pady=30
)
result_label.pack()

# 3. ボタンをまとめるためのフレーム (横並びにするため)
button_frame = tk.Frame(window)
button_frame.pack()

# 4. 「振る」ボタン
roll_button = tk.Button(
    button_frame, # 配置先を button_frame に変更
    text="振る",
    font=("Helvetica", 20),
    command=roll_dice
)
roll_button.pack(side=tk.LEFT, padx=10) # 左から詰めて配置

# 5. 「リセット」ボタン (★追加された機能)
reset_button = tk.Button(
    button_frame, # 配置先を button_frame に変更
    text="リセット",
    font=("Helvetica", 20),
    command=reset_display # クリックされたら reset_display を実行
)
reset_button.pack(side=tk.LEFT, padx=10) # 左から詰めて配置

# 6. GUIの実行
window.mainloop()
