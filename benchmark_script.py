import os
import time

gosec_template = "gosec {}"
semgrep_template = "semgrep --config 'p/golang' -f {} --json"

# Path: benchmark_script.py
def benchmark_script_with_output(script_path):
    """
    Runs the benchmark script and returns the result.
    """
    # Path: benchmark_script.py
    start_time = time.time()
    output = os.popen(script_path).read()
    end_time = time.time()
    return end_time - start_time, output


def store(path, data):
    with open(path, "w") as f:
        f.write(data)


if __name__ == "__main__":
    # Path: benchmark_script.py
    # get all web frameworks paths using os.listdir
    # and run the benchmark script for each of them
    # and print the result
    # Path: benchmark_script.py

    frameworks_path = os.listdir(os.path.join(os.getcwd(), "frameworks"))
    for framework in frameworks_path:
        script_path = os.path.join("frameworks", framework)
        print(f"Benchmarking {framework}")
        print(script_path)

        # Benchmarking framework on gosec

        time_taken, output = benchmark_script_with_output(
            gosec_template.format(script_path)
        )
        print(f"Gosec took {time_taken} seconds on {framework}")
        store(f"gosec_results/{framework}.text", output)

        # Benchmarking framework on semgrep
        time_taken, output = benchmark_script_with_output(
            semgrep_template.format(script_path)
        )
        print(f"Semgrep took {time_taken} seconds on {framework}")
        store(f"semgrep_results/{framework}.text", output)