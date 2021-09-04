NOWHOUR=$(date +%H)
NOWWEEKDAY=$(date +%u)

# 오전이면 명령 실행
if [ "$NOWHOUR" -gt 12 ]
then
  python3 main.py
else
  if [ "$NOWWEEKDAY" -ge 6 ]
    then
      python main.py
    fi
fi
