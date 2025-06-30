from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Catagorize", stateless_http=True)

def determine_category(log):
    msg = log["message"].lower()
    status = log["status"]

    if "econnrefused" in msg:
        return "Database Down"
    elif "timeout" in msg:
        return "Network Delay"
    elif status >= 500:
        return "Server Crash or Upstream Error"
    elif status == 403:
        return "Unauthorized Access"
    elif status == 401:
        return "Authentication Failure"
    elif status == 404:
        return "Resource Not Found"
    elif status >= 400:
        return "Client Error"
    else:
        return "Normal"

@mcp.tool(description="Categorizes a list of parsed logs based on status and message")
def catagorize(logs: list[dict]) -> list[dict]:
    for log in logs:
        log["category"] = determine_category(log)
    return logs
