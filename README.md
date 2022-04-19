# mcGuessr
sub and top-level domain finder (designed for minecraft servers)

# Description
this tool (wich was designed for minecraft servers but can also work with normal domains), automatically scans for a valid subdomain and top-level for a domain of choice, printing in red the not-founds, in green the unique ip's and in yellow the duplicated ip's



![alt-text](https://github.com/kl3sshydra/mcGuessr/raw/main/screenshot.png)

# Setup
```
git clone https://github.com/kl3sshydra/mcGuessr
cd mcGuessr
bash setup.sh
python3 main.py
```

# Options
if you want to print only the found domains, just launch this program without any arguments.<br>
if you want to print both the founds and not founds, do:<br>
```python3 main.py --print-not-found```