import subprocess
import StringIO

from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)
 
@app.route("/")
def test():
    return render_template('test.html')
 
@app.route("/runcode")
def runcode():
    result= os.popen("cd /Users/yashpahade/Desktop/Demo_terraform; terraform apply").read()
    return render_template('runcode.html',result=result)

@app.route("/delete")
def delete():
    result= os.popen("cd /Users/yashpahade/Desktop/Demo_terraform; terraform destroy -force").read()
    return render_template('delete.html',result=result)

@app.route("/iperf_server")
def iperf_server():
    return render_template('iperfserver.html')

@app.route("/genload")
def genload():
    s=''
    resp= subprocess.check_output (["iperf3", "-c", "192.168.1.235", "-V", "-b", "1024000000", "-t", "120"])
    for line in resp.splitlines():
        s += "<pre>" + line + "</pre> <br>\n"
    summary = s.split("- - - - - - - - - - - - - - - - - - - - - - - - -")
    output = summary[1]
    return output
if __name__ == "__main__":
    app.run(host = '0.0.0.0')
