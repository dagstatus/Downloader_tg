from youtube_dl import YoutubeDL
import aiofiles
import os
import re
import asyncio
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
path_dwld = 'temp'


async def dwld(url, user_id):
    if re.search('youtu', url):
        try:
            y_dwloader = YoutubeDL({'outtmpl': f'{path_dwld}/{user_id}.%(ext)s', "format": "mp4[height=480]",  'ignoreerrors': False})
            with y_dwloader:
                result = y_dwloader.extract_info(
                    url,
                    download=False  # We just want to extract the info
                )
            if result.get('duration') < 600:
                y_dwloader.download([url])
            return 'Благодарим за использование нашего бота'
        except Exception as exept_full:
            return 'Произошла ошибка скачивания'
            logging.WARNING(str(exept_full))

    else:
        y_dwloader = YoutubeDL({'outtmpl': f'{path_dwld}/{user_id}.%(ext)s'})
        y_dwloader.download([url])

async def delete_local_file(user_id):
    print('start del')
    print(os.listdir(path_dwld))
    for file in os.listdir(path_dwld):
        if re.search(str(user_id), file):
            async with aiofiles.open(f'{path_dwld}\{file}', mode='r', buffering=1) as f:
                await f.close()
                os.remove(f'{path_dwld}\{file}')
    print("deleted: "+file)



async def del_file(user_id):
    for filename in os.listdir(path_dwld):
        if re.search(user_id, filename):
            print(filename)
            try:
                os.remove(f'temp/{user_id}.%(ext)s')
            except Exception as exept:
                logging.WARNING(exept)



# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(delete_local_file('1111'))
#     loop.close()