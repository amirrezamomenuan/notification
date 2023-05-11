import os

workers_per_core = 1
threads_per_worker = 10

worker_class = "uvicorn.workers.UvicornWorker"

bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
reload = True if os.getenv("ENVIRONMENT") == "development" else False
