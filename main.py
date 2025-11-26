from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def hello(name: str, message: str):
    return f"""
    <html>
      <head>
        <title>Hello page</title>
        <style>
          body {{
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e5e7eb;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
          }}
          .card {{
            background: #020617;
            padding: 32px 40px;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            text-align: center;
          }}
          .title {{
            font-size: 32px;
            margin-bottom: 12px;
          }}
          .subtitle {{
            font-size: 20px;
            color: #38bdf8;
          }}
        </style>
      </head>
      <body>
        <div class="card">
          <div class="title">Hello, {name}!</div>
          <div class="subtitle">{message}</div>
        </div>
      </body>
    </html>
    """
