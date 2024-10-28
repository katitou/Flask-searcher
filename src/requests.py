def log_request(req: 'flask_request', res: str) -> None:
    with open('search.log', 'a') as file:
        print(req.remote_addr, req.user_agent, req.form, res, file=file, sep='|')