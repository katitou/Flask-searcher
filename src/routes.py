from flask import Blueprint, Flask, render_template, request
from markupsafe import escape
from src.requests import log_request
from src.search import search


router = Blueprint("routes", __name__)


def register_routes(app: Flask) -> None:
    app.register_blueprint(router)


class RouteManager:
    def __init__(self):
        self.controller = RouteController()

    @router.route("/")
    @router.route("/entry", methods=["GET"])
    def entry_page(self) -> str:
        entry_page = self.controller.create_entry_page()

        return entry_page

    @router.route("/search", methods=["POST"])
    def do_search(self) -> str:
        search = self.controller.do_search()

        return search

    @router.route("/viewlog", methods=["GET"])
    def view_log(self) -> str:
        log = self.controller.view_log()

        return log


class RouteController:
    def __init__(self) -> None:
        self.data_base = "DataBse"

    def create_entry_page(self) -> str:
        return render_template("entry.html", the_title="Search for Letters online")

    def do_search(self) -> str:
        phrase = request.form["phrase"]
        letters = request.form["letters"]
        results = str(search(phrase, letters))
        log_request(request, results)

        return render_template(
            "results.html",
            the_title="Results searching for letters",
            the_results=results,
            the_phrase=request.form["phrase"],
            the_letters=request.form["letters"],
        )

    def view_log(self) -> str:
        titles: list[str] = ["Remote addr", "User agent", "Form Data", "Results"]
        log_list: list[list[str]] = []
        with open("search.log", "r") as log:
            for line in log:
                log_list.append([])
                for item in line.split("|"):
                    log_list[-1].append(escape(item))

        return render_template(
            "request.html", the_title="View Log", row_titles=titles, data=log_list
        )
