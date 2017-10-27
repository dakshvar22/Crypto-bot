from crontab import CronTab
#init cron

pairs = ['XETHZUSD'
		,'XXBTZUSD'
		,'XXRPZUSD'
		,'XXMRZUSD'
		,'XXMRZUSD'
		]
vals = ['302.0'
		,'5650.0'
		,'0.20'
		,'87.0'
		,'91.0'
		]

direction = ['up'
		, 'down'
		, 'down'
		, 'down'
		, 'up'
		]

my_cron = CronTab(user='daksh')

for index,pair in enumerate(pairs):

	job = my_cron.new(command='/home/daksh/anaconda2/bin/python /home/daksh/cron/Crypto-bot/queryPrice_dev.py --currency_pair {0} --val {1} --direction {2}'.format(pair,vals[index],direction[index]),comment='queryPrice_'+pair)

	job.minute.every(3)

	my_cron.write()
