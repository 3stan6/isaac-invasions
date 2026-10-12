import sys
import json
import urllib.request
import urllib.error

import os

TOKEN = os.environ.get("MELTY_TOKEN")
if not TOKEN:
    token_path = r"C:\Users\3STAN\.gemini\antigravity\scratch\melty_token.txt"
    if os.path.exists(token_path):
        with open(token_path, "r", encoding="utf-8") as f:
            TOKEN = f.read().strip()
URL = "https://melty.gg/api/mcp"

def call_tool(name, arguments=None):
    if arguments is None:
        arguments = {}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": name,
            "arguments": arguments
        }
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode('utf-8')
            # Check if event stream or plain json
            if body.startswith("data: "):
                # SSE format
                lines = body.splitlines()
                json_lines = [l[6:] for l in lines if l.startswith("data: ")]
                return json.loads(json_lines[-1]) if json_lines else body
            return json.loads(body)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='replace')
        return {"http_error": e.code, "body": err_body}
    except Exception as e:
        return {"error": str(e)}

def list_tools():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list",
        "params": {}
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode('utf-8')
            return json.loads(body)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='replace')
        return {"http_error": e.code, "body": err_body}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "tools":
        print(json.dumps(list_tools(), indent=2))
    elif len(sys.argv) > 1:
        tool_name = sys.argv[1]
        arg_str = sys.argv[2] if len(sys.argv) > 2 else "{}"
        if arg_str.startswith("@"):
            with open(arg_str[1:], "r", encoding="utf-8") as f:
                args = json.load(f)
        elif arg_str == "-":
            args = json.load(sys.stdin)
        else:
            try:
                args = json.loads(arg_str)
            except Exception:
                import ast
                args = ast.literal_eval(arg_str)
        print(json.dumps(call_tool(tool_name, args), indent=2))
    else:
        print("Usage: melty_cli.py [tools | <tool_name> <json_args>]")
