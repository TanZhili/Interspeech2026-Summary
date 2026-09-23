# Towards Chinese Yue Opera Singing Voice Synthesis: A Benchmark with Dataset, Data Augmentation and Baseline Model

- 论文编号：131
- 报告人：Peng Bai
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bai26_interspeech.pdf

## 问题
中国戏曲 SVS 资源稀缺，越剧（吴语）此前无专用数据集与基准；专业演员少、电子谱缺失、自动对齐难、源分离差，导致低资源困境。

## 方法
构建 YOAT：专业小生演员工作室干声约 1.35 h，切分为 565 句（均约 8.61 s），人工音素/时长+Parselmouth 音高对齐。增强：DA1 约 1 h 念白；DA2 字典拼接念白至 8 h；DA3 混入 4.5 h 歌仔戏对齐数据。基线 YueOpera-Singer：Transformer 编码器 + 乐谱时长扩展 + OT-CFM U-Net 解码，HiFi-GAN 声码。

## 实验与结果
543/22 训练测试划分。YueOpera-Singer-10：F0 RMSE 0.2133、MOS-N 3.92，优于 FFT-Singer、DiffSinger、FT-GAN，参数与显存更省。DA3 最有效（F0 RMSE 0.1834、MOS-N 4.01）；DA2 随规模提升发音 MOS；DA1 主要提发音、对 F0 帮助有限。

## 结论
给出越剧 SVS 首个数据集–增强–基线基准，MOS 约 3.92，为吴语戏曲合成提供可复现起点。

## 点评
贡献在文化低资源的数据与标注管线，而非架构创新；CFM 基线质量–效率均衡。单歌手、短时长限制泛化，跨剧种音高迁移（DA3）比同语念白更有效，提示“节奏–音高结构相似”比发音同域更关键。
