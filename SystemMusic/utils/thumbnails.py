import os
import httpx
from PIL import Image
from youtubesearchpython.__future__ import VideosSearch

def resize_image(image, max_width=1280, max_height=720):
    w_ratio = max_width / image.width
    h_ratio = max_height / image.height
    return image.resize((int(image.width * w_ratio), int(image.height * h_ratio)))

async def get_thumb(videoid):
    path = f"cache/{videoid}.png"
    if os.path.exists(path):
        return path

    try:
        result = (await VideosSearch(f"https://www.youtube.com/watch?v={videoid}", limit=1).next())["result"][0]
        thumb_url = result["thumbnails"][0]["url"].split("?")[0]

        async with httpx.AsyncClient() as client:
            r = await client.get(thumb_url)
            if r.status_code == 200:
                with open(path, "wb") as f:
                    f.write(r.content)

                img = Image.open(path)
                img = resize_image(img)
                img.save(path)

                return path
    except:
        pass
