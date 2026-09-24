# Pashto Common Voice: Building the First Open Speech Corpus for a 60-Million-Speaker Low-Resource Language

- 论文编号：1432
- 报告人：Hanif Rahman
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rahman26_interspeech.pdf

## 问题
普什图语约 6–8 千万使用者，此前几乎无足够规模的开放许可语音语料；八个阿拉伯/波斯键盘缺失辅音常被替换或丢弃，转移学习易失败。

## 方法
2022–2025 在 Mozilla Common Voice 建语料：界面本地化、维基百科抽句过滤、针对 shin/zhe/dze/tse 等音位定向补句、Facebook 教程与无障碍叙事、VOA Pashto 广播动员；双评审验证。跨 CV14–CV23 十个版本。

## 实验与结果
规模：1.5h/5 人 → 147.07h/1483 人；CV17→CV18 说话人约增 108 倍（9→971）。MCV23：107781 clips，60337 已验证（82.33h），13 域；约 39% 仍未审。性别元数据缺失约 98%。Whisper Base 在 MCV20 全微调测试集 WER 13.4%（相对 Fleurs 零样本 99.0%）。

## 结论
开放普什图语料首次达到可全量微调规模；广播社区动员是可迁移的增长杠杆。后续需补审与性别覆盖。

## 点评
贡献是数据基础设施与社区增长动力学，而非新模型。强在可复现方法学与明确基线；弱在读语音 vs 自然语音差距、人口统计残缺，限制公平评测。
