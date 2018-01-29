. /root/.bash_profile
cd /root/smaugpython/.swxpy/smaug

. venv/bin/activate

python ./bot.py >> /root/smaugpython/.swxpy/smaug/log/server.log 2>&1 &
echo "execute server.sh" >> /root/smaugpython/.swxpy/smaug/log/server.log 
