from pydantic import BaseModel


class Amount(BaseModel):
    issue_amt: int = 0
    pr_amt: int = 0
    push_amt: int = 0
    non_provide_amt: int = 0
