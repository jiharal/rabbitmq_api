

# server
```bash
(venv) ➜  rabbitmq_api python start_server.py online
API Started
publish status {'correlation_id': '7b7e8c26-4ede-456c-a381-91389395bbe4', 'success': True, 'message': 'success', 'data': {'status': 'ONLINE'}}
(venv) ➜  rabbitmq_api python start_server.py offline
API Started
publish status {'correlation_id': 'c45acb9f-102e-4008-9209-66056e0edbc9', 'success': True, 'message': 'success', 'data': {'status': 'OFFLINE'}}
(venv) ➜  rabbitmq_api python start_server.py none
API Started
publish status {'correlation_id': 'd088da13-6560-4c73-bfdf-cd9807db1a89', 'success': False, 'message': 'Server is down', 'data': {}}

```

# client
```bash
Received message: '{"correlation_id": "9a1a5ecc-4291-43bc-be33-18da3c0d48a9", "success": true, "message": "success", "data": {"status": "ONLINE"}}'
Received message: '{"correlation_id": "7b7e8c26-4ede-456c-a381-91389395bbe4", "success": true, "message": "success", "data": {"status": "ONLINE"}}'
Received message: '{"correlation_id": "c45acb9f-102e-4008-9209-66056e0edbc9", "success": true, "message": "success", "data": {"status": "OFFLINE"}}'
Received message: '{"correlation_id": "d088da13-6560-4c73-bfdf-cd9807db1a89", "success": false, "message": "Server is down", "data": {}}'
```