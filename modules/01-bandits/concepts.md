# Concepts — Bandits

## Problem setup

在 multi-armed bandit 裡，你每次要從多個 action 中選一個，並拿到 reward。

重點是：
- 你不知道每個 action 的真實期望報酬
- 你只能透過互動慢慢估計

## Key idea 1: Action-value estimate

記 `Q(a)` 為某個 action 的價值估計。

最基本的做法是用 sample average：

`Q_n(a) = (前 n 次選到 a 的 reward 平均)`

## Key idea 2: Incremental update

不需要每次把全部歷史拿出來重算平均。

可以寫成：

`Q_{n+1} = Q_n + (1 / n) * (R_n - Q_n)`

這個形式非常重要，之後 RL 很多更新規則都長這個樣子。

## Key idea 3: Exploration vs Exploitation

- exploitation：選目前看起來最好的 action
- exploration：嘗試不確定但可能更好的 action

如果你永遠只 exploitation，可能太早陷入局部最佳。
如果你一直 exploration，學得很慢。

## Common strategies

### epsilon-greedy
大部分時間選當前最佳，少部分時間隨機探索。

### optimistic initialization
一開始把所有 action value 設得偏高，逼 agent 願意多試幾次。

### UCB
除了看目前估計值，也把不確定性一起納入考量。
