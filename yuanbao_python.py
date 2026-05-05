class NewAgent(BaseAgent):
    def __init__(self, agent_id: str, message_bus: MessageBus):
        capabilities = ["new_capability1", "new_capability2"]
        super().__init__(agent_id, "新Agent名称", "描述", message_bus, capabilities)
    
    async def execute_task(self, task: Task) -> Any:
        # 实现具体业务逻辑
        result = await self._do_work(task.metadata)
        return result