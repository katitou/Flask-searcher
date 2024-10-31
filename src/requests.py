from flask import Request
import mysql.connector

def log_request(req: Request, res: str) -> None:
    """Loggging web-request and returning results."""
    db_config = {
        'host': '127.0.0.1', 
        'user': 'admin', 
        'password': 'admin', 
        'database': 'searchlogDB', 
        'collation':'utf8mb4_general_ci'
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    _SQL = """
        insert into log 
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)
        """
    
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'], 
                          req.remote_addr,
                          str(req.user_agent),
                          res))
    
    conn.commit()
    cursor.close()
    conn.close()