"""MCP server for Environment Variable & Secret Drift Config Validator."""
import sys
import json
from client import EnvConfigDriftValidator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "validate_env_config_drift",
                "description": "Validates runtime environment variables against required template keys",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "template_keys": {"type": "array"},
                        "runtime_env": {"type": "object"}
                    },
                    "required": ["template_keys", "runtime_env"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "validate_env_config_drift":
            args = params.get("arguments", {})
            res = EnvConfigDriftValidator.validate_env_config(
                args.get("template_keys", []),
                args.get("runtime_env", {})
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
