from flask import Flask, render_template, request
import math

app = Flask(__name__)

def binomial_probability(n, k, p):
    """
    Menghitung probabilitas binomial P(X = k).
    """
    if k > n or p < 0 or p > 1:
        return 0
    comb = math.comb(n, k)  # Kombinasi nCk
    return comb * (p ** k) * ((1 - p) ** (n - k))

def binomial_cdf(n, k, p):
    """
    Menghitung probabilitas kumulatif binomial P(X <= k).
    """
    cdf = 0
    for i in range(k + 1):
        cdf += binomial_probability(n, i, p)
    return cdf

@app.route("/", methods=["GET", "POST"])
def index():
    prob = None
    cdf = None
    n = None
    p = None
    k = None

    if request.method == "POST":
        try:
            # Mengambil input dari form
            n = int(request.form["n"])
            p = float(request.form["p"])
            k = int(request.form["k"])
            
            # Hitung probabilitas dan CDF
            prob = binomial_probability(n, k, p)
            cdf = binomial_cdf(n, k, p)
        except ValueError:
            prob = None
            cdf = None

    return render_template("index.html", prob=prob, cdf=cdf, n=n, p=p, k=k)

if __name__ == "__main__":
    app.run(debug=True)
