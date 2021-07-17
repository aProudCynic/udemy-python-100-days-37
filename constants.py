from secrets import API_TOKEN

USERNAME = "aproudcynic"
URL_BASE = "https://pixe.la/v1/users"
GRAPH_ID = "habit-tracker"
GRAPH_URL = f"{URL_BASE}/{USERNAME}/graphs/{GRAPH_ID}"
TOKEN_API_HEADER = {
    "X-USER-TOKEN": API_TOKEN,
}