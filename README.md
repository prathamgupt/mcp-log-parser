# 🧠 MCP Log Parser & Categorizer

This repository provides two lightweight MCP (Materialized Cursor Protocol) servers designed to **parse server logs** and **categorize them intelligently**. Ideal for use with [Cursor](https://cursor.so) or any agent framework that supports MCP.

---

## 📌 Features

- ✅ Parses raw logs into structured JSON format
- 🧠 Categorizes logs based on level, status code, and message context:
  - `Normal`
  - `Server Crash or Upstream Error`
  - `Unauthorized Access`
  - `Resource Not Found`
  - `Client Error`
- 🔌 Supports stateless HTTP for easy integration
- ⚡ Optimized for use in Cursor or other local agent environments

---

## 🚀 Sample Flow

### 🔹 Input Logs
```
2025-06-30 14:23:45 [INFO] 200 /api/login User successfully logged in.
2025-06-30 14:25:12 [ERROR] 500 /api/data Internal server error occurred.
2025-06-30 14:26:03 [DEBUG] 200 /api/fetch/cache Fetched data from cache.
2025-06-30 14:28:47 [WARN] 403 /api/update Permission denied for update.
2025-06-30 14:30:01 [INFO] 201 /api/register New user registered.
2025-06-30 14:32:18 [ERROR] 404 /api/item/42 Item not found.
2025-06-30 14:34:10 [DEBUG] 200 /api/status Status check passed.
2025-06-30 14:36:25 [INFO] 200 /api/logout User logged out.
2025-06-30 14:38:09 [WARN] 429 /api/requests Too many requests.
2025-06-30 14:40:55 [ERROR] 500 /api/payment Payment processing failed.
```

### 🔹 Parsed Output (via `parser` MCP Server)
```json
{
  "timestamp": "2025-06-30T14:23:45",
  "level": "INFO",
  "status": 200,
  "url": "/api/login",
  "message": "User successfully logged in."
}
```

### 🔹 Categorized Output (via catagorize MCP Server)
```json
{
  "timestamp": "2025-06-30T14:25:12",
  "level": "ERROR",
  "status": 500,
  "url": "/api/data",
  "message": "Internal server error occurred.",
  "category": "Server Crash or Upstream Error"
}
```

---

## 🧩 MCP Server Configuration (for use in Cursor or agents)
Add the following to your `.cursor/config.json` or pass to your agent system:

```json
{
  "mcpServers": {
    "catagorize": {
      "url": "https://mcp-log-parser.onrender.com/catagorize/mcp/"
    },
    "parser": {
      "url": "https://mcp-log-parser.onrender.com/parser/mcp/"
    }
  }
}
```

---

## 🛠️ Usage in Cursor
Once configured, you can highlight a set of raw logs and ask Cursor:

> Parse these logs

Then you can follow up with:

> Categorize these parsed logs