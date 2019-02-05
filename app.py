from flask import Flask, render_template

app = Flask(__name__)


def count(num):
    if num <= 1:
        return num
    else:
        return count(num-1) + count(num-2)


@app.route("/fib/<int:start_idx>/<int:end_idx>")
def fib(start_idx, end_idx):
    if start_idx <= 0 or end_idx <= 0:
        return "Please, enter a positive number"
    elif start_idx >= end_idx:
        return "The start_idx must be bigger than end_idx"
    else:
        numbers = []
        for i in range(start_idx, end_idx + 1, 1):
            numbers.append(str(count(i)))

    return "Fibonacci sequence: " + ", ".join(numbers)


@app.route("/health")
def health():
    return render_template("health.html")


if __name__ == "__main__":
    app.run()
