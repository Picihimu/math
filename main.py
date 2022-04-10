# import math
# import colorama
# from colorama import Fore
# print(f'{Fore.GREEN}1.(a + b)^2')
# print(f'{Fore.RED}2.(a - b)^2')
#
# colorama.init(True)
#
# choice = int(input("type the number: "))
#
# a = int(input("What's the Value of a : "))
# b = int(input("What's the Value of b : "))
# # c = int(input("What's the Value of c : "))
#
# if choice == 1:
#     print(f"(a + b)^2")
#     print(f"({a}+{b})^2")
#     print("a^2 + 2ab + b^2")
#     print(f"{a * a} + {2 * a * b} + {b * b}")
#
# elif choice == 2:
#     print(f"(a - b)^2")
#     print(f"({a}-{b})^2")
#     print("a^2 - 2ab + b^2")
#     print(f"{a * a} - {2 * a * b} + {b * b}")
#
# # elif choice == 2:
# # elif choice == 2:
# # elif choice == 2:
# # elif choice == 2:
# # elif choice == 2:


from flask import Flask
app = Flask(__name__)


@app.route('/about')
def about_page():
    return "about"


# # index
# @app.route('/')
# def index():
#     return "Hello112"


@app.route('/')
def home():
    return "world"


# def run():
#   app.run(host='0.0.0.0',port=8080)

# /me
@app.route("/me", methods=["GET"])
def get_results():
    return "Dummy Result"

#
# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")
