from sqlalchemy import create_engine
import functools
from retry import retry
import time

#Context Manager
class postGress():
    def __init__(self,connection):
        self.connection=connection
    def __enter__(self):
        self.engine = create_engine(self.connection)
        self.connection=self.engine.raw_connection()
        self.cursor=self.connection.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
            print('Rollback Complete')
        else:
            self.connection.commit()
            print('Commit Successfull')
        self.cursor.close()
        self.connection.close()
        print('Connection Closed')
        return True

# Retry Decorator
def retry_and_log(retry_attempts):
    # type: (int, Callable[..., Any]) -> Callable[..., Any]
    """
    A function wrapper for catching all exceptions and logging them, with retry attempts
    """
    def wrapper(f):
        # type: (Callable[..., Any]) -> Callable[..., Any]
        @functools.wraps(f)
        def inner(*args, **kwargs):
            mdelay=backoff=2
            # type: (*Any, **Any) -> Any
            for i in range(retry_attempts):                
                try:                                     
                    return f(*args, **kwargs)
                except Exception as ex:
                    print(f'Retrying in {i+1} Seconds....')   
                    print(ex)
                    time.sleep(i+1)
        return inner

    return wrapper


# DB Decorator

def db_connection(func):
    @retry_and_log(retry_attempts=3)    
    @functools.wraps(func) # To preserve the identity of orignal function
    def wrapper(*args,**kwargs):
        with postGress('postgresql://vista:vista@157.245.103.106:5432/vista') as database_cursor:
        # connection= f'postgresql://vista:vista@157.245.103.106:5432/vista'
        # engine = create_engine(connection)
        # database_connection = engine.raw_connection()
        # #database_connection = connect('akshay/akshay@157.245.103.106/ORCLCDB.localdomain')
        # database_cursor = database_connection.cursor()
        

            return func(database_cursor,*args,**kwargs)
    return wrapper


@db_connection
@retry_and_log(retry_attempts=4)
def func(db_cursor):
    query="SELECT PARAM_VALUE FROM SLA_CONFIG_PARAM WHERE PARAM_TYPE='ACCOUNT' AND PARAM_NAME='EXTENSION'"
    # db_cursor.execute(query)
    db_cursor.execute(query)
    p=db_cursor.fetchall()
    # raise Exception('Errooor')
    print(p)

func()

# print(help(func))
# print(func.__name__)


# Decorator with arguments--syntax of calling @db_connection(2)

# def db_connection(nums):
#     def decorator(func):
#         @functools.wraps(func) # To preserve the identity of orignal function
#         def wrapper(*args,**kwargs):
#             connection= f'postgresql://vista:vista@157.245.103.106:5432/vista'
#             engine = create_engine(connection)
#             database_connection = engine.raw_connection()
#             #database_connection = connect('akshay/akshay@157.245.103.106/ORCLCDB.localdomain')
#             database_cursor = database_connection.cursor()
            

#             return func(database_connection,database_cursor,*args,**kwargs)
#         return wrapper
#     return decorator



    
    