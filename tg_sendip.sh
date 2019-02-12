#!/bin/bash
set -x

msg=$1
tgpath=/home/aida/tg
cd ${tgpath}


(echo "contact_list";sleep 1; echo "msg Nicholas_Dykeman $msg"; echo "safe_quit") | ${tgpath}/bin/telegram-cli -k tg-server.pub -W

#sudo chmod -R 0655 teletest.sh
