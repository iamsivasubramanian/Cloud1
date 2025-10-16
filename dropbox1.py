from flask import Flask, request, send_file, redirect, url_for
import dropbox
import io

app = Flask(__name__)

ACCESS_TOKEN = "sl.u.AGC7ZKIHZTXgB9g0Ynsk0kX4ThSwIWzXISDN7hWJRDEixF2gBtE-uSCevCZmtlCK5neOP0GqMaNnLL0OJH_jNLf2VHeFblMttAQSS8sHLF4tZkGF9yPk5hG2t7sgVDkeSUjN2c10uLkfIvxTgz3Os46QClO0PgTxM46DYVCfrhUkC00M3nqWEW8URITkQev1WiXHq50cVZ9sPnzKuG1j6rAc51FMMRtxRQUMbpVzwZfj5zBM1-MIYW_tXDEUYk64Z-H_DutUYw_vLsSSdEhCOJjSmWoQDbpkgQTIib7HNJU8GXVSKKIfMXnDYl_CxKwi9Lf6aSFGgNcGLgn4yf1gtJywPzWqxBw7zKMv4oj5bccwU-kEjpPpEQ2EYhc3aoKndwGBV2HlkUUNpt8dv2ptGvJ8eNxS0GEqIASOW4CsukIjvCNf1RqaiW5sj6mDtajLCX7Ibk3wVfJ8qVGL9H6AQQG1t53xT1ovwHt2vQ7-aqcAPJzSXVjePeTzMwStx6POclXohTCXTW68WWykTqYE6_FV7SZVQ1ETy4boP-Yz_-tL62iEaNRX9ZueO7HV43qoL4qV9CbFurCZy0JQeFDoQEgD4JUnL7QNwiDB7GYFIBveYcPHkCrYoPf_yLjGwy0PcpZCMd0VGWc9atOD57LH0AO7KZ69m97IKrfnTA256vMOtEdJbtdol1i5jYgZvPrCp6zX1sjeI24Gl1tARWYAVXpzNEFJJufDcTJr-1UuHNn-HYpmcU6wy1szJAy66tQqEyYMvOLqRGuBlus0Cuva05pzvbVXMk5aprdJpe9ZHxzNhS5NNHxDx26kALcyIsnd4-U6F2h8P3MjKagSC3frjQpLF4G7Lw9TjQgLI68MNiQyx0nYsne09cXRmxpGyY8et_cvrakjIU0w0xE-aECN2sis-Dmae61fLE2pgi9cVZhd_EAD5pZ4nmeUbWr54jPfR53RaYmZOEMPGXZWvWZvv0qLqe1TPKbGUn3dHpgxfVrDLs4Jzns02NV2ahO9KzWNCxj0ApCOiTd3mNjz8nJz1X-uxHILSMlfAf45lyoKVHqdbe3OTqxBdelmRDsGLxBcGAmU11ttCPRUM6-R4H44hrLsRTud3duxAtXbOyIsnBqhpbBkOwBV0mV45iEQaYk0kbmOvScjCmxhGm7hmlNEXcOuyHBy2LPJTQO7Qc8JKpDf4nJWkbPbVzPYTo1VFs_RztSiAnWwaIzb-7CJvBxrdYjKrzMqka1Go0GlV4H6mQPCmuGUh6SyHKJe1fjrWzB4ztkIV9XgSDofdW6J-2Mxe6kDb5_fWC5kksNydFblxa4NO8PkTagf8-o2dOoZRZj4rUnHylkiVprLx7sSI-M6ZllkmevKkJbXRrarNyEe49KEnp3hH73sBipGsLbNDYx606jQVpY3kH4a6yW_0mu0AfgFUaBOHJRFiQHe-csVElNfRNk22g5sKmE55XcpFJMYfIamN4nrDKJICeXEjMXQqVmX"
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Home page: upload + download form
@app.route('/')
def home():
    return '''
    <h2>Upload File to Dropbox</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    <br><br>
    <h2>Download File from Dropbox</h2>
    <form action="/download" method="post">
        <input type="text" name="filename" placeholder="Enter filename to download">
        <input type="submit" value="Download">
    </form>
    '''

# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return "No file selected."
    dropbox_path = f"/MyUploads/{file.filename}"
    try:
        dbx.files_upload(file.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
        return f"✅ '{file.filename}' uploaded successfully to Dropbox folder!"
    except Exception as e:
        return f"❌ Upload failed: {e}"

# Download route
@app.route('/download', methods=['POST'])
def download():
    filename = request.form.get('filename')
    if not filename:
        return "No filename provided."
    
    dropbox_path = f"/MyUploads/{filename}"
    try:
        metadata, res = dbx.files_download(dropbox_path)
        file_stream = io.BytesIO(res.content)
        return send_file(file_stream, as_attachment=True, download_name=filename)
    except Exception as e:
        return f"❌ Download failed: {e}"

if __name__ == '__main__':
    app.run(debug=True)
