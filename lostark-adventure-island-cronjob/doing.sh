NOWHOUR=$(date +%H)
NOWWEEKDAY=$(date +%u)

# 오전이면 명령 실행
if [ "$NOWHOUR" -lt 12 ]
then
  echo -n "${WEBHOOK_LIST}" | base64 --decode > ./lostark-adventure-island-cronjob/webhook_list.txt
  python3 ./lostark-adventure-island-cronjob/main.py
else
  if [ "$NOWWEEKDAY" -ge 6 ]
    then
      echo -n "${WEBHOOK_LIST}" | base64 --decode > ./lostark-adventure-island-cronjob/webhook_list.txt
      python3 ./lostark-adventure-island-cronjob/main.py
    fi
fi
