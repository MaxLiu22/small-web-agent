"""
最小可运行的 browser-use Demo：
- 使用与你当前 .env 相同的 Kimi/OpenAI 兼容配置
- 启动一个浏览器 Agent，访问一个简单页面

这一步的目标只是：确认 browser-use + 你的 LLM 配置 能正常工作。
"""

import os

from dotenv import load_dotenv
from browser_use import Agent, Browser
from langchain_openai import ChatOpenAI


def build_llm() -> ChatOpenAI:
    """复用你在 agent_test.py 中类似的 Kimi 配置。"""
    load_dotenv()

    api_key = os.getenv("KIMI_API_KEY")
    base_url = os.getenv("KIMI_BASE_URL")
    model = os.getenv("KIMI_MODEL", "moonshot-v1-8k")

    if not api_key or not base_url:
        raise RuntimeError(
            "缺少 Kimi 配置：请在项目根目录创建 `.env` 文件，并设置 "
            "KIMI_API_KEY 和 KIMI_BASE_URL。"
        )

    return ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model=model,
        temperature=0.2,
    )


def main() -> None:
    print("==== browser-use 最小 Demo ====")

    llm = build_llm()
    browser = Browser()  # 使用默认浏览器配置（底层仍是 Playwright）

    task = "打开 https://www.baidu.com，然后结束。不要做其他多余操作。"

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
    )

    print("📥 [任务] ", task)
    result = agent.run()

    print("✅ Agent 运行结束。返回结果概要：")
    print(result)


if __name__ == "__main__":
    main()

