# API 契约

线上契约以 [Apifox](https://hr124ptabw.apifox.cn/) 为准。

| 接口 | 方法 | 用途 |
| --- | --- | --- |
| `/api/search` | POST | 搜题并返回 `original`、`similar` 或 `miss` 三态 |
| `/api/chat` | POST | 直接解析或引导式答疑 |
| `/api/upload` | POST | 提取 PDF/图片文本并返回处理摘要 |

接口字段名和响应结构不得由个人私自修改。契约变更需先报备 TL，再同步更新 Apifox 和本文件。
## Stage2 修订文档（待确认）

- [架构图、数据字典与 API 契约规范](stage2%20-%20%E6%9E%B6%E6%9E%84%E5%9B%BE%E3%80%81%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8%E3%80%81API%E5%A5%91%E7%BA%A6%E8%A7%84%E8%8C%83.md)
- [接口联调与开发交接](stage2%20-%20%E6%8E%A5%E5%8F%A3%E8%81%94%E8%B0%83%E4%B8%8E%E5%BC%80%E5%8F%91%E4%BA%A4%E6%8E%A5.md)

以上为「接口更改建议」PR 的修订稿。确认并同步 Apifox 后作为开发基准；本次不修改业务代码或线上 Mock。
