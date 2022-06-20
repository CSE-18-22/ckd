cd app/
npm i
cd ../api/
brew install python3
python3 -m venv venv
pip install flask
pip install -U flask_cors
pip3 install -r requirements.txt
export FLASK_APP=app
cd ../
