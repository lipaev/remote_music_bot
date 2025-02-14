from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

stickers = ['CAACAgIAAxkBAAIEimcBOTDVRItWl1a4Gm0yV2jRhI2HAAKJAAMWQmsKRsvaWiyCsI42BA', 'CAACAgIAAxkBAAIEi2cBOTp7-YSQlgRvsajWc7f5cnx0AAIFPQACJSZpSMuuBLfxSXn2NgQ', 'CAACAgIAAxkBAAIEjGcBOVB19Y7VsZy_Tk1ImH306bkTAAJKBwACRvusBCNCmw1f3sTgNgQ', 'CAACAgIAAxkBAAIEjWcBOVqAGz6c1ISWvpsET8TSw1NzAALUGgAC2O4pSaBKbMFsS3S5NgQ', 'CAACAgIAAxkBAAIEjmcBOWCctoFjO63uMvEbSQFaN2oDAALjBQACP5XMCtgzraXSP7U0NgQ', 'CAACAgIAAxkBAAIEj2cBOWcrN6cpVAousKlzHxcEieiNAAI3AQACUomRI9UUQKd8bRIaNgQ', 'CAACAgIAAxkBAAIEkGcBOY5iPppCbXEk8Iqv4Oxjp0mdAAJaBwACRvusBIK0AX12IQG3NgQ', 'CAACAgIAAxkBAAIEkWcBOaBgmR0AARch482k52hC9ehIrgACnhAAAnYH-UsPzzlGLS-LBzYE', 'CAACAgIAAxkBAAIEkmcBObFeM3abxhP_7iuPXWWuXQW8AAKGAANEDc8XmHJJtmRJq7E2BA', 'CAACAgIAAxkBAAIEk2cBOb7eTWcaNb9IbgbsKzTkXY7_AAKzCwACKlBRSiyjtgnsadPWNgQ', 'CAACAgIAAxkBAAIEfmcBNhZ39Fw0v80Lz1Mi_SxQscVqAAIiAwACbbBCA7zHw9-hcLV4NgQ', 'CAACAgIAAxkBAAIElWcBOekgvKrbg-qthptkYhaGO0scAALdAAMw1J0RjVUlFacabq82BA', 'CAACAgIAAxkBAAIEl2cBOgG3_bNsR0txihcERgphdxceAAJMAANEDc8XTRtr1DoEB9A2BA', 'CAACAgIAAxkBAAIEmGcBOgxSjoHitbxfrUS8JmMT-vJBAAKgDAACdRjYS3aHIiVfD-VhNgQ', 'CAACAgIAAxkBAAIEmWcBOh9ZXBH09mhVKop4ZLWgu41WAALvAAPkoM4Hr4elAAGmzOB0NgQ', 'CAACAgIAAxkBAAIEmmcBOiegO--cSC8XNWMpEH1gCDSHAAL8CwACyCPoS7zjzQaY20MeNgQ', 'CAACAgIAAxkBAAIEm2cBOj71hwbX_UHTLJGG9ZhYVid7AAKBAAPBnGAM6PbLODBd3jc2BA', 'CAACAgIAAxkBAAIEnGcBOlmdyp1GGp0-D3u0eQHfhbGlAAJMAQACMNSdEffeb183gzkcNgQ', 'CAACAgIAAxkBAAIEnWcBOmQAAZnfmhsM1v2rb1t_CnALvQACIgADKA9qFBEx-ROlx0RXNgQ', 'CAACAgIAAxkBAAIEnmcBOm-Q8SxNns1gfs9DhAga2bYXAAJUAQACIjeOBJ6cKg4hDmDNNgQ', 'CAACAgIAAxkBAAIEn2cBOndDBJMp463Mj0XL_2dWAxflAAInCQACGELuCBKfUsx4Hdr9NgQ', 'CAACAgIAAxkBAAIEoGcBOqK8Qya1BX2MM6KExdQWVPj9AAJHAwACtXHaBjV7c9kAAYsdpDYE']

b = {'⏪': ('prevtrack', 1),
         '⏯': ('playpause', 1),
         '⏩': ('nexttrack', 1),
         '🔊 ⬆️': ('volumeup', 4),
         '🔉 ⬇️': ('volumedown', 4),
         '⬅️': ('left', 1),
         '➡️': ('right', 1),
         '⟪J': ('j', 1),
         'K': ('k', 1),
         'L⟫': ('l', 1),
         '[F]': ('f', 1)}

relingo = {'Shift + ⬅️': ('shift;;;left', 1),
           'Pause ⏯': ('playpause', 1),
        'Shift + ➡️': ('shift;;;right', 1),
         '🔊 ⬆️': ('volumeup', 4),
         '🔉 ⬇️': ('volumedown', 4),
         '[F]': ('f', 1)}

@dataclass
class TgBot:
    token: str
    admins_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot
    stickers: list[str]
    b: dict[str, tuple[str, int]]
    relingo: dict[str, tuple[str, int]]

config = Config(
    tg_bot=TgBot(
        token=getenv('BOT_TOKEN'),
        admins_ids=eval(getenv('ADMINS_IDS'))),
    stickers=stickers,
    b=b,
    relingo=relingo)
