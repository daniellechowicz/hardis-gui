if exist venv (
  echo Virtual environment already exists 
) else (
  py -3 -m venv venv
  pip install -r requirements.txt
)