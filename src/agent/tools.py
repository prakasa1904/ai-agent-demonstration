tools = [
    {
        "type": "function",
        "name": "get_cpu_usage",
        "description": "Get current CPU usage percentage",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "type": "function",
        "name": "get_memory_usage",
        "description": "Get current Memory usage percentage",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "type": "function",
        "name": "find_user_by_email",
        "description": "Find a user by their email address",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address of the user to find",
                },
            },
            "required": ["email"],
        },
    },
]
