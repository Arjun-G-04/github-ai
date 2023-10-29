from datetime import datetime
import pathway as pw
import threading
from pathway.internals import api
import re
from dotenv import load_dotenv
import os
load_dotenv()

repo = os.environ.get("REPO_NAME", "")

def return_table(table: pw.Table, *, include_id=True, short_pointers=True):
    keys, columns = pw.debug.table_to_dicts(table)
    if not columns and not include_id:
        return
    if include_id or len(columns) > 1:
        none = ""
    else:
        none = "None"
    def _format(x):
        if x is None:
            return none
        if isinstance(x, api.Pointer) and short_pointers:
            s = str(x)
            if len(s) > 8:
                s = s[:8] + "..."
            return s
        return str(x)

    def _key(id):
        return tuple(
            pw.debug._NoneAwareComparisonWrapper(column[id]) for column in columns.values()
        )
    try:
        keys = sorted(keys, key=_key)
    except ValueError:
        pass
    data = []
    if include_id:
        if columns:
            name = ""
        else:
            name = "id"
        data.append([name] + [_format(k) for k in keys])
    for name, column in columns.items():
        data.append([name] + [_format(column[k]) for k in keys])
    max_lens = [max(len(row) for row in column) for column in data]
    max_lens[-1] = 0
    myData = ''
    for row in zip(*data):
        formatted = " | ".join(
            value.ljust(max_len) for value, max_len in zip(row, max_lens)
        )
        if formatted.rstrip() == "data":
            continue
        myData+=(formatted.rstrip())
        myData+="\n"
    return myData    

def reorder_string(string):
    lines = string.splitlines()
    dates = {}
    for line in lines:
        date_match = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", line)
        if date_match:
            date_str = date_match.group()
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
            if date not in dates:
                dates[date] = []
            dates[date].append(line)

    sorted_lines = []
    for date in sorted(dates.keys()):
        sorted_lines.extend(dates[date])

    return "\n".join(sorted_lines)

class InputSchema(pw.Schema):
  author: str
  message: str
  date: str

class issuesSchema(pw.Schema):
    title:str
    login:str
    body:str
    isPR:bool

t = pw.io.http.read(
  "http://localhost:4000/commits",
  method="GET",
  schema=InputSchema,
  format="raw",
)

k = pw.io.http.read(
  "http://localhost:4000/issuesAndPR",
  method="GET",
  schema=InputSchema,
  format="raw",
)


def print_data(t,k):
  data = return_table(t, include_id=False)
  reordered_string = reorder_string(data)
  with open(f"./{repo}/commits.jsonl", "w+") as f:
    for line in reordered_string.splitlines():
      objLine = eval(line)
      f.write('{"docs": "commit '+ objLine["message"]+" made by "+ objLine["author"] + " on " + objLine["date"] + ' "}\n')
  data1 = return_table(k, include_id=False)
  reordered_string1 = reorder_string(data1)
  with open(f"./{repo}/prAndIssues.jsonl", "w+") as f:
    for line in reordered_string1.splitlines():
      objLine=eval(line)
      if(objLine['isPr']==False):
        f.write('{"docs": "Issue '+ objLine["title"]+ " made by " + objLine["login"]+ " on " + objLine["date"] + " containing the body " + objLine["body"] + ' "}\n')
      else:
        f.write('{"docs": "Pull Request '+ objLine["title"]+ " made by " + objLine["login"]+ " on " + objLine["date"] + " containing the body " + objLine["body"] + ' "}\n')
        

def timer_callback():
  print_data(t,k)
  threading.Timer(1, timer_callback).start()

timer = threading.Timer(1, timer_callback)
timer.start()
pw.run(debug=True)



