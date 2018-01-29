. $HOME/.bashrc

cd $IRUKAHOME/log
gunerr='./gunicorn.err'
gunlog='./gunicorn.log'
uplog='./uploadlog.log'

resultfile='/root/smaugpython/.swxpy/smaug/send.data'
echo "" > $resultfile


echo "df -h:" >> $resultfile
df -h >> $resultfile
echo "" >> $resultfile

echo "tail -n 10 $gunerr:" >> $resultfile
tail -n 10 $gunerr >> $resultfile
echo "" >> $resultfile

echo "tail -n 10 $gunlog:" >> $resultfile
tail -n 10 $gunlog >> $resultfile
echo "" >> $resultfile

echo "tail -n 20 $uplog:" >> $resultfile
tail -n 10 $uplog >> $resultfile
echo "" >> $resultfile


cd $IRUKAHOME/data
kuaishoulog='./kuaishou.log'
echo "du -h $kuaishoulog:" >> $resultfile
du -h $kuaishoulog >> $resultfile
echo "" >> $resultfile

echo "ls $IRUKAHOME/data:" >> $resultfile
ls $IRUKAHOME/data >> $resultfile
echo "" >> $resultfile

echo "du -h kuaishou*:" >> $resultfile
du -h kuaishou* >> $resultfile
echo "" >> $resultfile

for file in `ls /root/iruka/data/*.log`
do 
  line=`tail -n 1 $file`
  echo "cat $file: $line" >> $resultfile
done

cd /root/smaugpython/.swxpy/smaug
. venv/bin/activate
python ./monitor.py
