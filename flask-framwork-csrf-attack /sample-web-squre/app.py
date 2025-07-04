from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def squarenumber():
    if request.method == "POST":
        num = request.form.get("num")

        if not num or not num.isdigit(): #isdigit() which chek the num a int
            return "<h3>Invalid number</h3>"

        number = int(num)
        square = number ** 2
        return render_template("result.html", num=number, square=square)

    return render_template("squarenum.html")

if __name__ == "__main__":
    app.run(debug=True)