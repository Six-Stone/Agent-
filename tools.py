def fake_search(query):
    return f"[模拟搜索结果] 关于 '{query}' 的信息"

TOOLS = {
    "search": fake_search
}
