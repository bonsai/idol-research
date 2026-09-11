# idol-db Research Seed

`idol-db` の正本データを、`idol-research` が問いを発見するための **Research Seed** として利用する。

## 1. Source of Truth

`idol-db` はデータそのものを管理する正本であり、research 側にデータを複製して正本を増やさない。

| Source | 観測できる構造 |
|---|---|
| SPARK | イベント／出演者構造 |
| IDOL Watch | 継続的な観測／時系列 |
| agency | 所属／組織構造 |
| 惑星通信社 | メディア／活動主体／関係構造 |

4系統は「過去データの保管場所」ではなく、**何を観測し、何を問えるかを発見するための観測基盤**として扱う。

## 2. Research Seed

4系統を横断すると、単一データセットでは見えない関係・変化・欠損・偏りを発見できる。

```text
SPARK ─────┐
IDOL Watch ├─→ Research Seed → RQ → Hypothesis → Analysis
agency ────┤
惑星通信社 ┘
```

Research Seed は、分析結果そのものではなく、**次に調べるべき問いを発見する入力**である。

## 3. Research Boundary

```text
idol-db
  canonical data / provenance
          ↓
     research seed
          ↓
idol-research
  ├─ observation
  ├─ research question
  ├─ hypothesis
  ├─ analysis
  └─ marketing
          ↓
     evaluation / insight
          ↓
      idol-lab
  verified generalizable theory
```

- `idol-db` — canonical data / provenance
- `idol-research` — observation / RQ / hypothesis / analysis / marketing / evaluation
- `idol-lab` — 検証済みで一般化可能な理論・概念

## 4. Research Loop

```text
Observation
  ↓
Research Seed
  ↓
Research Question
  ↓
Hypothesis
  ↓
Data
  ↓
Analysis
  ↓
Evaluation
  ↓
Insight
  ↓
Next Hypothesis
  ↺
```

重要なのは、**データを移したことを研究完了とみなさない**こと。

> データを移した＝研究を終えた、ではない。  
> データを正本として接続したことで、研究可能になった。

## 5. Seed から発見する問い

### SPARK
- 誰が、どのイベントに、どの頻度で出演しているか
- 出演者同士にどのような共演ネットワークがあるか

### IDOL Watch
- 活動頻度は時間とともにどう変化するか
- 活動の開始・停止・転換はいつ起きるか

### agency
- 所属構造と活動形態にはどのような関係があるか
- 個人／グループ／事務所の関係はどう変化するか

### 惑星通信社
- メディア掲載と活動主体の関係はどうなっているか
- どの活動がどのメディア接点につながるか

### Cross Dataset
- 出演 × 時系列 × 所属 × メディアを重ねると何が見えるか
- 4系統で一致する活動パターンはあるか
- 逆に、一方のデータにしか現れない活動は何か
- データ間の欠損・偏りそのものは何を示しているか

## 6. Principle

Research は「データを読む作業」ではなく、**観測可能なデータから次の問いを生成するプロセス**とする。

```text
Canonical Data
    ↓
Cross-Dataset Observation
    ↓
Anomaly / Pattern / Gap
    ↓
Research Question
    ↓
Hypothesis
    ↓
Evidence
    ↓
Evaluation
    ↓
Generalization?
    ├─ No → research に蓄積
    └─ Yes → idol-lab に理論として返す
```

この seed は `idol-research` の研究開始点であり、単なるデータ移管記録ではない。
