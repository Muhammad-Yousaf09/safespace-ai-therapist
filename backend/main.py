# step 1:Set up FastAPI backend
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from ai_agent import graph, SYSTEM_PROMPT
from ai_agent import parse_response

app = FastAPI()


class Query(BaseModel):
    message: str


# step 2: Recieve and validate request from Frontend
@app.post("/ask")
async def ask(query: Query):
    # setting AI Agent
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)
    
    # step 3:send response to the front end
    return {"response": final_response, "tool_called": tool_called_name}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
# main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
