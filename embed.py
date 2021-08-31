import discord
from coins_price import get_all_latest_price

def get_embed():
    data = get_all_latest_price()
    embed = discord.Embed(title='Cryptocurrencies price',
                          description='This is automatically send every hour',
                          color=0x00ffff)
    embed.clear_fields()
    for d in data:
        embed.add_field(name=d['symbol'],
                        value=round(d['price'], 2),
                        inline=True)
        embed.add_field(name='24hr %change',
                        value=str(round(d['percent_change_24h'], 2)) + '%',
                        inline=True)
        embed.add_field(name='7d %change',
                        value=str(round(d['percent_change_7d'], 2)) + '%',
                        inline=True)
        embed.set_footer(text='Data from https://coinmarketcap.com/')
    return embed
