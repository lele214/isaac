py -3 -m venv .venv

.venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Output "---> All ok"
$Rsp = Read-Host "Want to start the website ? 'y for yes'"
if ($Rsp -eq "y") {
    Flask --app .\main.py run
}else {
    Write-Output "Then if you want to start the website do Flask --app .\main.py run"
}
