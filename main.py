import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from aiogram_bot import AiogramBot
from tradingview import Tradingview

TOKEN = '6545309020:AAFF0LPsrhSQyKVloSqjLx_C_Rw6NI39c6o'
CHAT_ID = 173975362

aiogram_bot = AiogramBot(token=TOKEN, chat_id=CHAT_ID)

trading_pairs_array = [
    'BTCUSDT.P', 'ETHUSDT.P', 'BCHUSDT.P', 'XRPUSDT.P', 'EOSUSDT.P', 'LTCUSDT.P', 'TRXUSDT.P', 'ETCUSDT.P', 'LINKUSDT.P',
    'XLMUSDT.P', 'ADAUSDT.P', 'XMRUSDT.P', 'DASHUSDT.P', 'ZECUSDT.P', 'XTZUSDT.P', 'BNBUSDT.P', 'ATOMUSDT.P', 'ONTUSDT.P',
    'IOTAUSDT.P', 'BATUSDT.P', 'VETUSDT.P', 'NEOUSDT.P', 'QTUMUSDT.P', 'IOSTUSDT.P', 'THETAUSDT.P', 'ALGOUSDT.P', 'ZILUSDT.P',
    'KNCUSDT.P', 'ZRXUSDT.P', 'COMPUSDT.P', 'OMGUSDT.P', 'DOGEUSDT.P', 'SXPUSDT.P', 'KAVAUSDT.P', 'BANDUSDT.P', 'RLCUSDT.P',
    'WAVESUSDT.P', 'MKRUSDT.P', 'SNXUSDT.P', 'DOTUSDT.P', 'YFIUSDT.P', 'BALUSDT.P', 'CRVUSDT.P', 'TRBUSDT.P',
    'RUNEUSDT.P', 'SUSHIUSDT.P', 'EGLDUSDT.P', 'SOLUSDT.P', 'ICXUSDT.P', 'STORJUSDT.P', 'BLZUSDT.P', 'UNIUSDT.P', 'AVAXUSDT.P',
    'FTMUSDT.P', 'ENJUSDT.P', 'FLMUSDT.P', 'RENUSDT.P', 'KSMUSDT.P', 'NEARUSDT.P', 'AAVEUSDT.P', 'FILUSDT.P', 'RSRUSDT.P',
    'LRCUSDT.P', 'MATICUSDT.P', 'OCEANUSDT.P', 'BELUSDT.P', 'CTKUSDT.P', 'AXSUSDT.P', 'ALPHAUSDT.P', 'ZENUSDT.P', 'SKLUSDT.P',
    'GRTUSDT.P', '1INCHUSDT.P', 'CHZUSDT.P', 'SANDUSDT.P', 'ANKRUSDT.P', 'LITUSDT.P', 'UNFIUSDT.P', 'REEFUSDT.P',
    'RVNUSDT.P', 'SFPUSDT.P', 'XEMUSDT.P', 'COTIUSDT.P', 'CHRUSDT.P', 'MANAUSDT.P', 'ALICEUSDT.P', 'HBARUSDT.P', 'ONEUSDT.P',
    'LINAUSDT.P', 'STMXUSDT.P', 'DENTUSDT.P', 'CELRUSDT.P', 'HOTUSDT.P', 'MTLUSDT.P', 'OGNUSDT.P', 'NKNUSDT.P', 'DGBUSDT.P',
    'BAKEUSDT.P', 'GTCUSDT.P', 'IOTXUSDT.P', 'AUDIOUSDT.P',
    'C98USDT.P', 'MASKUSDT.P', 'ATAUSDT.P', 'DYDXUSDT.P', '1000XECUSDT.P', 'GALAUSDT.P', 'CELOUSDT.P', 'ARUSDT.P', 'KLAYUSDT.P',
    'ARPAUSDT.P', 'CTSIUSDT.P', 'LPTUSDT.P', 'ENSUSDT.P', 'PEOPLEUSDT.P', 'ANTUSDT.P', 'ROSEUSDT.P', 'DUSKUSDT.P', 'FLOWUSDT.P',
    'IMXUSDT.P', 'API3USDT.P', 'GMTUSDT.P', 'APEUSDT.P', 'WOOUSDT.P', 'JASMYUSDT.P', 'DARUSDT.P', 'GALUSDT.P', 'OPUSDT.P', 'INJUSDT.P',
    'STGUSDT.P', 'SPELLUSDT.P',  'LDOUSDT.P', 'CVXUSDT.P', 'ICPUSDT.P', 'APTUSDT.P',
    'QNTUSDT.P',  'FETUSDT.P', 'FXSUSDT.P', 'HOOKUSDT.P', 'MAGICUSDT.P', 'TUSDT.P', 'RNDRUSDT.P', 'HIGHUSDT.P',
    'MINAUSDT.P', 'ASTRUSDT.P', 'AGIXUSDT.P', 'PHBUSDT.P', 'GMXUSDT.P', 'CFXUSDT.P', 'STXUSDT.P', 'BNXUSDT.P', 'ACHUSDT.P', 'SSVUSDT.P',
    'CKBUSDT.P', 'PERPUSDT.P', 'TRUUSDT.P', 'LQTYUSDT.P', 'USDCUSDT.P', 'IDUSDT.P', 'ARBUSDT.P', 'JOEUSDT.P', 'TLMUSDT.P', 'AMBUSDT.P',
    'LEVERUSDT.P', 'RDNTUSDT.P', 'HFTUSDT.P', 'XVSUSDT.P', 'EDUUSDT.P', 'IDEXUSDT.P', 'SUIUSDT.P',
    'UMAUSDT.P', 'RADUSDT.P', 'KEYUSDT.P', 'COMBOUSDT.P', 'NMRUSDT.P', 'MAVUSDT.P', 'MDTUSDT.P',
    'XVGUSDT.P', 'WLDUSDT.P', 'PENDLEUSDT.P', 'ARKMUSDT.P', 'AGLDUSDT.P', 'YGGUSDT.P', 'BNTUSDT.P', 'OXTUSDT.P',
    'SEIUSDT.P', 'CYBERUSDT.P', 'HIFIUSDT.P', 'ARKUSDT.P', 'FRONTUSDT.P', 'GLMRUSDT.P', 'BICOUSDT.P', 'STRAXUSDT.P', 'LOOMUSDT.P',
    'BONDUSDT.P',  'STPTUSDT.P', 'WAXPUSDT.P', 'RIFUSDT.P', 'POLYXUSDT.P', 'GASUSDT.P',
    'POWRUSDT.P', 'SLPUSDT.P', 'TIAUSDT.P', 'SNTUSDT.P', 'CAKEUSDT.P', 'MEMEUSDT.P', 'TWTUSDT.P', 'ORDIUSDT.P',
    'STEEMUSDT.P', 'BADGERUSDT.P', 'ILVUSDT.P', 'NTRNUSDT.P', 'MBLUSDT.P'
]

async def job():
    code_execution_time  = datetime.now()
    print("Code executed at:", code_execution_time)

    # Call the synchronous function using asyncio.to_thread
    buy_sell_pairs_result = await asyncio.to_thread(
        Tradingview.get_buy_sell_pairs, trading_pairs_array
    )

    # Print the result
    print(buy_sell_pairs_result)

    # Send the message asynchronously
    buy_pairs = buy_sell_pairs_result['buy_pairs']
    sell_pairs = buy_sell_pairs_result['sell_pairs']
    if buy_pairs != [] or sell_pairs != [] :
        await aiogram_bot.send_message(f"Code Executed On : {code_execution_time}")
        await aiogram_bot.send_message(buy_sell_pairs_result)

    print('\n' + 100 * '=' + '\n')

async def main():
    scheduler = AsyncIOScheduler()

    # Add the job to the scheduler
    scheduler.add_job(job, 'cron', minute='*/5', second= 3)

    # Start the scheduler
    scheduler.start()
    print('Telegram Bot Strarted Successfully')
    print('\n')
    print('Scheduler Strarted Successfully')
    
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped.")
        scheduler.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
