from agents.planner import plan_task
from agents.executor import execute_task
from agents.reviewer import review_result
from memory import add_memory

def run_workflow(user_input):
    plan = plan_task(user_input)
    execution = execute_task(plan)
    final = review_result(execution)

    add_memory({
        "input": user_input,
        "plan": plan,
        "result": final
    })

    return {
        "plan": plan,
        "execution": execution,
        "final": final
    }
