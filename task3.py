def analyze_methods(data):
    result = {}
    for i in data:
        method= i["method"]
        error= i["error"]
        time= i["time_ms"]
        iteration= i["iterations_count"]

        if method not in result:
            result[method] = {"max_error": error,
                              "total_time_ms": time,
                              "iterations_count": iteration}
        else:
            result[method]["max_error"]= max(error, result[method]["max_error"])
            result[method]["total_time_ms"]+=time
            result[method]["iterations_count"]+=iteration
    return result



experiments_data = [
{"method": "Euler", "iteration": 1, "error": 0.15,
"time_ms": 1.2},
{"method": "Runge-Kutta", "iteration": 1, "error": 0.01,
"time_ms": 3.5},
{"method": "Euler", "iteration": 2, "error": 0.18,
"time_ms": 1.3},
{"method": "Runge-Kutta", "iteration": 2, "error": 0.008,
"time_ms": 3.6},
{"method": "Euler", "iteration": 3, "error": 0.22,
"time_ms": 1.2},
{"method": "Newton", "iteration": 1, "error": 0.05,
"time_ms": 2.1}
]

