import logging
import azure.functions as func
import pyodbc


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Made it")
    return func.HttpResponse("Made it!")
