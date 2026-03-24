# Module 01 — Bandits

## Why this module matters

Multi-armed bandit 是學 RL 最好的起點之一。

它把問題濃縮成最核心的張力：

- 要不要繼續利用目前看起來最好的選項？
- 還是要花代價去探索可能更好的選項？

這就是 exploration vs exploitation。

## You should learn to answer

- 為什麼 bandit 問題不是 supervised learning？
- action-value estimate 是什麼？
- incremental update 為什麼有用？
- epsilon-greedy 的直覺是什麼？
- optimistic initialization 在做什麼？
- UCB 想補的是哪個盲點？

## Reading suggestions

### Primary
- Sutton & Barto, *Reinforcement Learning: An Introduction*, Chapter 2

### Optional supporting material
- David Silver RL course（bandit / intro 相關內容）
- 自己畫圖觀察平均 reward 與選臂次數變化

## Module contents

- `concepts.md`：觀念摘要
- `references.md`：學習資源
- `exercise-guide.md`：這個模組的練習題導引

## Exit criteria

完成這個 module 後，你應該能：

- 自己寫出一個 epsilon-greedy bandit agent
- 解釋 sample-average update 的由來
- 比較不同 exploration 策略的效果
