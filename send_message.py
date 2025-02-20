import requests
import time
import logging
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(filename='groupme_bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_message(bot_id, message):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': bot_id,
        'text': message
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 202:
            logging.info(f'Message sent successfully to bot {bot_id}!')
        else:
            logging.error(f'Error sending message to bot {bot_id}: {response.status_code}')
            logging.error(response.text)
    except Exception as e:
        logging.error(f'Exception occurred while sending message to bot {bot_id}: {str(e)}')

def send_messages_to_account(bot_ids, message):
    for bot_id in bot_ids:
        send_message(bot_id, message)
        time.sleep(2)  # Interval between messages to different groups

def main():
    # Bot IDs for Account 1
    account_1_bots = [
'9b61fe19ba6c7b953c21abb907',
'd75c02b0c805fdd7283262f87a',
'4fa02b883456c5d8ef78fc4a1f',
'b51b43bbc7626287a5e61d0a02',
'd06bef86924aee0d05dbb61858',
'a9b456067e96ac1506f02f5a40',
'6a9bd49563e6488058beed17f0',
'4c2fce7f90ab53bc9f96faa2db',
'e9e4ff631c4fd8a0f4db5172cb',
'876549f24fb5fd9a3db4561c30',
'96a6e0a46c3c9d7e0b1c030f5a',
'e5bfd2b40ba25426ec4f2620cc',
'ac79f0e05a98a7981f7c82dd0b',
'23c65c37f27a8f9410f4a64c4c',
'f3e72b8c4e6419c9be7018f9a5',
'78e2cf522592ae55e4ca70b222',
'e912953312f3e5e1ae2dd26084',
'61d64daae1a7ab7fbdcb457170',
'33d95b6fc9b1f712ffd66f9087',
'b1111264beebda6c4d8dbdb97f',
'501aa907b04328e66aa2e1dd13',
'21e198c78d835fb99ae6ee0a86',
'87f16cc59b14d2d137a7af66e5',
'18326ff81aff678b38c54c0e64',
'925b82b20a06f8d119f8278bc3',
'9d3abe1997fcd2aa18c0ebab46',
'c2db28161f4d7cf6d38832f7ac',
'c9b453ce115b1a19a247ff5854',
'546111c385a12b4fd196083919',
'0ec6d0daca7c73a8fa817ca3df',
'e07f09264f4d84bab8b7625dbf',
'a76789bf0c8b6626229e4d4293',
'd6495c6fc3e48e60cc9f4afba7',
'2c20dc3769d79bfb832af5e828',
'd3a9bdfbc580b0e07b8e5ba9c7',
'640746ed634db104b1695fe1ea',
'81b2babb52a9d5f2229bbbde0d',
'a4573d98c2f7bbad7d15f2c3c5',
'e9fb441286db7347f69e51f21a',
'4565fbd4372c066d0734007800',
'83976c7eec655c913ffcb99d24',
'fa5db4fe391005a0743dee9151',
'074694d840bd75ba4f0149ce7a',
'73f58f9534cbbba61952bd099f',
'8a1635de02b1f7e09ff6d4319b',
'0f7cd635f15a0055266dd231d1',
'f735ca08e5c9f9f4ad5f8799c8',
'933a25b86377eb9d9ba6493570',
'dc3a56b082637aa7a4af1f3ad7',
'90a641234c4b158fdcacb885f2',
'f387444fcda0f79f6a7adfe7a2',
'd90bcef7ca4edf9475508f5ba5',
'a1269e557b9f42399066c767d9',
'b717ce28a7c33d3e24cadf180f',
'e9e82ee453c1be7c1cc28007f3',
'47d77d5c79a2f97ef661d9dc45',
'18ae4221ad206ad0b0e38df279',
'b1e7b626c4599fe83233c7cb3a',
'a71467a12e0ddc0b78008504db',
'874f2cf9c373fd13dac9642008',
'301230452ded9b02975f7b3870',
    ]

    # Bot IDs for Account 2
    account_2_bots = [
'ac98e0b3e5dab0ccb4ee1d72f9',
'92311b1c2d6b0dac7532516327',
'73ddc97f7517a9367d7982a7f3',
'223e1b151f5cf12c11357abe81',
'be5543187921ba3f017d6ee210',
'52e5d097b299b477a89b0265d4',
'3b2243c76e8fd77b9e57500688',
'8d000904800afa8d138a4ed0aa',
'fbf9c8af7276e7c046713cb2ed',
'2878aeb2374584c445558602de',
'71340a2032afc2b9bd039d4eb4',
'f839876e3afe7ab976ce94ec74',
'42c0ee598a560bfec24fcd7e14',
'e488f585d1a1131ca044a65f03',
'6a9669042f64b59680a61f2e6b',
'63cd9f60b592e51a129c2f123f',
'6f820305c74cc69f6726e3bb23',
'1786956a55fed4dda073d2170f',
'e78d86c75b79a549021f32b024',
'1b0fa07412c2a5ca6b1b58db35',
'a871a28bc8f33f5362e0033b52',
'388c17d7ccfd55e5bac72603f7',
'151808385e001f800745effd40',
'ddd1bdb74fa180fc5e07f9106c',
'bce86541cf11088249d40fc7bf',
'c03de24b7683a37ddb691ca23d',
'5484a9384b7ba9abd5e2487d6a',
'e92e96dae41f4f33f2c857034a',
'04c3e523f470ef4e41fca51dbf',
'f2ae5b8ed1aecd66555e2013ab',
'6b6d2ceb61dc77fdd5a3ca49db',
'478d326c2d82b10f95559d7a7f',
'd614bef92ca42bb3bc689cff81',
    ]

    # Bot IDs for Account 3
    account_3_bots = [
        'c2dc08658afcae53830115aa38',
        '3390dbce8c71447fac43452b99',
        '9964a5bf5753f4acf1991e3a21',
        '87cf8fcb0b081539a88029ec4c',
        '146de6c5d348e3287c075593f4',
        '1177b09014c5175b0778160fdc',
        '77c02e46bed3765a66da0f9d11',
        'e8e59ee33fcccfd2ac83893927',
        'e4fe832e2f621a49c18e0f2d76',
        '5063fe802ffbba3260d8678d86',
        'dcdae03712a588da5cd84d2ec0',
        'ca53ec9d5704f2352243953f9c',
        '92a636f6fca54939fb5940ba92',
        'bca3917b668cc5ff6438db1e81',
        'deeef1f5470f22ca5b18e1c180',
        '34943a9fe54bab14c7a434e8f2',
        'e7ceac27b1a6e0193e10e59063',
        '48a8df7d64db75f43fb8057529',
        '8ea2ba1676667a54629702fc85',
        '3106fb0310ba028dc91b7bf8dd',
        '6ba479d30faf096daae263ce0e',
        '257dd132d863c7d5cf54184139',
        '51c93286da63b885eb1c5457d1',
        '6c0e2e0c3635ddfef66c9461a7',
        '0bcea5d1505e2216c443824ec0',
        '5972cfd879a4f405f0df2afcca',
        '9cb2675cdfa273e76c1d029532',
        '532295dd1ff5ea15b9e6f7d446',
        '8f8d9361c0aaf51df799a8ed56',
        '9474c340f44148187029c0b44e',
        'a7caf145fa2eec4f2a0113bdfa',
        '9b1e18aae5dfd123119df6d7f3',
        'c7cd6219d1a1c79cbe9d404a99',
        'bda31d00dbe95d6ba6192cba46',
        'bb95172ca93c9bc9a3e730a256',
        'f8ce5d90faacf7a56df998bab0',
        '14415b77d0c0951dfb3e16e178',
        'e57b7c8f482a7eff58fcde3d43',
        '174d0e82146793afb1370f778c',
        'f601f402313ad9760be6b52f6e',
        'bbd32d4c4308d4163a59338fc3',
        'f02387b6a88ae6bd639ba227fb',
        '45f63fc2be040339369d8bad00',
        '88577de288e861cfe31581bd8f',
        'a38c59a916a5bad9077a27671a',
        'f205f35038e25ba3e75e61915a',
        'cfdff8528cfc14a6c0335b6ecc',
        'c0fa7ec596812ffcbe7659db88',
        'f9fd9e0c031bd85fc8237a654f',
        'a56150bb882ea448e5f0787143',
        'cec81814788c910741abc90763',
        'ee6ecd3486bce81e4510eccc4e',
    ]

    # Messages for each account
    message_account_1 = (
    "Want an essay done today? visit the link to get quality and plagiarism free essays at the best price!! https://essayme.odoo.com/essay"
    )

    message_account_2 = (
    "Want an essay done today? visit the link to get quality and plagiarism free essays at the best price!!  https://essayme.odoo.com/essay"
    )

    message_account_3 = (
    "Want an essay done today? visit the link to get quality and plagiarism free essays at the best price!!  https://essayme.odoo.com/essay"
    )       
    # Time configuration
    start_time_account_1_2 = datetime.now().replace(hour=18, minute=23, second=00, microsecond=0)
    start_time_account_3 = datetime.now().replace(hour=18, minute=23, second=00, microsecond=0)
    end_time = datetime.now().replace(hour=11, minute=00, second=00, microsecond=0) + timedelta(days=1)
    interval = timedelta(hours=0, minutes=40, seconds=00)
    current_time = datetime.now()
    if current_time < start_time_account_1_2:
        wait_time = (start_time_account_1_2 - current_time).total_seconds()
        logging.info(f'Waiting for {wait_time / 60} minutes to start sending messages for accounts 1 and 2.')
        time.sleep(wait_time)

    while datetime.now() < end_time:
        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.submit(send_messages_to_account, account_1_bots, message_account_1)
            executor.submit(send_messages_to_account, account_2_bots, message_account_2)

            if datetime.now() >= start_time_account_3:
                executor.submit(send_messages_to_account, account_3_bots, message_account_3)

        next_run_time = datetime.now() + interval
        wait_time = (next_run_time - datetime.now()).total_seconds()
        logging.info(f'Waiting for {wait_time / 60} minutes until next round of messages.')
        time.sleep(wait_time)

if __name__ == '__main__':
    logging.info('Starting to send messages to all bots')
    main()
    logging.info('Finished sending messages to all bots')