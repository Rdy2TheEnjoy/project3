def log(filename = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = func.__name__ + " ok"
            except Exception as e:
                log_message = func.__name__ + " error: " + str(e) + ". Inputs: " + str(args) + ", " + str(kwargs)
                result = None
            else:
                print(log_message)
            finally:
                if filename:
                    with open(filename, "a") as f:
                      f.write(log_message + "\n")


            return result
        return wrapper
    return decorator

