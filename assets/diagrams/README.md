# 图表 / Diagrams

手写 SVG，可直接在浏览器/GitHub 中打开，也可用文本编辑器改。不含外部字体与图片依赖，离线可读。

| 文件 | 内容 | 对应章节 |
|---|---|---|
| `layered-network.svg` | L0/L1/L2 三层职责、上下行、三条不变量 | 白皮书 §4 · `docs/protocol-draft/` |
| `problem-coupling.svg` | 六个问题的闭环与"同一调节器" | 白皮书 §3.7 · §6 · §7.6 |

## 约定

- 只用系统字体（`system-ui`），中英文混排时英文在前中文在后。
- 每个图底部标注"示意图，非规范"，避免被当成规范图。
- 修改图时同步检查对应章节文字，不要出现"图说的和文说的不一致"。

## 建议补的图（欢迎认领）

1. `validation-order.svg`：校验顺序与短路规则（`docs/protocol-draft/validation-flow.md`）。
2. `fee-split.svg`：手续费三路分流的恒等式。
3. `dormancy-conditions.svg`：沉睡实验分支的七项条件与"缺一不可"关系。
4. `fork-coexistence.svg`：重放保护如何避免双付歧义（Q7）。
