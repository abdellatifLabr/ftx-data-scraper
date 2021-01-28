from celery import shared_task


@shared_task
def get_futures_markets():
    print('GETTING FUTURES MARKETS...')


@shared_task
def get_and_calculate_spreads():
    print('GETTING SPREADS...')
