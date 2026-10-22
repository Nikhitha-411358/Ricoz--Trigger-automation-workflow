import requests

BASE = "http://127.0.0.1:8000"

workflow = requests.post(f"{BASE}/workflows", json={
    "name": "High Value Order Workflow",
    "action_type": "notification",
    "action_config": {
        "recipient": "sales-team",
        "message": "High value order detected."
    }
})
print("Workflow:", workflow.json())

workflow_id = workflow.json()["id"]

trigger = requests.post(f"{BASE}/triggers", json={
    "name": "High Value Order Trigger",
    "event_type": "ORDER_CREATED",
    "condition_field": "amount",
    "operator": ">",
    "condition_value": 50000,
    "workflow_id": workflow_id,
    "enabled": True
})
print("Trigger:", trigger.json())
