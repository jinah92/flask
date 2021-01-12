from datetime import datetime, timedelta

def createDateTime():
    # 요청할 base_date, base_time 계산
    now = datetime.now()

    # 40분 이전 => 현재 시보다 1시간전 'base_time'을 요청
    if now.minute < 40:
        # 00:40 이전이면 => 'base_date'는 전날, 'base_time'은 2300
        if now.hour == 0:
            base_date = (now - timedelta(days=1)).strftime('%Y%m%d')
            base_time = '2300'
        else:
            base_date = now.strftime('%Y%m%d')
            base_time = (now - timedelta(hours=1)).strftime('%H00')
    # 40분 이후 => 현재 시와 같은 'base_time'을 요청
    else:
        base_date = now.strftime('%Y%m%d')
        base_time = now.strftime('%H00')

    return base_date, base_time
