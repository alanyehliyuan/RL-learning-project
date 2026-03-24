# Hints — Exercise 01

## Hint 1

在 epsilon-greedy 裡：
- 以 `epsilon` 的機率隨機選 action
- 否則選目前 `q_values` 最大的 action

## Hint 2

sample-average incremental update 公式：

`Q <- Q + (1 / N) * (R - Q)`

其中 `N` 是該 action 被選到的次數。
