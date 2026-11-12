# Tobpage

一款暗黑西游风的 Hugo 主题：墨黑打底、鎏金主色、朱砂点缀，骨架借鉴 Butterfly × AnZhiYu 的双栏卡片流。由 [普客网](https://puke.eu.org/) 自研自用，与 WordPress 主题 TobPress 成对。

**演示站**：https://puke.eu.org/

## 截图

桌面端 Hero：

![桌面端 Hero](images/hero-desktop.jpg)

手机端首页：

![手机端首页](images/home-mobile.jpg)

开场动画收尾帧（大圣棍指南天门）：

![开场动画收尾帧](images/loader-arrive.jpg)

浅色模式文章页：

![浅色模式文章页](images/post-light.jpg)

## 特性

- **双栏卡片流**：文章卡片 + 粘性侧栏（作者卡、分类、标签云、最新文章），桌面与移动端各自适配
- **两段式孙悟空开场动画**：仅首页渲染、每次打开首页播放——v11「在飞」打头（加载中），加载完成交叠切 v12「棍指南天门」收尾，3 秒内必退场；减动效偏好下不播放
- **五大栏目两级分类 + 彩色图标**：文章 / 技术 / 软件 / 资讯 / 日常，各含二级分类，内置彩色图标与分组分类页
- **深浅双色**：一键切换并持久化，浅色为深灰纸面
- **中文字数与阅读时长**：按中文字符正确计数，卡片与文章页显示「N 字 · 约 M 分钟」
- **本地搜索**：JSON 索引按需加载，无外部服务依赖
- **文章目录 + 阅读进度**：侧栏 TOC 锚点导航，顶部金→赤渐变进度条
- **归档时间线**：按年月分组，中文月份
- **页脚信息区**：备案号、运行天数等均由站点参数配置（见下），主题本身不带任何站点默认值
- **系列文章导航**：文章 front matter 写 `series`（系列名）+ 可选 `series_order`（序号），同系列 ≥2 篇时文章页自动渲染系列框（全系列目录 + 「本系列第 X / N 篇」），零站点配置
- **相关文章**：文末按 Hugo Related Content 自动推荐（内置默认索引 keywords/tags/date），无相关结果时不渲染
- **代码块一键复制**：正文代码块悬停出现复制按钮（原生 JS，含剪贴板降级路径）
- **图片灯箱**：点击正文图片全屏查看，可前后翻看本篇全部图片（Esc/方向键/点背景关闭）；包着真外链的图片不拦截
- **排版 shortcode**：`notice`（注/提示/警告提示框）、`details`（折叠块）、`tabs`/`tab`（标签页），用法见下文，零配置

## 环境要求

- Hugo **扩展版（extended）**，已在 **0.169.0** 上验证构建（theme.toml 声明下限 0.120.0）

## 安装

```bash
git clone https://github.com/tobaye/Tobpage.git themes/tobpage
```

在站点 `hugo.toml` 里启用：

```toml
theme = "tobpage"
```

### 站点脚手架（必备，否则导航死链/搜索不可用）

主题的导航固定链向三个页面，且本地搜索依赖首页的 JSON 索引，新站需自备：

1. **三个内容页**（放站点 `content/` 下）：
   - `search.md`：front matter 写 `layout: "search"`
   - `archives.md`：front matter 写 `layout: "archives"`
   - `about.md`：普通页面即可
2. **首页输出 JSON**：站点 `hugo.toml` 里加 `[outputs]` 的 `home = ["HTML", "RSS", "JSON"]`（Hugo 不从主题继承 outputs，必须站点自配），搜索页才能拉到 `/index.json`。
3. **robots.txt**：站点配了 `[languages]` 时 Hugo 不自动生成 robots.txt，建议站点自备 `static/robots.txt`。
4. **分页**：Hugo ≥0.128 已移除顶层 `paginate` 键，分页大小用 `[pagination] pagerSize = 10`。

## 关键参数

主旨语、建站日期、备案号、Hero 图等全部是**站点参数**，主题内没有任何普客网的默认值——不配就不渲染：

```toml
[params]
  heroImage = "/img/hero-wukong.jpg"   # Hero 背景图（可替换为任意图）
  ogImage = ""                          # 分享预览图（og:image / twitter:image）默认值，可空（见下）

[params.assets]
  favicon = ""                          # 站点图标路径，可空（见下）

[params.tobpage]
  heroMotto = "普天之下，皆为客。"       # Hero 与开场动画的主旨语
  startDate = "2026-10-29"             # 页脚「本站已运行 X 天」的起算日
  moeIcp = "萌ICP备20269123号"          # 页脚备案号
  moeIcpURL = "https://icp.gov.moe/?keyword=20269123"  # 备案链接
```

分享预览图（`og:image` / `twitter:image`）：文章页优先用该文的 `cover.image`；没有时依次回退站点参数 `ogImage`、`heroImage`，再没有就用主题自带的 `img/hero-wukong.jpg`，输出恒为绝对地址。想全站统一一张分享图，配 `ogImage` 即可。

站点图标（favicon）：配了 `params.assets.favicon` 就用站点自己的文件；不配则自动用主题自带的 `static/favicon.svg`（墨黑底、鎏金云纹、朱砂点），不会 404。想换图，把自己的 `favicon.svg` 放进站点 `static/` 同名覆盖即可。

栏目体系（分类名→栏目/图标/配色）在主题的 `layouts/partials/category-meta.html` 一处定义，换栏目改这一处即可；大圣视觉素材在 `static/img/`，替换同名文件即可换图。文章用到了未登记进该表的分类也不会让构建失败——它们会在分类索引页单列为「其他」组。

## 文章增强（零配置，写上就生效）

### 系列文章

组诗、连载等多篇成组时，在每篇 front matter 写同名 `series`，序号用可选的 `series_order`（不写序号的篇目按日期排在已编号之后）：

```yaml
series: "清平调词三首"
series_order: 1
```

同系列 ≥2 篇时，每篇文首自动出现系列框：系列名、全系列有序目录（当前篇标注「本篇」）与「本系列第 X / N 篇」。

### 相关文章

文末自动渲染，用 Hugo 内置默认索引（keywords 权重 100、tags 80、date 10，阈值 80），无结果不渲染。想调整（如让最新一篇文章也能出相关推荐）可在站点 `hugo.toml` 覆盖：

```toml
[related]
  includeNewer = true
```

### 排版 shortcode

提示框（类型 `note` 注 / `tip` 提示 / `warn` 警告，也可 `type="warn"` 命名参）：

```markdown
{{< notice warn >}}这里是警告内容，**支持 Markdown**。{{< /notice >}}
```

折叠块（原生 `<details>`，无 JS 可开合；`open=true` 默认展开）：

```markdown
{{< details "点开看细节" >}}折叠起来的内容……{{< /details >}}
```

标签页（JS 接管为选项卡；无 JS 时面板平铺、内容不丢）：

```markdown
{{< tabs >}}
{{< tab "其一" >}}第一首的内容。{{< /tab >}}
{{< tab "其二" >}}第二首的内容。{{< /tab >}}
{{< /tabs >}}
```

## 字体出处

站名整图 `static/img/hero-title.webp`（站点以 `params.tobpage.titleImage` 启用）由两款字体离线合成：大字为马善政毛笔体（Ma Shan Zheng，Google Fonts，SIL Open Font License 1.1）；印章篆字字形源为全字庫說文解字，數位發展部，CNS11643中文標準交換碼全字庫網站，https://www.cns11643.gov.tw ，依《政府資料開放授權條款－第 1 版》使用。合成脚本存于主题仓 `assets-src/`。页面文字全部使用系统字体，无外部字体请求。

## 许可

MIT，见 [LICENSE](LICENSE)。
