from pydantic import BaseModel


class AnalyzedWebHookResponse(BaseModel):

    def __init__(self,
                 sender: str, event_type: str,
                 repo_name: str, repo_url: str,
                 event_url: str,
                 *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.sender = sender
        self.event_type = event_type
        self.repo_name = repo_name
        self.repo_url = repo_url
        self.event_url = event_url
