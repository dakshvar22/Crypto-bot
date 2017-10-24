from crontab import CronTab
#init cron

pairs = ['XETHZUSD'
		,'XXBTZUSD'
		,'XXRPZUSD'
		,'XXMRZUSD'
		]
vals = ['301.0'
		,'5650.0'
		,'0.20'
		,'88.0'
		]

direction = ['down'
		, 'down'
		, 'down'
		, 'down'
		]

my_cron = CronTab(user='daksh')

for index,pair in enumerate(pairs):

	job = my_cron.new(command='/Users/daksh/anaconda2/bin/python /Users/daksh/personal/crypto/kraken/queryPrice_dev.py --currency_pair {0} --val {1} --direction {2}'.format(pair,vals[index],direction[index]),comment='queryPrice_'+pair)

	job.minute.every(3)

	my_cron.write()