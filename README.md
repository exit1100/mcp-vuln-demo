# MCP Weather Tool (mcp-vuln-demo)

LLM과 Claude MCP 연동을 위한 간단한 날씨 도구 예제입니다.  
임의의 도시명을 입력하면 온도, 습도, 바람 방향, 상태 등의 정보를 랜덤하게 응답합니다.



## 🛠 설치 및 실행 방법

### 1. `uv` 설치 (Windows CMD 환경 기준)

```bash
powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
powershell -Command "Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression"
```

### 2. 저장소 클론 및 환경 설정
```bash
git clone https://github.com/exit1100/mcp-vuln-demo.git
cd mcp-vuln-demo

uv venv
.venv\Scripts\activate.bat
uv add "mcp[cli]"
```


## 🧠 Claude Desktop 연동 설정
Claude Desktop 앱의 config.json에 다음 항목을 추가하세요:
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "[Repository Path]",
        "run",
        "main.py"
      ]
    }
  }
}
```
--directory 경로는 본인의 저장소 위치에 맞게 수정하세요.
