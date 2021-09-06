NOWHOUR=$(date +%H)
NOWWEEKDAY=$(date +%u)

# 오전이면 명령 실행
if [ "$NOWHOUR" -lt 24 ]
then
  echo -n "${WEBHOOK_LIST}" | base64 --decode > ./webhook_list.txt
  python3 main.py
else
  if [ "$NOWWEEKDAY" -ge 6 ]
    then
      echo -n "${WEBHOOK_LIST}" | base64 --decode > ./webhook_list.txt
      python3 main.py
    fi
fi
