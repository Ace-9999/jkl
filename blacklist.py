from discord.ext.commands import Cog, command, has_permissions
import discord, json
from library import funcs


class blacklist(Cog, name='blacklist'):
	def __init__(self, bot):
		self.bot = bot

	@command(name='blacklist')
	@has_permissions(kick_members=True)
	async def blacklist(self, ctx, userid:int, *, reason=None):
		role1 = discord.utils.get(ctx.guild.roles, id=850757324116066315)
		"""role2 = discord.utils.get(ctx.guild.roles, id=761540775523123220)
		role3 = discord.utils.get(ctx.guild.roles, id=752263653495144538)"""
		with open('data/blacklist.json','r') as f:
			black = json.load(f)
		user = ctx.guild.get_member(userid)
		if userid in black["users"]:
			return await ctx.send('Already Blacklisted.')
		if not user:
			black["users"].append({userid:reason})
		else:
			await user.add_roles(role1)
			black["users"].append({userid:reason})
		with open('data/blacklist.json','w') as f:
			json.dump(black,f)
		await ctx.send(f'Blacklisted User')
		
"""	@Cog.listener("on_message")
	async def check4bl(message):
		return # to think of a sys until thought of roles	"""	
	
def setup(bot):
	bot.add_cog(blacklist(bot))