# 🧩 可观测的多模态 Hello-World Web Agent：LLM + VLM + 实时画面

一个简单的 Web Agent 演示项目，通过简单的配置即可实现：

1. **逻辑推理**：使用 **Kimi (LLM)** 推理任务步骤
2. **视觉识别**：使用 **Qwen-VL (VLM)** 识别网页内容
3. **实时观测**：通过 **Playwright** 与 **noVNC** 在前端实时显示浏览器操作

这是一个 Hello World 级别的脚手架项目，适合快速上手和二次开发。

## 🏗️ 技术架构
* **大脑 (Reasoning):** Kimi API (OpenAI 兼容协议)
* **眼睛 (Vision):** Qwen-VL (VLM，OpenAI 兼容接口)
* **执行器 (Driver):** Python + Playwright
* **实时画面 (Streaming):** Docker + Xvfb + x11vnc + noVNC
* **交互界面 (UI):** FastAPI + React / Simple HTML (双 Iframe 架构)

---

## 🛠️ 开始之前
在开始之前，请确保你已准备好：
1. **Python 3.10+**
2. **Docker Desktop**
3. **Kimi API Key**（BASE_URL 请指向 Kimi 官方或中转地址）
4. **Qwen-VL API Key**（视觉增强模式需配置 VL_BASE_URL / VL_API_KEY，详见项目配置）

## 🚀 启动步骤

### 1. 配置环境变量

在项目根目录创建 `.env` 文件，配置必要的 API 密钥：

```bash
# Kimi API 配置（必需）
KIMI_API_KEY=your_kimi_api_key_here
KIMI_BASE_URL=https://api.moonshot.cn/v1  # 或你的中转地址

# Qwen-VL API 配置（可选，用于视觉增强模式）
VL_MODEL=qwen-vl-max-latest
VL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1  # Qwen-VL 的 OpenAI 兼容接口地址
VL_API_KEY=your_qwen_vl_api_key_here
```

> **提示**：如果暂时没有 Qwen-VL API Key，可以只配置 Kimi 相关变量，项目会以纯文本 + DOM 模式运行。

### 2. 启动 Docker 容器

在项目根目录执行：

```bash
docker-compose up --build
```

首次运行会构建 Docker 镜像（包含 Playwright、Xvfb、noVNC 等），可能需要几分钟时间。

### 3. 访问 Web 界面

容器启动成功后，打开浏览器访问：

- **主界面**：http://localhost:8000/
  - 左侧：任务输入与"启动 Agent"按钮
  - 右侧：实时显示 Agent 在浏览器中的操作画面（通过 noVNC）

- **noVNC 独立界面**（可选）：http://localhost:6080/vnc_lite.html

### 4. 运行 Agent

1. 在左侧面板点击 **"🚀 启动 Agent"** 按钮
2. 右侧屏幕会自动显示浏览器打开并执行任务（例如：在百度搜索"深圳未来14天天气"）
3. 任务完成后，左侧日志区域会显示执行结果

### 5. 停止服务

按 `Ctrl + C` 停止容器，或使用：

```bash
docker-compose down
```

---

## 💡 快速体验

完成上述配置后，你可以：

1. 在项目根目录执行：`docker-compose up --build`
2. 打开浏览器访问：`http://localhost:8000/`
3. 点击左侧的"🚀 启动 Agent"按钮，右侧屏幕会实时显示浏览器自动打开并执行任务（例如：在百度搜索"深圳未来14天天气"）

---

## 📄 开发日志与路线图
详细的 3-Day Sprint 冲刺记录、Day4 视觉增强设计以及未来路线图，请查看：

- **`LOGS.md`** - 开发进度与规划文档
