"""Brain router — dispatches intent to the appropriate EU agent."""

import importlib
from ailawfirm_eu.brain.intents import Intent, AGENT_FOR_INTENT


def route(intent: Intent, payload: str) -> dict:
    agent_module_name = AGENT_FOR_INTENT.get(intent, "matter_agent")
    full_module = f"ailawfirm_eu.agents.{agent_module_name}"
    try:
        mod = importlib.import_module(full_module)
        handler = getattr(mod, "handle", None)
        if handler is None:
            return {
                "ok": False,
                "intent": intent.value,
                "agent": agent_module_name,
                "error": f"agent module {full_module} has no handle()",
            }
        result = handler(payload)
        return {
            "ok": True,
            "intent": intent.value,
            "agent": agent_module_name,
            "result": result,
        }
    except ImportError as e:
        return {
            "ok": False,
            "intent": intent.value,
            "agent": agent_module_name,
            "error": f"agent module import failed: {e}",
        }


def think(text: str) -> dict:
    from ailawfirm_eu.brain.classifier import classify

    intent = classify(text)
    return route(intent, text)
