# agent/mcp_server.py (mini)
# Ejecuta un MCP server que expone 'retrieve_guideline' y 'extract_and_score'
# para que cualquier cliente compatible (p.ej. IDE) pueda orquestar el flujo.
from agent.mcp_server import Server, Tool
from agent.tools import tool_retrieve_guideline, tool_extract_and_score

srv = Server("health-rag")
srv.add_tool(Tool("retrieve_guideline", tool_retrieve_guideline, {"q":"string"}))
srv.add_tool(Tool("extract_and_score", tool_extract_and_score, {"html":"string","overrides":"object"}))
if __name__=="__main__":
    srv.run_stdio()
