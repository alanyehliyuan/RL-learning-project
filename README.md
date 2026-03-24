# RL Learning Project

A course-structured repository for learning reinforcement learning step by step.

## 這個 repo 的目標

這不是單純收集 RL 程式碼的地方，而是一套可逐步完成的學習系統：

- 先建立直覺
- 再做紙上推導與小題目
- 再進到可執行的實作
- 最後做成小專案

## 使用方式

- `main`：教材主線、索引、題目、解答入口
- 練習時可另外開 branch，例如：`alan/ex01-bandit-attempt`
- 我之後若提供示範解答或延伸實驗，也可以用獨立 branch 或直接整理進 `solutions/`、`projects/`

## 課程地圖

### Phase 0 — Foundations
- prerequisites：機率、微積分、線代、Python、基本 machine learning 背景
- RL 在解什麼問題
- supervised / unsupervised / reinforcement learning 的差異
- agent / environment / reward / policy / value 的基本概念

### Phase 1 — Bandits and Intuition
- multi-armed bandit
- exploration vs exploitation
- epsilon-greedy
- optimistic initialization
- UCB
- Thompson sampling（選修）

### Phase 2 — MDP and Dynamic Programming
- Markov decision process
- Bellman equation
- policy evaluation
- policy improvement
- policy iteration
- value iteration

### Phase 3 — Tabular RL
- Monte Carlo methods
- Temporal-Difference learning
- SARSA
- Q-learning
- on-policy vs off-policy

### Phase 4 — Function Approximation and Deep RL
- value function approximation
- policy gradient
- DQN
- actor-critic / PPO（入門層級）

### Phase 5 — Mini Projects
- CartPole
- MountainCar
- 一些偏應用型的小題目

## Repo 結構

```text
RL-learning-project/
├── README.md
├── syllabus/
│   ├── roadmap.md
│   ├── how-to-study.md
│   └── prerequisites.md
├── modules/
│   ├── 00-foundations/
│   ├── 01-bandits/
│   ├── 02-mdp-dp/
│   ├── 03-tabular-td/
│   ├── 04-q-learning-sarsa/
│   ├── 05-function-approx/
│   ├── 06-policy-gradient/
│   └── 07-deep-rl/
├── exercises/
├── solutions/
├── projects/
├── notes/
└── notion/
```

## 建議學習流程

每個單元都盡量走這四步：

1. 先讀概念與背景
2. 做小題目或紙上推導
3. 實作最小可跑版本
4. 回頭寫下自己的理解與反思

## 第一個起手單元

我們先從 `01-bandits` 開始，原因是：

- 概念小
- 很適合建立 RL 直覺
- 可以很快看到 exploration / exploitation 的核心衝突
- 之後很多 RL 方法都能從這裡長出來

## Notion 的角色

Notion 不作為唯一知識本體，而是作為：

- 學習進度看板
- 個人筆記與心得整理
- 問題追蹤
- 模組完成狀態管理

核心教材、題目、解答、程式碼仍然放在 repo 內，用 git 管理。
