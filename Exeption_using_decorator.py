import functools
from retry import retry
from functools import wraps,lru_cache
import time
from sqlalchemy import create_engine



def db_connection(func):
    @functools.wraps(func) # To preserve the identity of orignal function
    def wrapper(*args,**kwargs):
        connection= f'postgresql://vista:vista@157.245.103.106:5432/vista'
        engine = create_engine(connection)
        database_connection = engine.raw_connection()
        #database_connection = connect('akshay/akshay@157.245.103.106/ORCLCDB.localdomain')
        database_cursor = database_connection.cursor()
        # raise Exception('Error')
        return func(database_connection,database_cursor,*args,**kwargs)
    return wrapper


def retry_and_log(retry_attempts):
    # type: (int, Callable[..., Any]) -> Callable[..., Any]
    """
    A function wrapper for catching all exceptions and logging them, with retry attempts
    """
    def wrapper(f):
        # type: (Callable[..., Any]) -> Callable[..., Any]
        @functools.wraps(f)
        def inner(*args, **kwargs):
            # type: (*Any, **Any) -> Any
            for i in range(retry_attempts):
                
                try:
                                     
                    return f(*args, **kwargs)
                except Exception as ex:
                    print('Retrying....')   
                    print(ex)
                    time.sleep(i+1)
        return inner

    return wrapper
  
@retry_and_log(retry_attempts=2)
@db_connection
def my_method(db_conn,db_cursor):
    print(db_conn,db_cursor)
    print('Hello')
    # raise Exception("hello world")

my_method()