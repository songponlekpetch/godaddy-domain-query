import pprint
import typer

from config import GO_DADDY_API_URL, GO_DADDY_API_KEY, GO_DADDY_API_SECRET
from services.go_daddy_service import GoDaddyService
from services.report_service import ReportService

app = typer.Typer(
    help="""
    Extract Domain from GoDaddy API.

    The standard process is to run the following commands:

    * `> python main.py show-columns` to show the columns available
    
    * `> python main.py show-domains` to show the domain information
    
    """,
    rich_markup_mode="markdown",
)

@app.command()
def show_columns() -> None:
    go_daddy = GoDaddyService(GO_DADDY_API_KEY, GO_DADDY_API_SECRET, GO_DADDY_API_URL)
    domains = go_daddy.get_domains()
    ReportService.get_columns(domains)

@app.command()
def show_domains(columns: str="domain,expires,status"):
    go_daddy = GoDaddyService(GO_DADDY_API_KEY, GO_DADDY_API_SECRET, GO_DADDY_API_URL)
    domains = go_daddy.get_domains()
    ReportService.create(data=domains, columns=columns.split(","))
    

if __name__ == "__main__":
    app()
