# 参考文献与阅读路线 / References

**规则**：只收录可独立核验的条目（有作者、年份、可查标题或出处）。不可核验的概称不收录。

## 建议阅读顺序

| 顺序 | 读什么 | 目的 | 用时 |
|---|---|---|---|
| 1 | Nakamoto (2008) | 确认本项目的出发点就是比特币，不是"改进版" | 1 小时 |
| 2 | Garay et al. (2015) | 理解"安全"在形式上意味着什么 | 3 小时 |
| 3 | Eyal & Sirer (2014) | 理解共识不是只有 51% 攻击一种死法 | 1 小时 |
| 4 | de Vries (2018) | 理解能耗讨论的量化基础 | 1 小时 |
| 5 | Bünz et al. (2018) | 理解"隐藏金额还能验证"的技术代价 | 3 小时 |
| 6 | De Filippi & Wright (2018) | 理解代码与法律的边界（对应白皮书 §12.5） | 4 小时 |

## 1. 共识与账本

1. **Nakamoto, S. (2008).** *Bitcoin: A Peer-to-Peer Electronic Cash System.* — 原始设计，本项目的对话对象。
2. **Merkle, R. C. (1979).** *A Certified Digital Signature.* CRYPTO '89. — 默克尔树来源。
3. **Garay, J., Kiayias, A., & Leonardos, N. (2015).** *The Bitcoin Backbone Protocol: Analysis and Applications.* EUROCRYPT 2015. — 形式化安全模型，Q6/Q8 的必读前置。
4. **Eyal, I., & Sirer, E. G. (2014).** *Majority is not Enough: Bitcoin Mining is Vulnerable.* Financial Cryptography 2014. — 自私挖矿，Q2 的反例来源。
5. **Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S. (2016).** *Bitcoin and Cryptocurrency Technologies.* Princeton University Press. — 教科书级入门。

## 2. 隐私与密码学

6. **Bünz, B., Bootle, J., Boneh, D., Poelstra, A., Wuille, P., & Maxwell, G. (2018).** *Bulletproofs: Short Proofs for Confidential Transactions and More.* IEEE S&P 2018. — 范围证明，对应白皮书 §8.2 的候选方案。
7. **Maxwell, G. (2013).** *CoinJoin: Bitcoin Privacy for the Real World.* — 交易混淆的起点，也是"混淆不等于隐私"的起点。
8. **BIP-340** *Schnorr Signatures for secp256k1*；**BIP-32** *Hierarchical Deterministic Wallets*；**BIP-141** *Segregated Witness*. — 一次性地址派生与签名方案的规范文本。

## 3. 能耗与激励

9. **de Vries, A. (2018).** *Bitcoin's Growing Energy Problem.* Joule, 2(5). — 能耗量化的通行参照；注意其估算方法与假设争议（这是 Q8 要处理的）。
10. 关于手续费市场与矿工收入结构的实证研究（如 Möser & Böhme 对交易费用的纵向研究）——引用前请核对原文，本仓库不代为背书具体结论。

## 4. 治理与法律

11. **De Filippi, P., & Wright, A. (2018).** *Blockchain and the Law.* Harvard University Press. — 白皮书 §12.5"代码不是法律"的直接依据。
12. **BIP-8 / BIP-9** 版本位激活机制。 — 向后兼容升级的现实样本，也是"扩展标志位为何必须逐个定义"的教训来源。
13. 中国大陆监管文件（公开可查，仅作事实陈述，非法律意见）：2017 年 9 月 4 日七部门《关于防范代币发行融资风险的公告》；2021 年 9 月十部门《关于进一步防范和处置虚拟货币交易炒作风险的通知》。

## 5. 待补方向（未收录，避免滥引）

- 控制理论在多参数闭环中的应用（Q6 需要正式方法，目前只在白皮书层面提出问题）。
- Proof-of-stake 与 PoW 安全预算的对比研究（对比章节需要更严肃的量化）。
- 货币流通速度与"稳态供应"的经济学文献（Q4 需要）。

**说明**：空缺不是遗漏，是明确的缺口。填这些位置需要先读原文，不能靠二手转述。

## 引用规范

- 引用时给出作者、年份、标题；有 DOI 或稳定链接时一并给出。
- 不得把"A 论文提到 B 观点"写成"B 观点由 A 证明"。
- 若某论断找不到来源，应在文中标为"未经验证的判断"，而不是编一个引用。
