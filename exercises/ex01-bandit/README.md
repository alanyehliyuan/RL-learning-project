# Exercise 01 — 10-Armed Bandit with Epsilon-Greedy

## Goal

實作最小版本的 bandit 問題，並理解 epsilon-greedy 的效果。

## What you need to do

1. 建立一個 10-armed bandit environment
2. 每個 arm 都有自己的真實 reward mean
3. 每次 pull 某個 arm 時，從對應分布取樣 reward
4. 實作 epsilon-greedy agent
5. 跑多次實驗並畫圖

## Deliverables

- `starter.py` 補完後可執行
- 能輸出平均 reward 曲線
- 你能解釋 epsilon 對學習行為的影響

## Questions to answer

1. 如果 epsilon = 0，會發生什麼事？
2. 為什麼只看短期 reward 可能會誤導？
3. 為什麼增加 exploration 有時反而讓長期表現更好？
