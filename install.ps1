py -3 -m venv .venv

.venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Output "---> All ok"